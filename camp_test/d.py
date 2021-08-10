from PIL import Image

path = input()
path = path+".png"

img = Image.open(path)
data = img.load()
w, h = img.size

position = []
for x in range(w):
    for y in range(h):
        color = data[x, y]
        if color != (0, 0, 0):
            position = x, y
            break

print(position)