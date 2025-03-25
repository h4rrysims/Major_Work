import pygame

PLAYER = 0
ENEMY = 1



class Level_1:
    def __init__(self):
        self.surface = surface
        #TODO:
        self.cash = [5000, 5000]
        self.positions = [0, 0]


        #TODO:
        self.sprites = [None, None]
    def play_turn(self, roll):
        pass

    def enemy_turn(self, roll):
        pass

    def play_turn(self, roll):

        if self.is_player_turn:
            self.player_turn(roll)
        else:
            self.enemy_turn(roll)

        if roll[0] != roll[1]:
            self.is_player_turn = not self.is_player_turn

    if self.cash[PLAYER] == 0:
        self.player_loses()  

    if self.cash[ENEMY] == 0:
        self.enemy_loses()
