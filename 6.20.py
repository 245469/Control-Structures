decimal = int(input("Enter decimal number: "))
number = decimal
binary = ""  # tu będziemy budować wynik
while number > 0:
    remainder = number % 2      # reszta z dzielenia przez 2
    binary = str(remainder) + binary  # dokładamy resztę na początek
    number = number // 2        # dzielimy liczbę całkowicie przez 2
print(f"{decimal}(10) = {binary}(2)")