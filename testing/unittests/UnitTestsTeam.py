"""
File: UnitTestsTeam.py
Author: Jeffrey Schachtsick
Date: 03/18/2018
Description: unit tests of the Team class
"""

import unittest
from libs.team import Team


class TestTeamMethods(unittest.TestCase):
    # Setup for the Unittest class
    def setUp(self):
        self.team = Team()

    # Tear down the class
    def tearDown(self):
        self.team.dispose()
        self.team = None

    # Make modification to the team city, team_name, and abrev and assert the same in return
    def test_team_city(self, team, city):
        the_city = team.getcity()
        self.assertEqual(the_city, city, 'incorrect city name')
    
