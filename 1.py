from pathlib import Path

path = Path("/home/digitcrom/Desktop/Miniproject/MaktabsharifMiniProject3/front/images")
new_path = Path("/home/digitcrom/Desktop/Miniproject/MaktabsharifMiniProject3/front/icons/icons.txt")

for file_path in sorted(path.glob("*.png")):
    print(file_path.name)


with open(new_path, "w"):
    for file_path in sorted(path.glob("*icon*.png")):
        with open(new_path, "a") as f:
            f.write(str(file_path) + "\n")
        # file_path.unlink()
