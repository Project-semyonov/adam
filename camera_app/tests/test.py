import unittest
from ..source.motionVideo import MotionVideo
class Test_camera(unittest.TestCase):
    def test_one(self):
        """I think the actual flow of the code should be improved
            this just looks wrong trying to write tests for it
        """
       cam1 buff1 = MtionVideo.compare()
       
       assert(cam1 == cam1)
       assert(buff1 == buff1)

if __name__=='__main__':
    unittest.main()
