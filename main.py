from constants import *
from pipette import pipette_press, pipette_release
from tip import tip_change
from sample import get_sample

def config() -> list:
    """
    Generates the basic config gcode strings for every file

    Returns:
        list: list containing gcode
    """
    GCODE: list = ["G21 ; Unidades en milímetros", "G17 ; Plano XY", "G90 ; Coordenadas absolutas",
                   "G94 ; Feed rate en unidades/minuto", "G28 ; Homing",
                   f"G0 Z{BASE_HEIGHT:.3f} F{TRAVEL_SPEED} ; Subir a altura segura"]

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
    tip_index: int = 0          # Index for tip changes
    
    for color, points in data.items():
        gcode_local.append(f"\n; ========== COLOR: {color.upper()} ==========")
        
        # Handles each point movement and insertion, adds its gcode to the current list
        for x, y in points:
            
            # Tip change logic, happens once per point
            gcode_local.extend(tip_change(tip_index)) 
            tip_index += 1
        
            # Sample loading logic, happens once per point
            gcode_local.extend(get_sample(color))
            
            real_x = x * DISC_SPACING
            real_y = y * DISC_SPACING
            
            gcode_local.append(f"G0 X{real_x:.3f} Y{real_y:.3f} F{TRAVEL_SPEED}")
            gcode_local.append(f"G1 Z{INSERTION_HEIGHT:.3f} F{WORKING_SPEED}")
            
            # Pipette press logic
            gcode_local.extend(pipette_press()) 
            
            gcode_local.append(f"G1 Z{BASE_HEIGHT:.3f} F{WORKING_SPEED}")
            
            # Pipette release logic
            gcode_local.extend(pipette_release()) 

    # Program end logic
    gcode_local.append(f"\n; --- Fin del programa ---")
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
