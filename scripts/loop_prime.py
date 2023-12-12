from math import sqrt

num = int(input("please enter a number: "))

isPrime = True
for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
        isPrime = False
        break

if isPrime and num != 1:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")
