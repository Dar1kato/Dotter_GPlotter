from constants import *
from pipette import pipette_press, pipette_release
from tip import tip_change
from sample import get_sample
import json

OUTPUT_FILE = "export.gcode"

def config(file) -> None:
    """
    Writes the basic configuration codes to the file

    Args:
        file (file): route to the file where the GCode will be written
    """
    write(file, "G21 ; Unidades en milímetros")
    write(file, "G17 ; Plano XY")
    write(file, "G90 ; Coordenadas absolutas")
    write(file, "G94 ; Feed rate en unidades/minuto")
    write(file, "G28 ; Homing")
    write(file, f"G0 Z{BASE_HEIGHT:.3f} F{TRAVEL_SPEED} ; Subir a altura segura")


def translate_coordinates(file, data: dict) -> None:
    """
    Converts Dotter JSON into GCode

    Args:
        file (file): route to the file where the GCode will be written
        data (dict): data extracted from the Dotter JSON, structured as {color: [(x1, y1), (x2, y2), ...], ...}
    """
    tip_index = 0
    
    for color, points in data.items():
        write(file, f"\n; ========== COLOR: {color.upper()} ==========")
        tip_change(file, tip_index)
        tip_index += 1
        get_sample(file, color)
        for x, y in points:
            real_x = x * DISC_SPACING
            real_y = y * DISC_SPACING
            write(file, f"G0 X{real_x:.3f} Y{real_y:.3f} F{TRAVEL_SPEED} ; Punto disco ({x},{y})")
            write(file, f"G1 Z{INSERTION_HEIGHT:.3f} F{WORKING_SPEED} ; Dispensar")
            pipette_press(file)
            write(file, f"G1 Z{BASE_HEIGHT:.3f} F{WORKING_SPEED} ; Subir")
            pipette_release(file)

    # Program end
    write(file, "\n; --- Fin del programa ---")
    write(file, f"G0 Z{BASE_HEIGHT:.3f} F{TRAVEL_SPEED} ; Subir seguro")
    write(file, "G0 X0.000 Y0.000 F{TRAVEL_SPEED} ; Volver al origen")
    write(file, "M2 ; Fin del programa")


def main() -> None:
    # Load JSON data
    with open("coordinates.json", "r") as f:
        data = json.load(f)

    # Generate GCode
    with open(OUTPUT_FILE, "w") as file:
        config(file)
        translate_coordinates(file, data)

    print(f"GCode generado: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()