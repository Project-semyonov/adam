import unittest
from ..source_files.myMotion import MyMotion
import numpy as np


class TestCamera(unittest.TestCase):
    def setUp(self):
        self.cam = MyMotion(5, .35)

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
        buff2 = np.array([])

        # Fake motion by the inversion of the image
        assert (buff2 != self.buff.array)

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
        self.cam.camera.stop_preview()
        self.cam.camera.close()
        cam = MyMotion(5, .25)

        buff2, vid2 = cam.sample()

        result = self.cam.motion(buff2)

        assert (result is True)

        cam.camera.stop_preview()
        
        cam.camera.close()
        
        self.cam = MyMotion(5, 2)
        
        self.buff, self.vid = self.cam.sample()

    def test_recording(self):
        """
        This should be the easiest to test in theory
        but idk how to yet
        :return:
        """

        self.cam.camera.stop_preview()
        self.cam.camera.close()
        
        cam = MyMotion(5, .25)

        buff, vid = cam.sample()

        result = cam.motion(buff)

        cam.new_video(vid)

        assert(open("/root/videos/motion-video-{}.h264".format(cam.timestamp), 'r'))

        cam.camera.stop_preview()
        
        cam.camera.close()
        
        self.cam = MyMotion(5, .25)
        
        self.buff, self.vid = self.cam.sample()


if __name__ == '__main__':
    unittest.main()


