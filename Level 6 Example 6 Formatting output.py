#Program name: Level 6 Example 6 Formatting output
#prints radioactive elements and their half lives in neatly lined up columns   

element1 = "Einsteinium, Es"
atomicNumber1 = 99
halfLife1 = 471.65

element2 = "Mendelevium, Md"
atomicNumber2 = 101
halfLife2 = 51.5

#print heading
print("{:<20}{:>18}{:>25}".format("Element","Atomic Number","Half Life (Days)"))
#print data
print("{:<20}{:>12d}{:>25.2f}".format(element1,atomicNumber1,halfLife1))
print("{:<20}{:>12d}{:>25.2f}".format(element2,atomicNumber2,halfLife2))
