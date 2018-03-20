"""
File: UnitTestsTeam.py
Author: Jeffrey Schachtsick
Date: 03/18/2018
Description: unit tests of the Team class
"""

import unittest
import random
from libs.team import Team


class TestTeamMethods(unittest.TestCase):
    # Setup for the Unittest class
    def setUp(self):
        self.team = Team()

    # Tear down the class
    def tearDown(self):
        self.team = None

    # Test the Team attributes at init
    def test_init_team_city(self):
        self.assertIsNone(self.team.getcity(), "Fail: Init team city is not None")

    def test_init_team_name(self):
        self.assertIsNone(self.team.getteamname(), "Fail: Init team name is not None")

    def test_init_team_abrv(self):
        self.assertIsNone(self.team.getabrv(), "Fail: Init team abrv is not None")

    def test_init_team_wins(self):
        self.assertEqual(self.team.wins, 0, "Fail: Init team wins is not 0")

    def test_init_team_loss(self):
        self.assertEqual(self.team.getloss(), 0, "Fail: Init team losses is not 0")

    def test_init_team_games_played(self):
        self.assertEqual(self.team.getgamesplayed(), 0, "Fail: Init team games played is not 0")

    def test_init_team_win_percent(self):
        self.assertEqual(self.team.getwinpercent(), 0, "Fail: Init team win percentage is not 0")

    # Make modification to the team city, team_name, and abrev and assert the same in return
    def test_team_city(self, city='Seattle'):
        self.team.city = city
        self.assertEqual(self.team.city, city, 'Fail: incorrect city name')

    def test_team_name(self, name='Sonics'):
        self.team.team_name = name
        self.assertEqual(self.team.team_name, name, 'Fail: Incorrect team name')

    def test_team_abrv(self, abrv='SSS'):
        self.team.abrev = abrv
        self.assertEqual(self.team.abrev, abrv, 'Fail: Incorrect team abreviation')

    # Create a random number, to test the addWins and/or addLoss methods
    def test_team_addwin(self):
        rand_num = random.randrange(163)
        for x in range(0, rand_num):
            self.team.addwin()
        self.assertEqual(rand_num, self.team.getwins(), 'Fail: Generated wins are not the same')

    def test_team_addloss(self):
        rand_num = random.randrange(163)
        for x in range(0, rand_num):
            self.team.addloss()
        self.assertEqual(rand_num, self.team.getloss(), 'Fail: Generated losses are not the same.')

    # test the modify team
    def test_team_modifyteam(self, city='Portland', name='Pickles', abrv='PP'):
        self.team.modifyteam(city, name, abrv)
        self.assertTrue(city == self.team.city, 'Fail: Incorrect team city')
        self.assertTrue(name == self.team.team_name, 'Fail: Incorrect team name')
        self.assertTrue(abrv == self.team.abrev, 'Fail: Incorrect team abreviation')

    # test mix of addwin and addloss
    def test_team_mix_win_loss(self):
        rand_num = random.randrange(163)
        wins = 0
        losses = 0
        for x in range(0, rand_num):
            # There are 162 games, 0 is a win and 1 is a loss
            result = random.randrange(2)
            if result == 0:
                self.team.addwin()
                wins += 1
            else:
                self.team.addloss()
                losses += 1
        self.assertEqual(wins, self.team.getwins(), 'Fail: Incorrect number of wins')
        self.assertEqual(losses, self.team.getloss(), 'Fail: Incorrect number of losses')
        self.assertTrue(((self.team.getwins() + self.team.getloss()) == rand_num),
                        'Fail: Wins and losses did not add up')

    # test number of games played
    def test_team_mix_games_played(self):
        rand_num = random.randrange(163)
        wins = 0
        losses = 0
        for x in range(0, rand_num):
            # There are 162 games, 0 is a win and 1 is a loss
            result = random.randrange(2)
            if result == 0:
                self.team.addwin()
                wins += 1
            else:
                self.team.addloss()
                losses += 1
        self.assertEqual(wins, self.team.getwins(), 'Fail: Incorrect number of wins')
        self.assertEqual(losses, self.team.getloss(), 'Fail: Incorrect number of losses')
        self.assertTrue(((self.team.getwins() + self.team.getloss()) == rand_num),
                        'Fail: Wins and losses did not add up')
        self.assertEqual((self.team.getwins() + self.team.getloss()),
                         self.team.getgamesplayed(), 'Fail: Games played does not add up.')

    # test calculation of win percentage
    def test_team_mix_team_calculation(self):
        rand_num = random.randrange(163)
        wins = 0
        losses = 0
        for x in range(0, rand_num):
            # There are 162 games, 0 is a win and 1 is a loss
            result = random.randrange(2)
            if result == 0:
                self.team.addwin()
                wins += 1
            else:
                self.team.addloss()
                losses += 1
        win_percent = wins / (wins + losses)
        self.assertEqual(wins, self.team.getwins(), 'Fail: Incorrect number of wins')
        self.assertEqual(losses, self.team.getloss(), 'Fail: Incorrect number of losses')
        self.assertTrue(((self.team.getwins() + self.team.getloss()) == rand_num),
                        'Fail: Wins and losses did not add up')
        self.assertEqual((self.team.getwins() + self.team.getloss()),
                         self.team.getgamesplayed(), 'Fail: Games played does not add up.')
        self.assertAlmostEqual(win_percent, self.team.win_percent, 'Fail: Win percentage is not equal')

if __name__ == '__main__':
    unittest.main()
