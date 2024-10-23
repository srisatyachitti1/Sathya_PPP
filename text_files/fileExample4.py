try:
    with open("../guido_bio.txt") as fobj:
        text=fobj.read()
except FileNotFoundError:
    text = None
print(text)
