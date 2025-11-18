human_years = int(input("Enter the dog's age in human years: "))
if human_years <= 2:
    print("The dog's age in dog's years is 10.5 years")
elif human_years > 2:
    dog_age = 10.5 + (human_years - 2) * 4
    print(f"The dog's age in dog's years is {dog_age} years")