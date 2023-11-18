import PIL
from PIL import Image
from PIL import ImageOps
import sys


def is_valid():
    if not len(sys.argv) == 2:
        input_argv_modify = sys.argv[1].lower().split(".")[1]
        output_argv_modify = sys.argv[2].lower().split(".")[1]
        if input_argv_modify not in ["jpg", "jpeg", "png"]:
            sys.exit(1)
        if output_argv_modify not in ["jpg", "jpeg", "png"]:
            sys.exit(1)
        if not input_argv_modify == output_argv_modify:
            sys.exit(1)
        return
    sys.exit(1)

is_valid()

shirt = Image.open("shirt.png")
size = shirt.size

try:
    photo = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit()

resized_photo = ImageOps.fit(photo, size)

resized_photo.paste(shirt, shirt)

resized_photo.save(fp=sys.argv[2])