from pathlib import Path
import re
path = Path('C:/Users/bcz/Desktop/MaktabSherif/week12/miniproject/MaktabsharifMiniProject3-1/front/images')
image_list=[]
icon_list=[]
for images in path.glob("*"):
    match=re.findall(r"([^\/\\]+)$",str(images))
    match_1="".join(match)
    image_list.append(match_1)
    icon_list.append("".join(re.findall(r"icon-(.*?)\.(png)",str(match_1))))
    image_list.sort()
print(image_list)
print(icon_list)

