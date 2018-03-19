"""
 File: team.py
 Author: Jeffrey Schachtsick
 Date: 03/17/2018
 Description: team object file to hold team specific data and be able to perform actions to the data with methods.
 """


class Team:
    # Team class initializer
    def __init__(self):
        self.city = None
        self.team_name = None
        self.abrev = None
        self.wins = 0
        self.loss = 0
        self.games_played = 0
        self.win_percent = 0

    # Methods for team
    # Calculate the win percentage (e.g. win percentage is 0.500)
    def calcpercent(self):
        self.win_percent = round((self.wins / self.games_played), 3)

    # Add a game and win to the team standings, then calculate the win percentage
    def addwin(self):
        self.wins += 1
        self.games_played += 1
        self.calcpercent()

    # Add a game and a loss to the team standings, then calculate the win percentage
    def addloss(self):
        self.loss += 1
        self.games_played += 1
        self.calcpercent()

    # Make changes to the team attributes
    def modifyteam(self, city, name, abrv):
        self.city = city
        self.team_name = name
        self.abrev = abrv

    # Get methods to retrieve team data
    def getcity(self):
        return self.city

    def getteamname(self):
        return self.team_name

    def getabrv(self):
        return self.abrev

    def getwins(self):
        return self.wins

    def getloss(self):
        return self.loss

    def getgamesplayed(self):
        return self.games_played

    def getwinpercent(self):
        return self.win_percent
