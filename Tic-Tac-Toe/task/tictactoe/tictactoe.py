# write your code here
# all_moves = [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]]
# for i in all_moves:
#     row = ""
#     for x in i:
#         row = row + x + " "
#     print(row)
# import numpy as np

class Symbol:
    x = "X"
    o = "O"
    _ = " "


class wrongStringInputException(Exception):
    pass


class TicTacToe:
    def __init__(self):
        self.feild = [
            [Symbol._, Symbol._, Symbol._],
            [Symbol._, Symbol._, Symbol._],
            [Symbol._, Symbol._, Symbol._]
        ]
        self.rows = 3
        self.columns = 3

    def set_state(self, str):
        if len(str) == 9:
            for i in range(0, self.rows):
                for j in range(0, self.columns):
                    self.feild[i][j] = str[(j % 3) + (i * 3)]
        else:
            raise wrongStringInputException
        # self.feild = np.array(str)

    def print_state(self):
        print("---------")
        for i in range(0, self.rows):
            row = ""
            for x in range(0, self.columns):
                if x == 0:
                    row = row + "| "
                row = row + self.feild[i][x] + " "
                if x == self.columns - 1:
                    row = row + "|"
            print(row)
        print("---------")


game = TicTacToe()
try:
    game.set_state(input())
except wrongStringInputException:
    print("Wrong string passed")
game.print_state()

