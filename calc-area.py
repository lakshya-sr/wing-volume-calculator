from shapely.geometry import Polygon
import sys

logging = False
def log(msg):
    if logging:
        print(msg)

def import_airfoil(filename):
    with open(filename) as f:
        coords = []
        chord = 1
        reading_coords = False
        for line in f:
            match line:
                case "Airfoil surface,\n":
                    next(f)
                    reading_coords = True
                case ",\n":
                    if reading_coords:
                        reading_coords = False
                case _:
                    if reading_coords:
                        log(line)
                        coords.append(tuple(map(lambda x: float(x)/chord, line.split(","))))
                    elif line.startswith("Chord("):
                        log(line)
                        chord = float(line.split(",")[1])

        return coords        

airfoil_points = import_airfoil(sys.argv[1])
shape = Polygon(airfoil_points)
print(shape.area)
