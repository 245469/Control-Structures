###
# Checks if the entered name is a Polish female name
# (most Polish female names end with "a")
#
name = input("Enter name: ")

if name.endswith("a"):
    print(f'{name} -- Polish female name')
else:
    print(f'{name} is not a typical Polish female name')