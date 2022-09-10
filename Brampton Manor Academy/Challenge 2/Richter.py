def richter(scaleTuple):
    print(f'{"Richter":<16} {"Joules":<32} TNT')
    for scale in scaleTuple:
        energy = 10**((1.5*scale)+4.8)
        oneTonneTNT = 4.184 * 10**9
        tnt = energy / oneTonneTNT
        print(f"{scale:<16} {energy:<32} {tnt}")

def richterValueInput():
    richterValue = float(input("Enter a Richter scale value: "))
    print(f"Richter value {richterValue}")
    return richterValue

def energyCalculation(richterValue):
    energy = 10**((1.5*richterValue)+4.8)
    return energy

def tntCalculation(richterValue):
    energy = 10**((1.5*richterValue)+4.8)
    oneTonneTNT = 4.184 * 10**9
    tnt = energy / oneTonneTNT
    return tnt

if __name__ == "__main__":
    scaleTuple = (1,5,9.1,9.3,9.5)
    richter(scaleTuple)
    richterValue = richterValueInput()
    energy = energyCalculation(richterValue)
    tnt = tntCalculation(richterValue)
    print(f"Equivalence in joules: {energy}")
    print(f"Equivalence in tonnes of TNT: {tnt}")
