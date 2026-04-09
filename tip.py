from constants import *

def tip_release() -> list:
    """
    Generates the gcode for tip releasing

    Returns:
        list: list containing gcode
    """
    GCODE: list = []
    
    GCODE.append(f"G0 X{BIN_X:.3f} Y{BIN_Y:.3f} F{TRAVEL_SPEED} ; Move to bin")
    GCODE.append(f"G1 Z{TIP_CHANGE_HEIGHT:.3f} F{WORKING_SPEED} ; Move to bin height")
    
    #TODO Tip release command here
    
    return GCODE
    
def tip_fixing(tip_index: int) -> list:
    """
    Generates the gcode for tip fixing

    Args:
        tip_index (int): position index of the tip to be fixed

    Returns:
        list: list containing gcode
    """
    GCODE: list = []
    
    tip_x = TIP_BOX_START_X + tip_index * TIP_SPACING
    tip_y = TIP_BOX_START_Y
    
    GCODE.append(f"G0 X{tip_x:.3f} Y{tip_y:.3f} F{TRAVEL_SPEED} ; Move over tip #{tip_index}")
    GCODE.append(f"G1 Z{TIP_CHANGE_HEIGHT:.3f} F{WORKING_SPEED} ; Move to tip fixing height")
    GCODE.append("G4 P500 ; Press tip")
    GCODE.append(f"G1 Z{BASE_HEIGHT:.3f} F{WORKING_SPEED} ; Move up with tip")
    
    return GCODE

def tip_change(tip_index: int) -> list:
    """
    Generates the gcode for tip changing

    Args:
        tip_index (int): position index of the tip to be changed

    Returns:
        list: list containing gcode
    """
    GCODE: list = []
    
    GCODE.append(f"\n; --- Changing to tip #{tip_index} ---")
    GCODE.extend(tip_release())
    GCODE.extend(tip_fixing(tip_index))
    
    return GCODE