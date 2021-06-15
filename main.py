# importing the module
from PIL import Image
import os

# importing the image
im = Image.open("media/images/qwery.png")
print("The size of the image before conversion : ", end="")
print(os.path.getsize("media/images/qwery.png"))

# converting to jpg
rgb_im = im.convert("RGB")

# exporting the image
rgb_im.save("media/images/qwery.jpg")
print("The size of the image after conversion : ", end="")
print(os.path.getsize("media/images/qwery.jpg"))