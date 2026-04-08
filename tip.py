from constants import *

def tip_release(file) -> None:
    write(file, "; --- Soltar punta ---")
    write(file, f"G0 X{BIN_X:.3f} Y{BIN_Y:.3f} F{TRAVEL_SPEED} ; Mover a cubeta")
    write(file, f"G1 Z{INSERTION_HEIGHT:.3f} F{WORKING_SPEED} ; Bajar a cubeta")
    
    # Aquí tu comando de soltar punta (pin, solenoide, etc.)
    
    write(file, f"G1 Z{BASE_HEIGHT:.3f} F{WORKING_SPEED} ; Subir")

def tip_fixing(file, tip_index: int) -> None:
    tip_x = TIP_BOX_START_X + tip_index * TIP_SPACING
    tip_y = TIP_BOX_START_Y
    write(file, "; --- Tomar nueva punta ---")
    write(file, f"G0 X{tip_x:.3f} Y{tip_y:.3f} F{TRAVEL_SPEED} ; Moverse sobre punta #{tip_index}")
    write(file, f"G1 Z{TIP_CHANGE_HEIGHT:.3f} F{WORKING_SPEED} ; Bajar a fijar punta")
    write(file, "G4 P500 ; Presionar punta")
    write(file, f"G1 Z{BASE_HEIGHT:.3f} F{WORKING_SPEED} ; Subir con punta")

def tip_change(file, tip_index: int) -> None:
    tip_release(file)
    tip_fixing(file, tip_index)