import unittest
from ..source.motionVideo import MotionVideo
class Test_camera(unittest.TestCase):
    def test_noMotion(self):
        """I think the actual flow of the code should be improved
            this just looks wrong trying to write tests for it
        """
       cam1 buff1 = MotionVideo.compare()
       
       assert(cam1 == cam1)
       assert(buff1 == buff1)

    def test_motion(self):
        """ pretty straight forward I'm thinking the tests will work
        we rewrite it
        """

        cam1 buff1 = MotionVideo.compare()

        cam2 = PIL.ImageOps.invert(cam1)

        #fake motion by the inversion of the image
        assert(cam2 != cam1)

    def test_recording(self):
        """ this should be the easiest to test in theory
        but idk how to yet
        """
        

if __name__=='__main__':
    unittest.main()
