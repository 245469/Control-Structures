print("SURVEY")
q1 = input("Are you interested in computer science? (y/n): ")
q2 = input("Do you like playing computer games? (y/n): ")
q3 = input("Do you have an Instagram account? (y/n): ")

# Zamiana odpowiedzi na wartości logiczne (True/False)
interested = q1 == 'y'
games = q2 == 'y'
instagram = q3 == 'y'

print("\nSURVEY RESULTS")
print("Interested in computer science:", "Yes" if interested else "No")
print("Playing computer games:", "Yes" if games else "No")
print("Has an Instagram account:", "Yes" if instagram else "No")