from constants import *
from pipette import pipette_press, pipette_release

def get_sample(color: str) -> list:
    """
    Handles the sample logic

    Args:
        file (file): route to the file where the GCode will be written
        color (str): color of the sample to be taken
        
    Raises:
        ValueError: the color described is not defined in COLOR_POSITIONS (constants.py)
    """
    GCODE = []
    
    if color not in COLOR_POSITIONS:
        raise ValueError(f"Color '{color}' no definido en COLOR_POSITIONS")
    
    pos = COLOR_POSITIONS[color]
    
    GCODE.append(f"; --- Tomar muestra: {color} ---")
    GCODE.append(f"G0 X{pos[0]:.3f} Y{pos[1]:.3f} F{TRAVEL_SPEED} ; Mover a pocillo {color}")
    GCODE.append(f"G1 Z{SAMPLE_HEIGHT:.3f} F{WORKING_SPEED} ; Bajar a muestra")
    GCODE.extend(pipette_press())
    GCODE.extend(pipette_release())
    GCODE.append(f"G1 Z{BASE_HEIGHT:.3f} F{WORKING_SPEED} ; Subir con muestra")
    
    return GCODE