from constants import *
from pipette import pipette_press, pipette_release

def get_sample(file, color: str) -> None:
    """
    Handles the sample logic

    Args:
        file (file): route to the file where the GCode will be written
        color (str): color of the sample to be taken
        
    Raises:
        ValueError: the color described is not defined in COLOR_POSITIONS (constants.py)
    """
    if color not in COLOR_POSITIONS:
        raise ValueError(f"Color '{color}' no definido en COLOR_POSITIONS")
    
    pos = COLOR_POSITIONS[color]
    
    write(file, f"; --- Tomar muestra: {color} ---")
    write(file, f"G0 X{pos[0]:.3f} Y{pos[1]:.3f} F{TRAVEL_SPEED} ; Mover a pocillo {color}")
    write(file, f"G1 Z{SAMPLE_HEIGHT:.3f} F{WORKING_SPEED} ; Bajar a muestra")
    pipette_press(file)
    pipette_release(file)
    write(file, f"G1 Z{BASE_HEIGHT:.3f} F{WORKING_SPEED} ; Subir con muestra")