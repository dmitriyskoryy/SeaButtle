import random

class Ship:

    # row - на какой строке поставить корабль
    # col - начиная с какой колонки расположить корабль
    # oriention_horizont - вертикально - v или горизонтально - h
    # number_decks - колличество палуб


    def __init__(self, row, col, number_decks, oriention_horizont):
        self.row = row
        self.col = col
        self.number_decks = number_decks
        self.oriention_horizont = oriention_horizont


    @property
    def ship(self):
        row = str(self.row)
        col = str(self.col)
        number_decks = str(self.number_decks)

        if not number_decks.isdigit() or not col.isdigit() or not row.isdigit():
            return False

        if self.number_decks > 3 or self.number_decks < 1:
            return False
        if (self.number_decks + self.col) > 7 and self.oriention_horizont == 'h':
            return False
        if (self.number_decks + self.row) > 7 and self.oriention_horizont == 'v':
            return False
        if self.row > 6 or self.row < 1:
            return False
        if self.col > 6 or self.col < 1:
            return False

        res = [self.row, self.col, self.number_decks, self.oriention_horizont]
        return res



