from PIL import Image # type: ignore
from pathlib import Path
import sys

def jpg_png_converter(original_folder, target_folder):
    folder = Path(original_folder)
    new_folder = Path(target_folder)
    new_folder.mkdir(parents=True, exist_ok=True) # create a folder it doesn't exist
    try:
        for file in folder.iterdir():
            if file.suffix == ".jpg":
                img = Image.open(file)
                img.save(new_folder / f"{file.stem}.png")
        print("Pictures converted successfully")
    except:
        print("The orignal directory does not exist")



try:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]    

    jpg_png_converter(original_folder=arg1, target_folder=arg2)
except:
    print("Provide two arguments: an orginal folder and a target folder")
