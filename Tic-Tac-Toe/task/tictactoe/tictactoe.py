# write your code here
# all_moves = [["X", "O", "X"], ["O", "X", "O"], ["X", "X", "O"]]
# for i in all_moves:
#     row = ""
#     for x in i:
#         row = row + x + " "
#     print(row)
class Symbol:
    x = "X"
    o = "O"
    _ = " "


class TicTacToe:
    def __init__(self):
        self.feild = [
            [Symbol.x, Symbol.o, Symbol.x],
            [Symbol.o, Symbol.x, Symbol.o],
            [Symbol.x, Symbol.x, Symbol.o]
        ]

    def print_state(self):
        for i in self.feild:
            row = ""
            for x in i:
                row = row + x + " "
            print(row)


game = TicTacToe()
game.print_state()
