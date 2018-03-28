from random import random
from math import hypot
from PIL import Image
from PIL import ImageDraw

TRIALS=10**6
XMAX=500
YMAX=500

def main():
    help = 1
    inside = 0
    img = Image.new('RGB', (XMAX, YMAX), "white")
    draw = ImageDraw.Draw(img)
    for i in xrange(TRIALS):
        x = random()
        y = random()
        draw.point((int(x * XMAX), int(y * YMAX)), fill = "blue")
        if hypot( x, y) < 1:
            inside += 1
            draw.point((int(x * XMAX), int(y * YMAX)), fill = "red")
    img.save('pi.png')
    mypi = 4 * inside / TRIALS
    return mypi

if __name__ == '__main__':
    main()
