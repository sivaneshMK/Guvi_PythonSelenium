'''
Unit Testing is a type of software testing where individual components or funtions of a software
application are tested in isolation to ensure that theywork as expected
'''

import unittest
def age_validation(age):
    if age>=18:
        return "your eligible to vote"
    else:
        return "your not eligible to vote"

class TestAgeValidation(unittest.TestCase):
    def test_age_validation(self):
        assert age_validation(14) =="your eligible to vote"

    def test_age_with_validdata(self):
        #assert age_validation(18) =="your eligible to vote"
        age = int(input("Enter Age"))
        self.assertEqual("your eligible to vote", age_validation(age))