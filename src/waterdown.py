import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from imageio import imread

###################### Basic image functions ##########################

def read_image(img_name):
    """
    Read an image file (.png) into a numpy array in which each entry is
    a row of pixels (i.e. ``len(img)`` is the image height in px.
    """
    data_dir = Path('..') / 'img'
    img = imread(data_dir / img_name)
    return img

def show_image(img):
    """
    Show an image using a provided pixel row array.
    """
    plt.imshow(img)
    plt.show()
    return

def show_original(img_name):
    """
    Debugging/development: produce and display an original image
    """
    img = read_image(img_name)
    show_image(img)
    return img

###################### Basic image functions ##########################

def load_wm():
    img_name = 'kirby003_01a.png'
    img = read_image(img_name)
    watered = img[6:20, 13:119]
    return watered

def show_wm(img):
    watered = get_wm(img)
    show_image(watered)
    return
