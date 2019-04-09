#Gurpreet kaur

from unittest import TestCase
from Assignment4 import Assignment4

class TestAssignment4(TestCase):
    """TestAssignment4 class is for test cases to validate proper functionality of the code"""
    __author__ = "Gurpreet Kaur"

    def test_database(self):
        """This test case creates database and table as well as checks the connectivity with database"""
        print('\n')
        print("This test is written by Gurpreet kaur")
        test = Assignment4.database(self)
        self.assertEqual(test,"database")
        print("This test case shows the database connectivity successfully")
