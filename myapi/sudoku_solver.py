import sys
import numpy as np

class Sudoku():

    def __init__(self, values):
        self.board = np.array(list(values)).astype(int).reshape(9, 9)
        self.domain = self.get_domain()

    def clone(self):
        return Sudoku(self.board.astype(str))

    def set_value(self, pos, val):
        self.board[pos] = val
        self.update_domain()

    def allval_str(self):
        return ''.join(str(s) for s in self.board.reshape(81))

    def get_domain(self):
        domain = {}
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    used = set(self.board[i]) | set(self.board[:, j]) | self.get_box_val((i, j))
                    domain[(i, j)] = set(range(1, 10)) - used
        return domain

    def update_domain(self):
        self.domain = self.get_domain()

    def get_box_val(self, ij):
        (i, j) = ij
        box_val = set()
        (i, j) = ((i // 3) * 3, (j // 3) * 3)
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                box_val.add(self.board[x][y])
        return box_val

    def get_mrv(self):
        return min(self.domain.items(), key = lambda x: len(x[1]))

    def gameover(self):
        return False if len(self.domain) else True

    def consistent(self):
        return False if set() in self.domain.values() else True

    def backtrack(self):
        if self.gameover():
            return self.clone()
        var = self.get_mrv()
        for value in var[1]:
            sudoku = self.clone()
            sudoku.set_value(var[0], value)
            if not sudoku.consistent():
                continue
            result = sudoku.backtrack()
            if result is not None:
                return result
        return None

    def ac3(self):
        pass

def main():
    s = Sudoku(sys.argv[1])
    s = s.backtrack()
    outfile = open('output.txt', 'w')
    outfile.write(s.allval_str() + ' BTS' + '\n')
    outfile.close()

def main2():
    infile = open('sudokus_start.txt', 'r')
    outfile = open('output.txt', 'w')
    for line in infile:
        s = Sudoku(line[:-1])
        s = s.backtrack()
        outfile.write(s.allval_str() + ' BTS' + '\n')
    infile.close()
    outfile.close()


if __name__ == '__main__':
    main()