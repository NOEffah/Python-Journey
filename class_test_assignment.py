# We want to test this class

# the class is called Employee
# It takes argument: first_name, last_name and annual_salary
# It has a method called give_raise that adds $5000 to the annual salary by default and also accepts and increase

class Employee:
    """A simple attempt to model an employee"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, g_raise=5000):
        if g_raise >= 0:
            self.annual_salary += g_raise
        return self.annual_salary
