x = int(input("please enter a int number x: "))
y = int(input("please enter a int number y: "))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


gcd_result = gcd(x, y)
lcm_result = lcm(x, y)

print(f"gcd {gcd_result} lcm {lcm_result}")
