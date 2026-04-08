from constants import *
from pipette import pipette_press, pipette_release

def get_sample(file, color: str) -> None:
    if color not in COLOR_POSITIONS:
        raise ValueError(f"Color '{color}' no definido en COLOR_POSITIONS")
    pos = COLOR_POSITIONS[color]
    write(file, f"; --- Tomar muestra: {color} ---")
    write(file, f"G0 X{pos[0]:.3f} Y{pos[1]:.3f} F{TRAVEL_SPEED} ; Mover a pocillo {color}")
    write(file, f"G1 Z{INSERTION_HEIGHT:.3f} F{WORKING_SPEED} ; Bajar a muestra")
    pipette_press(file)
    pipette_release(file)
    write(file, f"G1 Z{BASE_HEIGHT:.3f} F{WORKING_SPEED} ; Subir con muestra")