from pathlib import Path


png_path = Path.cwd().joinpath("front", "images")

for file_path in sorted(png_path.glob("*.png")):
    print(file_path.name)


icons = ""
for icon_path in png_path.glob("*icon*.png"):
    icons += f"{icon_path}\n"
    # Path.unlink(icon_path)

Path('Icons.txt').write_text(icons)

