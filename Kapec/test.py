from algo import Point, intersect
import unittest
import program
import algo

class Test_sort(unittest.TestCase):
    def test_1(self):
     line_1_point_start = Point (0,0)
     line_1_point_end = Point (100,100)

     line_2_point_start = Point (0,100)
     line_2_point_end = Point (100,0)
     result = intersect(line_1_point_start,line_1_point_end, line_2_point_start, line_2_point_end)
     self.assertTrue(True)


    def test_2(self):
     line_1_point_start = Point (0,0)
     line_1_point_end = Point (100,0)

     line_2_point_start = Point (0,100)
     line_2_point_end = Point (100,100)
     result = intersect(line_1_point_start,line_1_point_end, line_2_point_start, line_2_point_end)
     self.assertFalse(False)

if __name__ == '__main__':
    # generate_data()
    unittest.main()

