from images2gif import writeGif
from PIL import Image
import glob
from google import google
import sys
import os


def download_images(query, path, images=50, image_options=None):
    """Download images from google search images.

    Args:
        query: string to be passed as a google query
        min_size: minimum size in megapixels for the pictures
        color: color filter (can be None)
        path: directory to download images
    """

    res = google.search_images(query, image_options, images)
    google.images.download(res, path)


def create_gif(path, duration, file_name="output.gif", colors=None,
               size=(600, 350)):
    """Create a gif image from a folder containing images.

    Args:
        path: path containing images.
        duration: duration in seconds of each image in the GIF animation.
        file_name: output file name for the gif file.
        size: size of the gif file.
    """

    if not colors:
        file_names = glob.glob(os.path.join(path, "*"))

    else:
        file_names = []
        for color in colors:
            c_path = "{0}{1}{2}".format(path, "_", color)
            file_names.extend(glob.glob(os.path.join(c_path, "*")))

    images = []
    for fn in file_names:
        try:
            images.append(Image.open(fn))
        except:
            # print fn, "couldn't be used!"
            pass

    for im in images:
        im.thumbnail(size, Image.ANTIALIAS)

    # print file_name, images
    writeGif(file_name, images, duration=duration, subRectangles=False)


def _get_image_options(color, image_options):

    if not image_options:
        c_image_options = google.images.ImageOptions()
        c_image_options.color = color

    else:
        c_image_options = image_options
        c_image_options.color = color

    return c_image_options


def main(query, path="images", images=50, image_options=None, duration=0.05,
         colors=None, size=(600, 350)):

    print "Downloading images..."
    if not colors:
        download_images(query, path, images, image_options)

    else:
        c_images = images / len(colors)
        for color in colors:
            print color
            c_image_options = _get_image_options(color, image_options)
            c_path = "{0}{1}{2}".format(path, "_", color)
            download_images(query, c_path, c_images, c_image_options)

    print "Starting to create gif..."
    create_gif(path, duration, size=size)
    print "Gif created!"


if __name__ == '__main__':

    query = "Daft Punk"
    if len(sys.argv) > 1:
        query = sys.argv[1]

    path = "images"
    if len(sys.argv) > 2:
        path = sys.argv[2]

    images = 40
    if len(sys.argv) > 3:
        images = sys.argv[3]

    duration = 0.05
    if len(sys.argv) > 4:
        duration = sys.argv[4]

    colors = ["green", "red", "blue", "yellow"]
    if len(sys.argv) > 5:
        colors = sys.argv[5].split(",")

    image_options = google.images.ImageOptions()
    image_options.larger_than = google.images.LargerThan.MP_4

    main(query=query, path=path, images=images,
         duration=duration, colors=colors, image_options=image_options)

    # create_gif(path, 0.3, colors=colors)
