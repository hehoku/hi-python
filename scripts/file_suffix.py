# text.txt


def get_suffix(filename, has_dot=False):
    pos = filename.rfind(".")
    if 0 < pos < len(filename) - 1:
        index = pos + 1
        if has_dot:
            index = pos
        return filename[index:]
    else:
        return ""


if __name__ == "__main__":
    print(get_suffix("text.txt", True))
    print(get_suffix("text.txt", False))
