from PIL import Image


def load_img(claude):
    im = Image.open(claude)
    return im


def show_img(im):
    im.show()

def save_img(im, filename):
    im.save(filename, "jpeg")
    show_img(im)
