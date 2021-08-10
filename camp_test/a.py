import numpy as np
from PIL import Image

path = input()
image_file = Image.open(path)
image = np.array(image_file)

print("Red: {}".format(image[0][0][0]))
print("Green: {}".format(image[0][0][1]))
print("Blue: {}".format(image[0][0][2]))