
class Board:
    board = []

    def __init__(self, list_ships=None):
        self.list_ships = list_ships


    @property
    def new_board(self):
        self.board = ['O' for _ in range(37)]


    def set_board(self, xy, value):
        self.get_board[xy] = value

    @property
    def get_board(self):
        return self.board



    @property
    def add_ship(self):
        if len(self.board) <= 0:
            self.new_board
        if self.list_ships != -1:
            for list_ in self.list_ships:
                for i in range(0, list_[2]):
                    if list_[3] == 'h':
                        self.board[((list_[0] - 1) * 6) + list_[1] + i] = '\u25A0'
                    else:
                        self.board[((list_[0] - 1) * 6) + list_[1] + (i * 6)] = '\u25A0'
        else:
            return -1











