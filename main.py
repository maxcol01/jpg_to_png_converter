from pathlib import Path
import shutil as sh
from PIL import Image, ImageFilter # type: ignore

cd = Path(".")
folder_path = cd / "images"

for item in cd.iterdir():
    if item.suffix == ".jpg" and item.stem != "astro":
        sh.move(item, folder_path)

images_path = cd / "Pokedex"
img = Image.open(images_path/ "Pikatchu.jpg")

#print(img)
#print(img.format)
#print(img.size)
#print(img.mode)


box = (100, 100,  400, 400)
img.crop(box)
#img.show()

filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save(images_path / "pikatchu_blurred.jpg")

converted_image = img.convert("L")
converted_image.save(images_path / "Pikatchu_converted.jpg")

astronaut_image = Image.open(cd / "astro.jpg")
print(astronaut_image.size)
new_astro = astronaut_image.resize((400, 400))
print(new_astro.size)
new_astro.save(cd /"new_astro.jpg")
new_astro.show()