###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = True # False - switch off, True - switch on
light_switch2 = False
bulbs_on = 0
if light_switch1:
    bulbs_on += 1 # switch 1 lights 1 bulb
if light_switch2:
    bulbs_on += 2  # switch 2 lights 2 bulbs
print(f'{bulbs_on} bulbs are illuminating the house')