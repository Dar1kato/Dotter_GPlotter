from constants import write

def pipette_press() -> list:
    """
    Handles the pressing of the pipette button

    Args:
        file (file): route to the file where the GCode will be written
    """
    
    GCODE = []
    
    #TODO Aquí va tu lógica de actuador (servo, solenoide, etc.)
    GCODE.append("G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)") #! Provisional, reemplaza con tu comando de dispensar
    
    return GCODE

def pipette_release() -> list:
    """
    Handles the release of the pipette button

    Args:
        file (file): route to the file where the GCode will be written
    """
    GCODE = []
    
    #TODO Aquí va tu lógica de actuador para soltar (servo, solenoide, etc.)
    GCODE.append("G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)") #! Provisional, reemplaza con tu comando de soltar
    return GCODE