import random


def gen_password(length):
    all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    for _ in range(length):
        index = random.randint(0, len(all_chars) - 1)
        password += all_chars[index]
    return password


if __name__ == "__main__":
    length = int(input("请输入密码长度："))
    print(gen_password(length))
