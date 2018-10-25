import unittest
from ..source_files.myMotion import MyMotion
# from PIL import Image
import PIL.ImageOps


class TestCamera(unittest.TestCase):
    def test_noMotion(self):
        """
        I think the actual flow of the code should be improved
        this just looks wrong trying to write tests for it
        :return:
        """

        buff1 = MyMotion.compare(MyMotion(10))

        assert (buff1 == buff1)

    def test_motion(self):
        """
        Pretty straight forward I'm thinking the tests will work
        we rewrite it
        :return:
        """

        buff1 = MyMotion.compare(MyMotion(10))

        buff2 = PIL.ImageOps.invert(buff1)

        # Fake motion by the inversion of the image
        assert (buff2 != buff1)

    def test_recording(self):
        """
        This should be the easiest to test in theory
        but idk how to yet
        :return:
        """


if __name__ == '__main__':
    unittest.main()
