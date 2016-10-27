from PIL import Image
from PIL import ImageChops

im1 = Image.open("A.png")
im2 = Image.open("C.png")

newimage = im1
newimage.save("new.png")
