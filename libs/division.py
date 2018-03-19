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
    def __init__(self):
        self.league = None
        self.name = None
        self.abrv = None
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

    # Rank teams in the division based on win percentage, secondarily games played, and thirdly team city name
    def rankteams(self):
