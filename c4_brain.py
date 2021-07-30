
class ConnectFour(object):
    def __init__(self):
        self.game_over = False
        self.current_player = 1
        self.winner = None
        self.board = [[0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 1, 0]]

    def next_spot(self, x_coord):
        for row in range(len(self.board)-1, -1, -1):
            if self.board[row][x_coord] == 0:
                return row

        return None
