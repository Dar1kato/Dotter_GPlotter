# gcode_generator.py
import constants
import json

OUTPUT_FILE = "export.gcode"

def write(file, line: str) -> None:
    file.write(line + "\n")

def config(file) -> None:
    write(file, "G21 ; Unidades en milímetros")
    write(file, "G17 ; Plano XY")
    write(file, "G90 ; Coordenadas absolutas")
    write(file, "G94 ; Feed rate en unidades/minuto")
    write(file, "G28 ; Homing")
    write(file, f"G0 Z{constants.BASE_HEIGHT:.3f} F{constants.TRAVEL_SPEED} ; Subir a altura segura")

def pipette_press(file) -> None:
    # Aquí va tu lógica de actuador (servo, solenoide, etc.)
    # Por ahora usa un dwell como placeholder
    write(file, "G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)")

def pipette_release(file) -> None:
    write(file, "G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)")

def tip_release(file) -> None:
    write(file, "; --- Soltar punta ---")
    write(file, f"G0 X{constants.BIN_X:.3f} Y{constants.BIN_Y:.3f} F{constants.TRAVEL_SPEED} ; Mover a cubeta")
    write(file, f"G1 Z{constants.INSERTION_HEIGHT:.3f} F{constants.WORKING_SPEED} ; Bajar a cubeta")
    # Aquí tu comando de soltar punta (pin, solenoide, etc.)
    write(file, "G4 P300 ; Soltar punta")
    write(file, f"G1 Z{constants.BASE_HEIGHT:.3f} F{constants.WORKING_SPEED} ; Subir")

def tip_fixing(file, tip_index: int) -> None:
    tip_x = constants.TIP_BOX_START_X + tip_index * constants.TIP_SPACING
    tip_y = constants.TIP_BOX_START_Y
    write(file, "; --- Tomar nueva punta ---")
    write(file, f"G0 X{tip_x:.3f} Y{tip_y:.3f} F{constants.TRAVEL_SPEED} ; Moverse sobre punta #{tip_index}")
    write(file, f"G1 Z{constants.TIP_CHANGE_HEIGHT:.3f} F{constants.WORKING_SPEED} ; Bajar a fijar punta")
    write(file, "G4 P500 ; Presionar punta")
    write(file, f"G1 Z{constants.BASE_HEIGHT:.3f} F{constants.WORKING_SPEED} ; Subir con punta")

def tip_change(file, tip_index: int) -> None:
    tip_release(file)
    tip_fixing(file, tip_index)

def get_sample(file, color: str) -> None:
    if color not in constants.COLOR_POSITIONS:
        raise ValueError(f"Color '{color}' no definido en COLOR_POSITIONS")
    pos = constants.COLOR_POSITIONS[color]
    write(file, f"; --- Tomar muestra: {color} ---")
    write(file, f"G0 X{pos[0]:.3f} Y{pos[1]:.3f} F{constants.TRAVEL_SPEED} ; Mover a pocillo {color}")
    write(file, f"G1 Z{constants.INSERTION_HEIGHT:.3f} F{constants.WORKING_SPEED} ; Bajar a muestra")
    pipette_press(file)
    write(file, f"G1 Z{constants.BASE_HEIGHT:.3f} F{constants.WORKING_SPEED} ; Subir con muestra")

def translate_coordinates(file, data: dict) -> None:
    tip_index = 0
    for color, points in data.items():
        write(file, f"\n; ========== COLOR: {color.upper()} ==========")
        tip_change(file, tip_index)
        tip_index += 1
        get_sample(file, color)
        for x, y in points:
            # Convertir coordenadas relativas del disco a mm reales
            real_x = x * constants.DISC_SPACING
            real_y = y * constants.DISC_SPACING
            write(file, f"G0 X{real_x:.3f} Y{real_y:.3f} F{constants.TRAVEL_SPEED} ; Punto disco ({x},{y})")
            write(file, f"G1 Z{constants.INSERTION_HEIGHT:.3f} F{constants.WORKING_SPEED} ; Dispensar")
            pipette_press(file)
            write(file, f"G1 Z{constants.BASE_HEIGHT:.3f} F{constants.WORKING_SPEED} ; Subir")
            pipette_release(file)

    # Volver al origen al terminar
    write(file, "\n; --- Fin del programa ---")
    write(file, f"G0 Z{constants.BASE_HEIGHT:.3f} F{constants.TRAVEL_SPEED} ; Subir seguro")
    write(file, "G0 X0.000 Y0.000 F{constants.TRAVEL_SPEED} ; Volver al origen")
    write(file, "M2 ; Fin del programa")

def main() -> None:
    with open("coordinates.json", "r") as f:
        data = json.load(f)

    with open(OUTPUT_FILE, "w") as file:
        config(file)
        translate_coordinates(file, data)

    print(f"GCode generado: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()