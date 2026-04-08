from constants import write

def pipette_press(file) -> None:
    # Aquí va tu lógica de actuador (servo, solenoide, etc.)
    # Por ahora usa un dwell como placeholder
    write(file, "G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)")

def pipette_release(file) -> None:
    write(file, "G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)")