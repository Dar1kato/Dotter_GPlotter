import json
import sys
from pathlib import Path


TRAVEL_SPEED   = 300  

COLOR_DICT = {
    "black":    "S1",
    "red":      "S25",
    "blue":     "S75",
    "green":    "S50",
    "yellow":   "S100",
    "purple":   "S150",
    "orange":   "S175",
    "white":    "S225"
}

REPEAT_COUNT = 3

def config() -> list:
    """
    Generates the basic config gcode strings for every file
    Returns:
        list: list containing gcode
    """
    gcode: list = [
        "G21 ; Units as mm",
        "G17 ; XY Plane",
        "G90 ; Absolute Coordinates",
        "G94 ; Feed rate in units/minute",
    ]
    return gcode


def translate_coordinates(data: dict) -> list:
    """
    Generates gcode from given coordinates, repeated REPEAT_COUNT times
    Args:
        data (dict): coordinates dictionary
    Returns:
        list: list containing gcode
    """
    gcode_local: list = []

    for i in range(REPEAT_COUNT):
        gcode_local.append(f"\n; --- Repeticion {i + 1} de {REPEAT_COUNT} ---")

        for color, points in data.items():
            if color not in COLOR_DICT:
                print(f"[WARNING] Color '{color}' no encontrado en COLOR_DICT, omitiendo.")
                continue
            
            for i in range(len(points)):
                point = points[i]
                
                if len(point) != 2:
                    print(f"[WARNING] Punto inválido {point} para color '{color}', omitiendo.")
                    continue
                x, y = point
                
                if i == 0:
                    gcode_local.append(f"G0 X{-x:.3f} Y{-y:.3f} F{TRAVEL_SPEED}")
                    gcode_local.append(f"M3 {COLOR_DICT[color]} ; Color: {color}")
                
                else:
                    gcode_local.append(f"G0 X{-x:.3f} Y{-y:.3f} F{TRAVEL_SPEED}")
            
            gcode_local.append("M3 S1 ; Apagar color")

    # Program end
    gcode_local.append("\n; --- Fin del programa ---")
    gcode_local.append("M3 S1")
    gcode_local.append("M2")

    return gcode_local


def main(data: dict) -> str:
    """
    Generates full gcode string from coordinates data
    Args:
        data (dict): coordinates dictionary
    Returns:
        str: Generated gcode string
    """
    result: list = []
    result.extend(config())
    result.extend(translate_coordinates(data))
    return "\n".join(result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 main.py /ruta/al/archivo.json nombre_archivo_salida")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"[ERROR] Archivo no encontrado: {input_path}")
        sys.exit(1)

    if input_path.suffix.lower() != ".json":
        print(f"[ERROR] El archivo debe ser .json")
        sys.exit(1)

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"[ERROR] JSON inválido: {e}")
        sys.exit(1)

    print(f"Generando GCode ({REPEAT_COUNT} repeticiones)...")
    gcode = main(data)

    downloads = Path.home() / "Downloads"
    downloads.mkdir(exist_ok=True)
    output_path = downloads / (input_path.stem + ".gcode")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(gcode)

    print(f"✓ GCode guardado en: {output_path}")