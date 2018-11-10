import unittest
from ..source_files.myMotion import MyMotion
# from PIL import Image
import PIL.ImageOps


class TestCamera(unittest.TestCase):
    def setUp(self):
        self.cam = MyMotion(5, .25)

        self.buff, self.vid = self.cam.sample()

    def tearDown(self):
        self.cam.camera.stop_preview()
        self.cam.camera.close()

    def test_no_compare(self):
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

    def test_no_motion_compare(self):
        """
        Test that there is a None return when no motion is detected
        :return:
        """

        result = self.cam.motion(self.buff)

        assert (result is None)

    def test_fake_motion_compare(self):
        """
        Test that motion will return true
        :return:
        """

        buff2 = PIL.ImageOps.invert(self.buff)

        buff2 += self.buff

        result = self.cam.motion(buff2)

        assert (result is True)

    def test_recording(self):
        """
        This should be the easiest to test in theory
        but idk how to yet
        :return:
        """


if __name__ == '__main__':
    unittest.main()
