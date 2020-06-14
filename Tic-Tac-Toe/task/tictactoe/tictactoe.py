# write your code here
# all_moves = [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]]
# for i in all_moves:
#     row = ""
#     for x in i:
#         row = row + x + " "
#     print(row)
# import numpy as np
import re


class Symbol:
    x = "X"
    o = "O"
    _ = " "


class wrongStringInputException(Exception):
    pass


class OutOfBoundCoordinatesException(Exception):
    def __init__(self):
        print("Coordinates should be from 1 to 3!")


class NonIntCoordinatesException(Exception):
    def __init__(self):
        print("You should enter numbers!")


class CellAlreadyFilledException(Exception):
    def __init__(self):
        print("This cell is occupied! Choose another one!")


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
            "r1": "0,0:0,1:0,2",
            "r2": "1,0:1,1:1,2",
            "r3": "2,0:2,1:2,2",
            "c1": "0,0:1,0:2,0",
            "c2": "0,1:1,1:2,1",
            "c3": "0,2:1,2:2,2",
            "d1": "0,0:1,1:2,2",
            "d2": "2,0:2,2:0,2"
        }
        winner_x = False
        winner_o = False

        for i in winning_dict.keys():
            cnt_x = [self.feild[int(x.split(",")[0])][int(x.split(",")[1])] for x in winning_dict[i].split(":")].count(
                "X")
            cnt_o = [self.feild[int(x.split(",")[0])][int(x.split(",")[1])] for x in winning_dict[i].split(":")].count(
                "O")
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

    def validate_n_set_coordinates(self, coordinates, symbol):
        # check for numbers
        # print("starting function")
        x = coordinates.split(" ")
        # print(x, y)
        if re.match(r"[0-9]+", x[0]) is None or re.match(r"[0-9]", x[1]) is None:
            raise NonIntCoordinatesException
            # return False
        if not 1 <= int(x[0]) <= 3 or not 1 <= int(x[1]) <= 3:
            raise OutOfBoundCoordinatesException
            # return False
        # return True
        coordinate_dict = {
            "1 3": "0,0",
            "2 3": "0,1",
            "3 3": "0,2",
            "1 2": "1,0",
            "2 2": "1,1",
            "3 2": "1,2",
            "1 1": "2,0",
            "2 1": "2,1",
            "3 1": "2,2"
        }
        x, y = coordinate_dict[coordinates].split(",")
        # print(self.feild[int(x)][int(y)])
        if self.feild[int(x)][int(y)] != "_":
            raise CellAlreadyFilledException
        else:
            self.feild[int(x)][int(y)] = symbol

player_symbol = "X"
game = TicTacToe()
try:
    game.set_state(input())
except wrongStringInputException:
    print("Wrong string passed")
game.print_state()
# print(game.find_result())
restart_loop = True
while restart_loop is True:
    coordinates = input("Enter the coordinates: ")
    try:
        game.validate_n_set_coordinates(coordinates, player_symbol)
    except OutOfBoundCoordinatesException:
        continue
    except NonIntCoordinatesException:
        continue
    except CellAlreadyFilledException:
        continue
    restart_loop = False
game.print_state()
