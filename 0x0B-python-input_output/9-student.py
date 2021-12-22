#!/usr/bin/python3
"""Module: 9-student
This is a class Student that defines a student by:
- First_name
- Last_name
- Age
"""


class Student:
    """Class that defines a student.
    Public attributes:
        - first_name
        - last_name
        - age
    Public method to_json().
    """

    def __init__(self, first_name, last_name, age):
        """It accept and assign value to the argument of student class

        Args:
            - first_name
            - last_name
            - age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """It retrieves a dictionary representation of a Student instance

        Args:
            - self
            Return a dictionary of a JSON object
        """
        
        return self.__dict__
