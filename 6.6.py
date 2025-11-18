hours = int(input('Enter parking hours: '))
if hours >= 1 and hours <= 2:
    print(f'For {hours} hours of parking you have to pay 5€')
elif hours >= 3 and hours <= 6:
    print(f'For {hours} hours of parking you have to pay 15€')
elif hours > 6:
    print(f'For {hours} hours of parking you have to pay 20€')