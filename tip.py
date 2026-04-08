from constants import *

def tip_release() -> list:
    """
    Handles the GCode command to release the current tip

    Args:
        file (file): route to the file where the GCode will be written
    """
    GCODE = []
    GCODE.append("; --- Soltar punta ---")
    GCODE.append(f"G0 X{BIN_X:.3f} Y{BIN_Y:.3f} F{TRAVEL_SPEED} ; Mover a cubeta")
    GCODE.append(f"G1 Z{TIP_CHANGE_HEIGHT:.3f} F{WORKING_SPEED} ; Bajar a cubeta")
    
    #TODO Aquí va el comando de soltar punta
    
    return GCODE
    
def tip_fixing(tip_index: int) -> list:
    """
    Handles the GCode command to fix a new tip

    Args:
        file (file): route to the file where the GCode will be written
        tip_index (int): index of the tip to be fixed
    """
    GCODE = []
    
    tip_x = TIP_BOX_START_X + tip_index * TIP_SPACING
    tip_y = TIP_BOX_START_Y
    
    GCODE.append("; --- Tomar nueva punta ---")
    GCODE.append(f"G0 X{tip_x:.3f} Y{tip_y:.3f} F{TRAVEL_SPEED} ; Moverse sobre punta #{tip_index}")
    GCODE.append(f"G1 Z{TIP_CHANGE_HEIGHT:.3f} F{WORKING_SPEED} ; Bajar a fijar punta")
    GCODE.append("G4 P500 ; Presionar punta")
    GCODE.append(f"G1 Z{BASE_HEIGHT:.3f} F{WORKING_SPEED} ; Subir con punta")
    
    return GCODE

def tip_change(tip_index: int) -> list:
    """
    Handles the tip release and fixing

    Args:
        file (file): route to the file where the GCode will be written
        tip_index (int): index of the tip to be changed
    """
    
    GCODE = []
    GCODE.extend(tip_release())
    GCODE.extend(tip_fixing(tip_index))
    
    return GCODE