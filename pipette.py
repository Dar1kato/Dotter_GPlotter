
def pipette_press() -> list:
    """
    Handles the pressing of the pipette button
    """
    GCODE: list = []
    
    #TODO Actuator logic here
    GCODE.append("G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)") #! Provisional, replace with dispensing command
    
    return GCODE

def pipette_release() -> list:
    """
    Handles the release of the pipette button


    """
    GCODE: list = []
    
    #TODO Actuator logic here
    GCODE.append("G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)") #! Provisional, replace with releasing command
    
    return GCODE