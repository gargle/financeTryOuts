import unittest
from main import main

class mainTests(unittest.TestCase):
    #def setup(self):

    #def tearDown(self):

    def testFv(self):
        self.assertEquals(main.pv(main.fv(100,0.02,2),0.02,2), 100.00)

if __name__ == "__main__":
    unittest.main()
