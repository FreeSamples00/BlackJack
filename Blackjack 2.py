# Author: Spencer Christensen
# Project: Blackjack


# imports
import tkinter as tk
import random as r


# classes
class Player:
    def __init__(self):
        self._score = 0
        self._money = 0

        self._cards = []
        self._total = 0
        self._aces_as_11 = 0


class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value
        self._image_name = ''
        self._played = False

    def in_play(self):
        return self._played

    def deal(self, x, y, player):
        self._played = True

# functions


# definitions
dealer = Player()
player = Player()

deck = []
for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
    for value, name in [[11, "Ace",], [2, "Two"], [3, "Three"], [4, "Four"], [5, "Five"], [6, "Six"], [7, "Seven"],
                        [8, "Eight"], [9, "Nine"], [10, "Ten"], [10, "Jack"], [10, "Queen"], [10, "King"]]:
        deck.append(Card(f"{name} of {suit}", value))

