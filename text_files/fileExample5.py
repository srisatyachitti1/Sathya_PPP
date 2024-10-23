oceans = ["Pacific", "Atlantic", "Indian", "Southren", "Arctic"]

with open("../ocenas.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")