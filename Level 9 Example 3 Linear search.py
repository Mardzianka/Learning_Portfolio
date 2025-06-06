#Program name: Level 9 Example 3 Linear search
fish = ["parrotfish", "grouper", "boxfish", "damselfish",\
        "snapper", "ray"]

print("List of fish to be searched:",fish)
found = False
index = 0
searchItem = input("Enter a fish to look for: ")

while not found and index < len(fish):
    print(fish[index])
    if fish[index] == searchItem:
        found = True
    else:
        index = index + 1

if found:
    print(searchItem, "was found at position", index)

else:
    print("Item not found")
