import unittest
import nose
from gimvideo import make_gif
import os
import glob
import shutil
import ImageChops
from PIL import Image


class MakeGifTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.images_path = "images"

    @classmethod
    def tearDownClass(self):
        shutil.rmtree(self.images_path)

    def test_download_images(self):
        """Test method to download images from google."""

        query = "apple"
        path = self.images_path
        images = 5
        make_gif.download_images(query, path, images)

        num_imgs = len(glob.glob(os.path.join(path, "*")))
        self.assertEqual(num_imgs, images)

    def test_create_gif(self):
        """Test method to create a gif file from a bunch of images."""

        file_name = "output.gif"
        duration = 0.05
        path = "test_images"
        make_gif.create_gif(path, duration, file_name=file_name)

        im1 = Image.open("output.gif")
        im2 = Image.open("test_output.gif")
        self.assertIsNone(ImageChops.difference(im1, im2).getbbox())


if __name__ == '__main__':
    nose.main()
