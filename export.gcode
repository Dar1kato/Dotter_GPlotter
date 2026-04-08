G21 ; Unidades en milímetros
G17 ; Plano XY
G90 ; Coordenadas absolutas
G94 ; Feed rate en unidades/minuto
G28 ; Homing
G0 Z10.000 F3000 ; Subir a altura segura

; ========== COLOR: RED ==========
; --- Soltar punta ---
G0 X100.000 Y0.000 F3000 ; Mover a cubeta
G1 Z-5.000 F500 ; Bajar a cubeta
G1 Z10.000 F500 ; Subir
; --- Tomar nueva punta ---
G0 X50.000 Y0.000 F3000 ; Moverse sobre punta #0
G1 Z-12.000 F500 ; Bajar a fijar punta
G4 P500 ; Presionar punta
G1 Z10.000 F500 ; Subir con punta
; --- Tomar muestra: red ---
G0 X-80.000 Y0.000 F3000 ; Mover a pocillo red
G1 Z-5.000 F500 ; Bajar a muestra
G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)
G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)
G1 Z10.000 F500 ; Subir con muestra
G0 X0.000 Y-5.000 F3000 ; Punto disco (0,-1)
G1 Z-5.000 F500 ; Dispensar
G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)
G1 Z10.000 F500 ; Subir
G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)
G0 X5.000 Y-10.000 F3000 ; Punto disco (1,-2)
G1 Z-5.000 F500 ; Dispensar
G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)
G1 Z10.000 F500 ; Subir
G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)
G0 X10.000 Y-5.000 F3000 ; Punto disco (2,-1)
G1 Z-5.000 F500 ; Dispensar
G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)
G1 Z10.000 F500 ; Subir
G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)
G0 X10.000 Y0.000 F3000 ; Punto disco (2,0)
G1 Z-5.000 F500 ; Dispensar
G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)
G1 Z10.000 F500 ; Subir
G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)
G0 X5.000 Y5.000 F3000 ; Punto disco (1,1)
G1 Z-5.000 F500 ; Dispensar
G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)
G1 Z10.000 F500 ; Subir
G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)
G0 X0.000 Y10.000 F3000 ; Punto disco (0,2)
G1 Z-5.000 F500 ; Dispensar
G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)
G1 Z10.000 F500 ; Subir
G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)
G0 X-5.000 Y5.000 F3000 ; Punto disco (-1,1)
G1 Z-5.000 F500 ; Dispensar
G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)
G1 Z10.000 F500 ; Subir
G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)
G0 X-10.000 Y0.000 F3000 ; Punto disco (-2,0)
G1 Z-5.000 F500 ; Dispensar
G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)
G1 Z10.000 F500 ; Subir
G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)
G0 X-10.000 Y-5.000 F3000 ; Punto disco (-2,-1)
G1 Z-5.000 F500 ; Dispensar
G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)
G1 Z10.000 F500 ; Subir
G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)
G0 X-5.000 Y-10.000 F3000 ; Punto disco (-1,-2)
G1 Z-5.000 F500 ; Dispensar
G4 P500 ; Esperar 500ms (reemplaza con tu comando de dispensar)
G1 Z10.000 F500 ; Subir
G4 P300 ; Esperar 300ms (reemplaza con tu comando de soltar)

; --- Fin del programa ---
G0 Z10.000 F3000 ; Subir seguro
G0 X0.000 Y0.000 F{TRAVEL_SPEED} ; Volver al origen
M2 ; Fin del programa
