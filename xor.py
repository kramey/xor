from PIL import Image
from PIL import ImageChops

im1 = Image.open("A.png")

newimage = ImageChops.invert(im1)
newimage.save("new.png")
