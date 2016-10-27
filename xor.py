from PIL import Image
from PIL import Imagechops

im1 = Image.open("A.png")

newimage = Imagechops.invert(im1)
newimage.save("new.png")
