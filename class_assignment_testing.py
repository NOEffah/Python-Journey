# Here we test the Employee class from class_test_assignment file

import unittest
from class_test_assignment import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.raise1 = 1000000
        self.my_employee = Employee('Nana', 'Effah', self.raise1)

    def test_default_employee_raise(self):
        raise1 = self.my_employee.give_raise()
        self.assertEqual(raise1, self.raise1 + 5000)

    def test_accept_employee_raise(self):
        raise2 = self.my_employee.give_raise(10000)
        self.assertEqual(raise2, self.raise1 + 10000)


if __name__ == '__main__':
    unittest.main()
