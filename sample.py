from constants import *
from pipette import pipette_suction, pipette_release

def get_sample(color: str) -> list:
    """
    Generates the gcode for taking a sample of a given color

    Args:
        color (str): color of the sample to be taken

    Returns:
        list: list containing gcode

    Raises:
        ValueError: the color described is not defined in COLOR_POSITIONS (constants.py)
    """
    GCODE: list = []
    
    # Raise error if color is not defined in COLOR_POSITIONS
    if color not in COLOR_POSITIONS:
        raise ValueError(f"Color '{color}' not defined in COLOR_POSITIONS")
    
    pos = COLOR_POSITIONS[color]
    
    GCODE.append(f"; --- Taking sample: {color} ---")
    GCODE.append(f"G0 X{pos[0]:.3f} Y{pos[1]:.3f} F{TRAVEL_SPEED} ; Move to well {color}")
    GCODE.append(f"G1 Z{SAMPLE_HEIGHT:.3f} F{WORKING_SPEED} ; Move to sample height")
    GCODE.extend(pipette_suction())
    GCODE.append(f"G1 Z{BASE_HEIGHT:.3f} F{WORKING_SPEED} ; Move up with sample")
    
    return GCODE