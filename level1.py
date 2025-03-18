import pygame

PLAYER = 0
ENEMY = 1


from enemy import Enemy

class Level_1:
    def __init__(self):
        #TODO:
        self.cash = [5000, 5000]
        self.positions = [0, 0]


        #TODO:
        self.sprites = [None, None]

    def player_turn(self):
        if self.is_player_turn:
            self.player_turn()
        else:
            self.enemy_turn()

        self.is_player_turn = not self.is_player_turn

