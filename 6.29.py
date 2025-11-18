N = int(input("Enter the number of prime numbers to find: "))

prime_count = 0  # licznik znalezionych liczb pierwszych
num = 2          # liczba, którą sprawdzamy

print("Prime numbers:", end=' ')

while prime_count < N:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')
        prime_count += 1
    num += 1