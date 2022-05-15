import os


def getAllCogs():
    paths, cogs = [], []

    for root, subdirs, files in os.walk("src/cogs"):
        if "__pycache__" in subdirs:
            subdirs.remove("__pycache__")

        paths += [os.path.join(root, file) for file in files]
    for i, j in enumerate(paths):
        paths[i] = j.split("/")
        paths[i] = j.split("\\")
        paths[i].remove("src/cogs")
        paths[i][-1] = paths[i][-1][:-3]
        path = "src.cogs"

        for n, m in enumerate(paths[i]):
            path += f".{m}"

        cogs.append(path)

    return cogs
