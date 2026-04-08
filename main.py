import constants
import json

def config() -> None:
    with open("export.gcode", "w") as file:
        file.write("G21 ; Set units to millimeters\n")
        file.write("G17 ; Select XY plane\n")
        file.write("G90 ; Use absolute coordinates\n")
        file.write("G94 ; Set feed rate mode to units per minute\n")
        file.write("G28 ; Home all axes\n")
        
def pipettePress() -> None:
    print("Dispensing liquid...")
    
def pipetteRelease() -> None:
    print("Releasing pipette...")
    
    
    
def tipRelease() -> None:
    print(f"G0 X{constants.BIN_X:.3f} Y{constants.BIN_Y:.3f} F{constants.TRAVEL_SPEED} ; Move to bin location")
    print("Releasing tip...")
    
def tipFixing() -> None:
    print(f"G0 X{constants.TIP_BOX_START_X:.3f} Y{constants.TIP_BOX_START_Y:.3f} F{constants.TRAVEL_SPEED} ; Move to tip box location")
    print(f"G1 Z{constants.TIP_CHANGE_HEIGHT:.3f} F{constants.WORKING_SPEED} ; Lower to tip change height")
    print("Fixing new tip...")
    print(f"G1 Z{constants.BASE_HEIGHT:.3f} F{constants.WORKING_SPEED} ; Raise to base height")
        
def tipChange() -> None:
    tipRelease()
    tipChange()
    

        
def translateCoordinate() -> None:
    with open("coordinates.json", "r") as file:
        data = json.load(file)
        
        for color in data:
            for x, y in data[color]:
                print(f"G0 X{x:.3f} Y{y:.3f} F{constants.TRAVEL_SPEED} ; Move to ({x:.3f}, {y:.3f})")
                print(f"G1 Z{constants.INSERTION_HEIGHT:.3f} F{constants.WORKING_SPEED} ; Lower to insertion height")
                pipettePress()
                print(f"G1 Z{constants.BASE_HEIGHT:.3f} F{constants.WORKING_SPEED} ; Raise to base height")
                pipetteRelease()
                print(f"\n")
                tipRelease()
                print(f"\n")
                tipChange()
                

def main() -> None:
    translateCoordinate()
    
    
if __name__ == "__main__":
    main()