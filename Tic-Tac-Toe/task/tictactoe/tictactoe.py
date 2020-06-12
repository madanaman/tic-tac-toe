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
        self.raw_string = ""

    def set_state(self, str):
        if len(str) == 9:
            self.raw_string = str
            for i in range(0, self.rows):
                for j in range(0, self.columns):
                    self.feild[i][j] = str[(j % 3) + (i * 3)]
        else:
            raise wrongStringInputException
        # self.feild = np.array(str)

    def find_result(self):
        winning_dict = {
            "r1": "0,1,2",
            "r2": "3,4,5",
            "r3": "6,7,8",
            "c1": "0,3,6",
            "c2": "1,4,7",
            "c3": "2,5,8",
            "d1": "0,4,8",
            "d2": "2,4,6"
        }
        winner_x = False
        winner_o = False

        for i in winning_dict.keys():
            cnt_x = [self.raw_string[int(pos)] for pos in winning_dict[i].split(",")].count("X")
            cnt_o = [self.raw_string[int(pos)] for pos in winning_dict[i].split(",")].count("O")
            if cnt_x == 3:
                winner_x = True
            elif cnt_o == 3:
                winner_o = True

        blank_cnt = self.raw_string.count("_")

        if abs(self.raw_string.count("X") - self.raw_string.count("O")) >= 2:
            return "Impossible"
        elif winner_x is True and winner_o is not True:
            return "X wins"
        elif winner_o is True and winner_x is not True:
            return "O wins"
        elif winner_o is False and winner_x is False and blank_cnt > 0:
            return "Game not finished"
        elif winner_o is False and winner_x is False and blank_cnt == 0:
            return "Draw"
        elif winner_o is True and winner_x is True:
            return "Impossible"

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
print(game.find_result())
