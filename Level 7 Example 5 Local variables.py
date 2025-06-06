#Program name: Level 7 Example 5 Local variables
#demonstrates a local variable

def printLocalName():
#A local variable defined within the function takes precedence
  musketeerName = "Porthos" 
  print("Musketeer: " + musketeerName)

musketeerName = "Athos"
printLocalName()

