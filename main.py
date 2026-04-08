from constants import *
from pipette import pipette_press, pipette_release
from tip import tip_change
from sample import get_sample
import json

OUTPUT_FILE = "export.gcode"
GCODE = []

# main.py modificado

def config() -> list:
    # Ahora devuelve una lista en lugar de modificar una global
    c = []
    c.append("G21 ; Unidades en milímetros")
    c.append("G17 ; Plano XY")
    c.append("G90 ; Coordenadas absolutas")
    c.append("G94 ; Feed rate en unidades/minuto")
    c.append("G28 ; Homing")
    c.append(f"G0 Z{BASE_HEIGHT:.3f} F{TRAVEL_SPEED} ; Subir a altura segura")
    return c

def translate_coordinates(data: dict) -> list:
    gcode_local: list = []
    tip_index: int = 0
    
    for color, points in data.items():
        gcode_local.append(f"\n; ========== COLOR: {color.upper()} ==========")
        
        # IMPORTANTE: Extendemos la lista con lo que devuelven las funciones
        gcode_local.extend(tip_change(tip_index)) 
        tip_index += 1
        
        # Asegúrate de que get_sample también devuelva una lista
        gcode_local.extend(get_sample(color))
        
        for x, y in points:
            real_x = x * DISC_SPACING
            real_y = y * DISC_SPACING
            gcode_local.append(f"G0 X{real_x:.3f} Y{real_y:.3f} F{TRAVEL_SPEED}")
            gcode_local.append(f"G1 Z{INSERTION_HEIGHT:.3f} F{WORKING_SPEED}")
            gcode_local.extend(pipette_press()) # Devolver lista
            gcode_local.append(f"G1 Z{BASE_HEIGHT:.3f} F{WORKING_SPEED}")
            gcode_local.extend(pipette_release()) # Devolver lista

    # Finalización
    gcode_local.append(f"\n; --- Fin del programa ---")
    gcode_local.append("M2")
    return gcode_local

def main(data) -> str:
    # Esta es la función que llamará Flask
    resultado = []
    resultado.extend(config())
    resultado.extend(translate_coordinates(data))
    
    # Unimos todo en un solo bloque de texto
    return "\n".join(resultado)
