# Pierwsze dwadzieścia wyrazów ciągu Fibonacciego
fib1 = 0
fib2 = 1
print(fib1, fib2, end=' ')
count = 2
while count < 20:
    fib_next = fib1 + fib2
    print(fib_next, end=' ')
    fib1 = fib2  # przesuwamy poprzednie liczby
    fib2 = fib_next
    count += 1