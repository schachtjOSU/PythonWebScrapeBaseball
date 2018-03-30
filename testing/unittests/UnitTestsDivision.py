"""
File: UnitTestsDivision.py
Author: Jeffrey Schachtsick
Date: 03/29/2018
Description: unit tests of the Division class
"""

import unittest
import random
from libs.team import Team
from libs.division import Division

class TestDivisionMethods(unittest.TestCase):
    # Setup for the Unittest class
    def setUp(self):
        self.division = Division()
        self.team = Team()

    # Tear down the class
    def tearDown(self):
        self.division = None
        self.team = None

    # Test the Division attributes at init
    def test_init_division_league(self):
        self.assertIsNone(self.division.getleague(), "Fail: Init division league is not None.")

    def test_init_division_name(self):
        self.assertIsNone(self.division.getname(), "Fail: Init division name is not None.")

    def test_init_division_abrv(self):
        self.assertIsNone(self.division.getabrv(), "Fail: Init division abrv is not None.")

    def test_init_division_teams(self):
        self.assertIs(self.division.getteams(), [], "Fail: Init division teams is not []")

    # Make a name for the league, name and abrv and assert the same in return
    def test_division_league(self, league='Canadian'):
        self.division.league = league
        self.assertEqual(self.division.getleague(), league, "Fail: incorrect league name.")

    def test_division_name(self, name='South'):
        self.division.name = name
        self.assertEqual(self.division.getname(), name, "Fail: incorrect division name.")

    def test_division_abrv(self, abrv='CAS'):
        self.division.abrv = abrv
        self.assertEqual(self.division.getabrv(), abrv, "Fail: incorrect division abvr.")

    # Test the modify division method
    def test_modify_division(self):
        # Entry variables
        entry_league = 'Canadian'
        entry_name = 'South'
        entry_abrv = 'CAS'
        self.division.league = entry_league
        self.division.name = entry_name
        self.division.abrv = entry_abrv

        # Modification variables
        mod_league = 'Mexico'
        mod_name = 'North'
        mod_abrv = 'MXN'
        self.division.modifydivision(mod_league, mod_name, mod_abrv)
        self.assertTrue(mod_league == self.division.getleague(), 'Fail: Incorrect league')
        self.assertTrue(mod_name == self.division.getname(), 'Fail: Incorrect name')
        self.assertTrue(mod_abrv == self.division.getabrv(), 'Fail: Incorrect abrv')

    # Test adding a team to the division


    # Test adding a team and then removing the team.


    # Test to add multiple teams to the division


    # Test to add multiple teams to the division and removing


    # Test to add multiple teams to the division, give each win percentages(need wins & losses), and rank them
    