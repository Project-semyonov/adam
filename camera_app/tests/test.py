import unittest
from ..source_files.myMotion import MyMotion
# from PIL import Image
import PIL.ImageOps


class Test_Camera(unittest.TestCase):
    def setUp(self):

        self.test_cam = MyMotion(15)

        self.sample, self.buff = self.test_cam.sample()

    def test_compare(self):
        """
        I think the actual flow of the code should be improved
        this just looks wrong trying to write tests for it
        :return:
        """

        assert (self.buff == self.buff)

    def test_fake_motion(self):
        """
        Pretty straight forward I'm thinking the tests will work
        we rewrite it
        :return:
        """

        buff2 = PIL.ImageOps.invert(self.buff)

        # Fake motion by the inversion of the image
        assert (buff2 != self.buff)

    def test_compare_no_motion(self):
        """
        Test that there is a None return when no motion is detected
        :return:
        """

        result = self.test_cam.motion(self.buff)

        assert (result is None)

    def test_compare_fake_motion(self):
        """
        Test that motion will return true
        :return:
        """

        buff2 = PIL.ImageOps.invert(self.buff)

        buff2 += self.buff

        result = self.test_cam.motion(buff2)

        assert (result is True)

    def test_recording(self):
        """
        This should be the easiest to test in theory
        but idk how to yet
        :return:
        """


if __name__ == '__main__':
    unittest.main()
