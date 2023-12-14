str = "hello world"
print(str.center(50, "*"))
print(str.rjust(50, "*"))
print(str.ljust(50, "*"))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == "__main__":
    main()

items = dict(zip(["a", "b", "c"], [1, 2, 3]))
print(items)
