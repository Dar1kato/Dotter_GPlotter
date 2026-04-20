import time
from constants import *

def config() -> list:
    """
    Generates the basic config gcode strings for every file

    Returns:
        list: list containing gcode
    """
    GCODE: list = ["G21 ; Units as mm", "G17 ; XY Plane", "G90 ; Absolute Coordinates",
                   "G94 ; Feed rate in units/minute", "G28 ; Homing"]
    

    return GCODE


def translate_coordinates(data: dict) -> list:
    """
    Generates gcode from given coordinates

    Args:
        data (dict): coordinates dictionary

    Returns:
        list: list containing gcode
    """
    
    gcode_local: list = []      # Current gcode list
    
    start = time.time()
    while time.time() - start < TIME:
        
        for color, points in data.items():
            gcode_local.append(f"M3 {COLOR_DICT[color]} ; Color: {color}");

            for x, y in points:
                gcode_local.append(f"G0 X{x:.3f} Y{y:.3f} F{TRAVEL_SPEED}")
            

    # Program end logic
    gcode_local.append(f"\n; --- Fin del programa ---")
    gcode_local.append("M3 S0")
    gcode_local.append("G28 ; Home")
    gcode_local.append("M2")
    
    return gcode_local

def main(data: dict) -> str:
    """
    Flask script call

    Args:
        data (dict): coordinates dictionary

    Returns:
        str: Generated gcode string
    """
    result: list = []
    result.extend(config())
    result.extend(translate_coordinates(data))
    
    return "\n".join(result)
