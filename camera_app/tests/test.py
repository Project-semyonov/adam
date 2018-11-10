import unittest
from ..source_files.myMotion import MyMotion
# from PIL import Image
import PIL.ImageOps


class TestCamera(unittest.TestCase):
    def test_no_compare(self):
        """
        I think the actual flow of the code should be improved
        this just looks wrong trying to write tests for it
        :return:
        """

        cam = MyMotion(5, .25)

        buff1, vid = cam.sample()

        assert (buff1 == buff1)

        cam.camera.close()

    def test_fake_motion(self):
        """
        Pretty straight forward I'm thinking the tests will work
        we rewrite it
        :return:
        """

        cam = MyMotion(5, .25)

        buff1, vid = cam.sample()

        buff2 = PIL.ImageOps.invert(buff1)

        # Fake motion by the inversion of the image
        assert (buff2 != buff1)

        cam.camera.close()

    def test_no_motion_compare(self):
        """
        Test that there is a None return when no motion is detected
        :return:
        """

        cam = MyMotion(5, .25)

        buff1, vid = cam.sample()

        result = cam.motion(buff1)

        assert (result is None)

        cam.camera.close()

    def test_fake_motion_compare(self):
        """
        Test that motion will return true
        :return:
        """

        cam = MyMotion(5, .25)

        buff1, vid = cam.sample()

        buff2 = PIL.ImageOps.invert(buff1)

        buff2 += buff1

        result = cam.motion(buff2)

        assert (result is True)

        cam.camera.close()

    def test_recording(self):
        """
        This should be the easiest to test in theory
        but idk how to yet
        :return:
        """


if __name__ == '__main__':
    unittest.main()

