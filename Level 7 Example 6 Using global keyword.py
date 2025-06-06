#Program name: Level 7 Example 6 Using global keyword
#defining a global keyword variable

def defineGlobalName():
    global musketeerName
    musketeerName = "Aramis"
#end function

defineGlobalName()
print("Musketeer: " + musketeerName)

