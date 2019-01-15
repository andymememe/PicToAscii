import PIL
from PIL import Image
import os

def converter(g):
    if g >= 230:
        return '@'
    elif g >= 200:
        return '#'
    elif g >= 180:
        return '8'
    elif g >= 160:
        return '&'
    elif g >= 130:
        return 'o'
    elif g >= 100:
        return ':'
    elif g >= 70:
        return '*'
    elif g >= 50:
        return '.'
    else:
        return ' '

lineSize = 240
for filename in os.listdir('./pic'):
    img = Image.open('./pic/' + filename).convert('L')
    w = img.size[0]
    h = img.size[1]

    if w > h:
        ds = lineSize / w
    else:
        ds = lineSize / h
    w = int(w * ds)
    h = int(h * ds)
        
    img = img.resize((w, h), PIL.Image.ANTIALIAS)
    pix = img.load()

    with open('./txt/' + filename + '.txt', 'w', encoding='utf-8') as f:
        for y in range(h):
            line = []
            for x in range(w):
                line.append(converter(pix[x, y]))
            f.write(''.join(line) + '\n')