def rodsInput(rods):
    print("You input",rods,"rods")

def metersConvert(rods):
    meters = rods * 5.0292
    print("Meters:",meters)

def feetConvert(rods):
    feet = rods * 16.5
    print("Feet:",feet)

def milesConvert(rods):
    miles = rods * 0.003125
    print("Miles:",miles)

def furlongsConvert(rods):
    furlongs = rods * 0.025
    print("Furlongs:",furlongs)

def walkConvert(rods):
    timeMinutes = rods / 16.5333
    print("Minutes to walk",rods,"rods:",timeMinutes)

rods=float(input("Input rods: "))

rodsInput(rods)
metersConvert(rods)
feetConvert(rods)
milesConvert(rods)
furlongsConvert(rods)
walkConvert(rods)


