def richter(scaleList):
    for i in range (0,len(scaleList)):
        scale = scaleList[i]
        energy = 10**((1.5*scale)+4.8)
        oneTonneTNT = 4.184 * 10**9
        TNT = energy / oneTonneTNT
        print("Richter",scale,"-->",energy,"JOULES")
        print("Richter",scale,"-->",TNT,"TNT")

def richterValueOutput(richterValue):
    print("Richter value:",richterValue)

def equivalence(richterValue):
    energy = 10**((1.5*richterValue)+4.8)
    oneTonneTNT = 4.184 * 10**9
    TNT = energy / oneTonneTNT
    print("Equivalence in joules:",energy)
    print("Equivalence in tonnes of TNT:",TNT)


scaleList = (1,5,9.1,9.3,9.5)
richter(scaleList)
richterValue = float(input("Enter a Richter scale value: "))
richterValueOutput(richterValue)
equivalence(richterValue)
