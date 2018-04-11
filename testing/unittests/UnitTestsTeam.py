"""
File: UnitTestsTeam.py
Author: Jeffrey Schachtsick
Date: 03/18/2018
Description: unit tests of the Team class
"""

import unittest
import random
from libs.team import Team
from testing.unittests.UnitTestsPrint import TestPrint


class TestTeamMethods(unittest.TestCase):
    # Setup for the Unittest class
    def setUp(self):
        self.team = Team()

    # Tear down the class
    def tearDown(self):
        self.team = None

    # Test the Team attributes at init
    def test_init_team_city(self):
        test_print = TestPrint('test_init_team_city', 'Test team_city is None at init')
        test_print.values.append('Team City: ' + str(self.team.getcity()))
        test_print.printtest()
        self.assertIsNone(self.team.getcity(), "Fail: Init team city is not None")

    def test_init_team_name(self):
        test_print = TestPrint('test_init_team_name', 'Test team_name is None at init')
        test_print.values.append('Team Name: ' + str(self.team.getteamname()))
        test_print.printtest()
        self.assertIsNone(self.team.getteamname(), "Fail: Init team name is not None")

    def test_init_team_abrv(self):
        test_print = TestPrint('test_init_team_abrv', 'Test abrev is None at init')
        test_print.values.append('Team Abreviation: ' + str(self.team.getabrv()))
        test_print.printtest()
        self.assertIsNone(self.team.getabrv(), "Fail: Init team abrv is not None")

    def test_init_team_wins(self):
        test_print = TestPrint('test_init_team_wins', 'Test wins is 0 at init')
        test_print.values.append('Team Wins: ' + str(self.team.getwins()))
        test_print.printtest()
        self.assertEqual(self.team.getwins(), 0, "Fail: Init team wins is not 0")

    def test_init_team_loss(self):
        test_print = TestPrint('test_init_team_loss', 'Test losses is 0 at init')
        test_print.values.append('Team Losses: ' + str(self.team.getloss()))
        test_print.printtest()
        self.assertEqual(self.team.getloss(), 0, "Fail: Init team losses is not 0")

    def test_init_team_games_played(self):
        test_print = TestPrint('test_init_team_games_played', 'Test games_played is 0 at init')
        test_print.values.append('Games Played: ' + str(self.team.getgamesplayed()))
        test_print.printtest()
        self.assertEqual(self.team.getgamesplayed(), 0, "Fail: Init team games played is not 0")

    def test_init_team_win_percent(self):
        test_print = TestPrint('test_init_team_win_percent', 'Test win_percent is 0 at init')
        test_print.values.append('Win Percentage: ' + str(self.team.getwinpercent()))
        test_print.printtest()
        self.assertEqual(self.team.getwinpercent(), 0, "Fail: Init team win percentage is not 0")

    # Make modification to the team city, team_name, and abrev and assert the same in return
    def test_team_city(self, city='Seattle'):
        self.team.city = city
        test_print = TestPrint('test_team_city', 'Test team_city has a city')
        test_print.values.append('City: ' + str(city))
        test_print.values.append('Team city: ' + str(self.team.getcity()))
        test_print.printtest()
        self.assertEqual(self.team.getcity(), city, 'Fail: incorrect city name')

    def test_team_name(self, name='Sonics'):
        self.team.team_name = name
        test_print = TestPrint('test_team_name', 'Test team_name has a name')
        test_print.values.append('Name: ' + str(name))
        test_print.values.append('Team name: ' + str(self.team.getteamname()))
        test_print.printtest()
        self.assertEqual(self.team.getteamname(), name, 'Fail: Incorrect team name')

    def test_team_abrv(self, abrv='SSS'):
        self.team.abrev = abrv
        test_print = TestPrint('test_team_abrv', 'Test team has a abrv')
        test_print.values.append('Abreviation: ' + str(abrv))
        test_print.values.append('Team abreviation: ' + str(self.team.getabrv()))
        test_print.printtest()
        self.assertEqual(self.team.getabrv(), abrv, 'Fail: Incorrect team abreviation')

    # Create a random number, to test the addWins and/or addLoss methods
    def test_team_addwin(self):
        rand_num = random.randrange(163)
        for x in range(0, rand_num):
            self.team.addwin()
        test_print = TestPrint('test_team_addwin', 'Test adding wins for the team')
        test_print.values.append('Wins: ' + str(rand_num))
        test_print.values.append('Team wins: ' + str(self.team.getwins()))
        test_print.printtest()
        self.assertEqual(rand_num, self.team.getwins(), 'Fail: Generated wins are not the same')

    def test_team_addloss(self):
        rand_num = random.randrange(163)
        for x in range(0, rand_num):
            self.team.addloss()
        test_print = TestPrint('test_team_addloss', 'Test adding losses for the team')
        test_print.values.append('Losses: ' + str(rand_num))
        test_print.values.append('Team losses: ' + str(self.team.getloss()))
        test_print.printtest()
        self.assertEqual(rand_num, self.team.getloss(), 'Fail: Generated losses are not the same.')

    # test the modify team
    def test_team_modifyteam(self, city='Portland', name='Pickles', abrv='PP'):
        self.team.modifyteam(city, name, abrv)
        test_print = TestPrint('test_team_modifyteam', 'Test modifying a team attributes')
        test_print.values.append('City: ' + str(city))
        test_print.values.append('Team city: ' + str(self.team.getcity()))
        test_print.values.append('Name: ' + str(name))
        test_print.values.append('Team name: ' + str(self.team.getteamname()))
        test_print.values.append('Abreviation: ' + str(abrv))
        test_print.values.append('Team abreviation: ' + str(self.team.getabrv()))
        test_print.printtest()
        self.assertTrue(city == self.team.getcity(), 'Fail: Incorrect team city')
        self.assertTrue(name == self.team.getteamname(), 'Fail: Incorrect team name')
        self.assertTrue(abrv == self.team.getabrv(), 'Fail: Incorrect team abreviation')

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
        test_print = TestPrint('test_team_mix_win_loss', 'Test adding a mix of wins and losses')
        test_print.values.append('Team Wins: ' + str(self.team.getwins()))
        test_print.values.append('Team losses: ' + str(self.team.getloss()))
        test_print.values.append('Games Played: ' + str(rand_num))
        test_print.printtest()
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
        test_print = TestPrint('test_team_mix_games_played', 'Test the number of games played')
        test_print.values.append('Team Wins: ' + str(self.team.getwins()))
        test_print.values.append('Team losses: ' + str(self.team.getloss()))
        test_print.values.append('Games Played: ' + str(rand_num))
        test_print.printtest()
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
        win_percent = format(win_percent, '.3f')
        test_print = TestPrint('test_team_mix_team_calculation', 'Test the calculation of win percentage')
        test_print.values.append('Team Wins: ' + str(self.team.getwins()))
        test_print.values.append('Team losses: ' + str(self.team.getloss()))
        test_print.values.append('Games Played: ' + str(rand_num))
        test_print.values.append('Win Percentage: ' + str(self.team.getwinpercent()))
        test_print.values.append('Percentage: ' + str(win_percent))
        test_print.printtest()
        self.assertEqual(wins, self.team.getwins(), 'Fail: Incorrect number of wins')
        self.assertEqual(losses, self.team.getloss(), 'Fail: Incorrect number of losses')
        self.assertTrue(((self.team.getwins() + self.team.getloss()) == rand_num),
                        'Fail: Wins and losses did not add up')
        self.assertEqual((self.team.getwins() + self.team.getloss()),
                         self.team.getgamesplayed(), 'Fail: Games played does not add up.')
        self.assertEqual(win_percent, str(self.team.getwinpercent()), 'Fail: Win percentage is not equal')

if __name__ == '__main__':
    unittest.main()
