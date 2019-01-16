import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from imageio import imread
from skimage.color import rgb2grey
from cv2 import Canny, imread as cv_imread

###################### Basic image functions ##########################

def read_image(img_name, grey=False, use_opencv=False, uint8=False):
    """
    Read an image file (.png) into a numpy array in which each entry is
    a row of pixels (i.e. ``len(img)`` is the image height in px. If
    grey is True (default is False), returns a grayscale image (dtype
    uint8 if RGBA, and dtype float32 if greyscale). use_opencv uses the
    `cv2.imread` function rather than `imageio.imread`, which always
    returns a dtype of uint8. uint8 will enforce dtype of uint8 (i.e.
    for greyscale from `imageio.imread`) if set to True, but defaults
    to False.
    """
    data_dir = Path('..') / 'img'
    if use_opencv:
        if grey:
            img = cv_imread(data_dir / img_name, 0)
        else:
            img = cv_imread(data_dir / img_name)
    else:
        img = imread(data_dir / img_name, as_gray=grey)
        if uint8 and img.dtype != 'uint8':
            img = np.uint8(img)
    return img

def show_image(img, bw=False, no_ticks=True, title=''):
    """
    Show an image using a provided pixel row array.
    If bw is True, displays single channel images in black and white.
    """
    if not bw:
        plt.imshow(img)
    else:
        plt.imshow(img, cmap=plt.get_cmap('gray'))
    if no_ticks:
        plt.xticks([]), plt.yticks([])
    if title != '':
        plt.title = title
    plt.show()
    return

def show_original(img_name):
    """
    Debugging/development: produce and display an original image
    """
    img = read_image(img_name)
    show_image(img)
    return img

def save_image(image, figsize, save_path, ticks=False, grey=True):
    """
    Save a given image in a given location, default without ticks
    along the x and y axis, and if there's only one channel
    (i.e. if the image is greyscale) then use the gray cmap
    (rather than matplot's default Viridis).
    """
    fig = plt.figure(figsize=figsize)
    if grey:
        plt.imshow(image, cmap=plt.get_cmap('gray'))
    else:
        plt.imshow(image)
    if not ticks:
        plt.xticks([]), plt.yticks([])
    fig.savefig(save_path)
    return

################# Image gradients and edge detection #############

def get_grads(img):
    """
    Convolve Sobel operator independently in x and y directions,
    to give the image gradient.
    """
    dx = ndimage.sobel(img, 0)  # horizontal derivative
    dy = ndimage.sobel(img, 1)  # vertical derivative
    return dx, dy

def get_grad(img, normalise_rgb=False):
    dx, dy = get_grads(img)
    mag = np.hypot(dx, dy)  # magnitude
    if normalise_rgb:
        mag *= 255.0 / numpy.max(mag)
    return mag

def auto_canny(image, sigma=0.4):
    """
    Zero parameter automatic Canny edge detection courtesy of
    https://www.pyimagesearch.com - use a specified sigma value
    (taken as 0.4 from Dekel et al. at Google Research, CVPR 2017)
    to compute upper and lower bounds for the Canny algorithm
    along with the median of the image, returning the edges.
    
    See the post at the following URL:
    https://www.pyimagesearch.com/2015/04/06/zero-parameter-
    automatic-canny-edge-detection-with-python-and-opencv/
    """
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = Canny(image, lower, upper)
    return edged

###################### Watermarking functions ##########################

def load_wm():
    img_name = 'kirby003_01a.png'
    img = read_image(img_name)
    watered = img[6:20, 13:119]
    return watered

def show_wm(img):
    watered = get_wm(img)
    show_image(watered)
    return
