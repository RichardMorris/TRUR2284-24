import unittest
from shapes import *

class TestScreen(unittest.TestCase):

    def test_create_screen(self):
        screen =  Screen(5, 8)
        self.assertEqual(screen.width, 5) 
        self.assertEqual(screen.height, 8)
        self.assertEqual(len(screen.cells),8)   # is this part of the public API?
        self.assertEqual(len(screen.cells[0]),5)   # is this part of the public API?
    
    def test_the_str_method_of_a_blank_screen_creates_a_string_with_spaces_separeted_by_newlines(self):
        screen =  Screen(5, 10)
        self.assertEqual(str(screen), (" " * 5 + "\n") * 10)

class Test_Screen_With_Rectangle(unittest.TestCase):
    def test_drawing_a_rectangle_on_an_screen_larger_than_the_rectangle_fills_in_stars(self):
        # arrange
        screen = Screen(5, 5)
        rect = Rectangle(3, 2, 1, 1)
        # act
        rect.draw(screen)
        # assert
        expected = (
            "     \n"
            " *** \n"
            " *** \n"
            "     \n"
            "     \n"
        )
        self.assertEqual(str(screen), expected)

class TestStars(unittest.TestCase):

    #
    def test_stars_produces_a_string_with_works_with_positive_arguments(self):
        self.assertEqual(stars(1), '*')
        self.assertEqual(stars(2), '**')
        self.assertEqual(stars(5), '*****')

    # boundary value test
    def test_stars_method_produces_an_empty_string_with_zero_argument(self):
        self.assertEqual(stars(0), '')

    # erronous test
    def test_stars_method_produces_an_empty_string_with_one_argument(self):
        self.assertEqual(stars(-1), '')


if __name__ == '__main__':
    unittest.main()