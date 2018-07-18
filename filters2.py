from PIL import Image

def load_img(filename):
  im = Image.open(filename)
  return im

def show_img(im):
  im.show()

def save_img(im, filename):
  im.save(filename, "jpeg")
  show_img(im)

def obamicon(im):
  pixels = im.getdata()
  new_pixels = []

  darkBlue = (0, 51, 76)
  red = (217, 26, 33)
  lightBlue = (112, 150, 158)
  yellow = (252, 227, 166)

  # Process the pixels in the image.
  for p in pixels:
    # Pixel intensity = R value + G value + B value
    intensity = p[0] + p[1] + p[2]

    if intensity < 182:
      new_pixels.append(darkBlue)

    elif intensity >= 182 and intensity < 364:
      new_pixels.append(red)

    elif intensity >= 364 and intensity < 546:
      new_pixels.append(lightBlue)

    elif intensity >=546:
      new_pixels.append(yellow)


im = load_img("claude")
newim = obamicon(im)
show_img(newim)
