row = int(input("please enter row: "))

for i in range(1, row + 1):
    for j in range(0, i):
        print("*", end="")
    print()

print("-----")

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(" ", end="")
        else:
            print("*", end="")
    print()

print("-----")

for i in range(row):
    for _ in range(row - i - 1):
        print(" ", end="")
    for _ in range(2 * i + 1):
        print("*", end="")
    print()
