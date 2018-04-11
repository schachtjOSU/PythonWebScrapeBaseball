"""
 File: division.py
 Author: Jeffrey Schachtsick
 Date: 03/17/2018
 Description: team object file to hold division specific data and be able to perform actions to the data with methods.
"""

#imports
from libs.team import Team

class Division:
    # Division class initialization
    def __init__(self, league=None, name=None, abv=None):
        self.league = league
        self.name = name
        self.abrv = abv
        self.teams = []

    # Methods for the class
    # modify basic attributes of the division
    def modifydivision(self, league, name, abrv):
        self.league = league
        self.name = name
        self.abrv = abrv

    # Add a team to the division
    def addteam(self, team):
        self.teams.append(team)

    # Remove a team from the division
    def removeteam(self, team):
        self.teams.remove(team)

    # Rank teams in the division based on win percentage, secondarily games played, and thirdly team city name
    def rankteams(self):
        self.teams.sort(key=lambda x: x.win_percent, reverse=True)

    # Get methods to the division attributes
    def getleague(self):
        return self.league

    def getname(self):
        return self.name

    def getabrv(self):
        return self.abrv

    def getteams(self):
        return self.teams