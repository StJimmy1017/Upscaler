from PIL import Image
import cv2
import numpy as np

def nninterp(source):
    width, height = source.size
    new_width = width * 2
    new_height = height * 2
    nintendo = Image.new('RGB', (new_width, new_height))
    for y in range(new_height):
        for x in range(new_width):
            original_x = int(x * 0.5)
            original_y = int(y * 0.5)
            original_x = min(original_x, source.width - 1)
            original_y = min(original_y, source.height - 1)
            color = source.getpixel((original_x, original_y))
            nintendo.putpixel((x, y), color)
    return nintendo

def txsal(source):
    width, height = source.size
    new_width = width * 2
    new_height = height * 2
    sally = Image.new('RGB', (new_width, new_height))
    for y in range(height):
        for x in range(width):
            color = source.getpixel((x, y))
            sally.putpixel((x * 2, y * 2), color)
            sally.putpixel((x * 2 + 1, y * 2), color)
            sally.putpixel((x * 2, y * 2 + 1), color)
            sally.putpixel((x * 2 + 1, y * 2 + 1), color)
    return sally

def area(source):
    width, height = source.size
    new_width = width * 2
    new_height = height * 2
    source = np.array(source)
    ariel = cv2.resize(source, dsize=(new_width, new_height), interpolation=cv2.INTER_AREA)
    return Image.fromarray(ariel)

def lanczos(source):
    width, height = source.size
    new_width = width * 2
    new_height = height * 2
    source = np.array(source)
    lance = cv2.resize(source, dsize=(new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
    return Image.fromarray(lance)

def cubic(source):
    width, height = source.size
    new_width = width * 2
    new_height = height * 2
    source = np.array(source)
    buick = cv2.resize(source, dsize=(new_width, new_height), interpolation=cv2.INTER_CUBIC)
    return Image.fromarray(buick)