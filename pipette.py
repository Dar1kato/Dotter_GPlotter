from constants import *

def pipette_release() -> list:
    """
    Handles the release of the pipette button

    Args:
        file (file): route to the file where the GCode will be written
    """
    GCODE: list = []
    
    GCODE.append("M67 E0 Q0.65")
    GCODE.append(f"G1 Z{BASE_HEIGHT:.3f} F{WORKING_SPEED}")
    GCODE.append("M67 E0 Q0.0")
    
    return GCODE

def pipette_suction() -> list:
    """
    Handles the suction of the pipette button

    Args:
        file (file): route to the file where the GCode will be written
    """
    GCODE: list = []
    
    GCODE.append("M67 E0 Q0.55")
    GCODE.append("M67 E0 Q0.0")
    
    return GCODE