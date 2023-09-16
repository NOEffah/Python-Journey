# Testing Functions

import unittest
from some_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""
    
    def test_first_last_names(self):
        formatted_name = get_formatted_name('nana', 'effah')
        self.assertEqual(formatted_name, 'Nana Effah')
        
    def test_first_last_middle(self):
        formatted_name = get_formatted_name('nana', 'effah', 'owusu')
        self.assertEqual(formatted_name, 'Nana Owusu Effah')
        
        
if __name__ == '__main__':
    unittest.main()
                             