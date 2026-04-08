#######
# Speeds
#######
TRAVEL_SPEED   = 3000  
WORKING_SPEED  = 500

#######
# Heights
#######
BASE_HEIGHT       =  10.0  
INSERTION_HEIGHT  =  -5.0 
TIP_CHANGE_HEIGHT = -12.0  
SAMPLE_HEIGHT = -5.0

#######
# Tip box position and spacing
#######
TIP_BOX_START_X =  50.0   # medir con jogging
TIP_BOX_START_Y =   0.0
TIP_SPACING     =   9.0   # separación entre puntas en el rack (mm)

#######
# Trash bin position
#######
BIN_X = 100.0   # medir con jogging
BIN_Y =   0.0

#TODO Coordenadas de cada color — medir con jogging
#TODO El origen [0,0] es el centro del disco Petri

#######
# Color positions
#######
COLOR_POSITIONS = {
    "red":    (-80.0,   0.0),
    "blue":   (-80.0,  15.0),
    "green":  (-80.0,  30.0),
    "yellow": (-80.0,  45.0),
    "purple": (-80.0,  60.0),
}

#######
# Speeds
#######
DISC_SPACING = 5.0   

def write(file, line: str) -> None:
    file.write(line + "\n")