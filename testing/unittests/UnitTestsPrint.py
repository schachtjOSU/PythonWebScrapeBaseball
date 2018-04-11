"""
File: UnitTestsPring.py
Author: Jeffrey Schachtsick
Date: 03/29/2018
Description: helper to print tests
"""


class TestPrint:
    def __init__(self, test_name=None, description=None):
        self.test_name = test_name
        self.description = description
        self.values = []

    # print test output
    def printtest(self):
        print("********************")
        print("* Test Name: ", self.test_name)
        print("* Description: ", self.description)
        for value in self.values:
            print("*")
            print("* ", value)
        print("")
        print("")