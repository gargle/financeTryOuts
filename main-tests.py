import unittest
from main import main
import numpy.lib.financial as fin

class mainTests(unittest.TestCase):
    #def setup(self):

    #def tearDown(self):

    def testFv(self):
        self.assertEqual(main.pv(-fin.fv(0.02,2,0,100),0.02,2), 100.00)
        self.assertEqual(-fin.pv(0.02,2,0,main.fv(100,0.02,2)), 100.00)
        self.assertEqual(main.pv(main.fv(100,0.02,2),0.02,2), 100.00)



if __name__ == "__main__":
    unittest.main()
