import unittest

# adding "functions" Folder to the system path
import sys
sys.path.insert(0, '..')

# importing the functions I want to test
from functions.functions import my_func

# Now, defining test cases
# Need to define it as a special class  
class TestMyModule(unittest.TestCase):

# test cases mst always start with "test_"
    def test_myfunc_1(self):
        self.assertEqual(my_func(2,2),8)
        self.assertNotEqual(my_func(-2,-2),-8)

    def test_myfunc_2(self):
        self.assertEqual(my_func(0,0),0)


if __name__ == '__main__':
    unittest.main()

#print(my_func(2,2))


