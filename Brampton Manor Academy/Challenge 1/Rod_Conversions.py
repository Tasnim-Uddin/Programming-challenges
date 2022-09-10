def rodsInput():
    rods = float(input("Input rods: "))
    print(f"You input {rods} rods")
    return rods

def metersConvert(rods):
    return rods * 5.0292

def feetConvert(rods):
    return rods * 16.5

def milesConvert(rods):
    return rods * 0.003125

def furlongsConvert(rods):
    return rods * 0.025

def walkConvert(rods):
    return rods / 16.5333


if __name__ == "__main__":
    rods = rodsInput()
    print(f"Meters: {metersConvert(rods)}")
    print(f"Feet: {feetConvert(rods)}")
    print(f"Miles: {milesConvert(rods)}")
    print(f"Furlongs: {furlongsConvert(rods)}")
    print(f"Minutes to walk {rods} rods: {walkConvert(rods)}")

