#620097038
import unittest
from triangle import determine_triangle

class determine_triangleTEST(unittest.TestCase):
    def test_determine_triangle(self):
        self.assertEqual("Equilateral Triangle",determine_triangle(10,10,60), 'Equilateral Triangle')
        self.assertEqual("Equilateral Triangle",determine_triangle(20,20,60), 'Equilateral Triangle')
        self.assertNotEqual(determine_triangle(15,20,35), 'Equilateral Triangle', "Isosceles Triangle")

    def test_determine_isosceles(self):
        self.assertEqual("Isosceles Triangle",determine_triangle(10,10,36),'Isosceles Triangle')
        self.assertEqual("Isosceles Triangle",determine_triangle(90,90,40),'Isosceles Triangle')
        self.assertNotEqual(determine_triangle(10,20,30), 'Isosceles Triangle', 'Neither of the two')
    
    def test_classify_neither(self):
        self.assertEqual("Neither of the two",determine_triangle(32,12,36),'Neither of the two')
        self.assertEqual("Neither of the two",determine_triangle(11,9,36),'Neither of the two')

    def test_classify_invalid(self):
        self.assertEqual("Triangle is Invalid",determine_triangle(1,0,10),'Triangle is Invalid')
        self.assertEqual("Triangle is Invalid",determine_triangle(2,12,10),'Triangle is Invalid')
        self.assertNotEqual(determine_triangle(10, 10, 60), 'Triangle is Invalid', 'Equilateral Triangle')



if __name__ == '__main__': 
    unittest.main() 