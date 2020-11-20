import PIL
from PIL import Image
import glob
image_list = []
for filename in glob.glob('./happy-face-image/*.png'): #assuming gif
    im= filename
    image_list.append(im)
    print(im)