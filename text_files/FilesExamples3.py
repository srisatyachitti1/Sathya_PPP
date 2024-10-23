try:
    with open("../not_exist_file.txt") as fobj:
        text=fobj.read()
except FileNotFoundError:
    text = None
print(text)
