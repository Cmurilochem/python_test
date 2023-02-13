import unittest # library needed to construct test cases

from mymodule import square, double # importing these functions from mymodule 

class TestSquare(unittest.TestCase): # now constructinf the "class" and test cases

    def test_square(self):
        self.assertEqual(square(2),4)         
        self.assertEqual(square(3.0),9.0)
        self.assertNotEqual(square(-3.0),-9.0)

    def test_double(self):
        self.assertEqual(double(3.0),6.0)
        self.assertEqual(double(-4),-8)
        self.assertEqual(double(0),0)

if __name__ == '__main__': # if this is run as script, this is the main program
    unittest.main()            