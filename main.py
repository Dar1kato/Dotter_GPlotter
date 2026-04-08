import constants
import json

def config():
    with open("export.gcode", "w") as file:
        file.write("G21 ; Set units to millimeters\n")
        file.write("G17 ; Select XY plane\n")
        file.write("G90 ; Use absolute coordinates\n")
        file.write("G94 ; Set feed rate mode to units per minute\n")
        file.write("G28 ; Home all axes\n")
        
def readCoordinates() -> None:
    with open("coordinates.json", "r") as file:
        data = json.load(file)
        
        for color in data:
            for x, y in data[color]:
                print(f"Color: {color}, X: {x}, Y: {y}")

def main() -> None:
    readCoordinates()
    
    
if __name__ == "__main__":
    main()