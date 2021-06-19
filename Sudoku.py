from copy import deepcopy
from itertools import chain
from math import sqrt
from pprint import pprint

def find_zeros(array: [[int]]):
    for row, line in enumerate(array):
        for col, cell in enumerate(line):
            if cell == 0:
                yield (row,col)

def if_exists(num: int, line: [int]):
    return num in line

def if_exist_in_box(num: int, box: [[int]]):
    return if_exists(num, [*chain(*box)])

def generate_box(sudoku: [[int]], position: (int, int)):
    block_size = int(sqrt(len(sudoku)))
    rng = list(range(0, len(sudoku), block_size))
    result = []
    for i in rng:
        for j in rng:
            if position[0] >= i and position[1] >= j:
                result = [*map(lambda x: x[j:j+block_size], sudoku[i:i+block_size])]
    return result

def transpose(sudoku: [[int]]):
    r = []
    for i in range(0, len(sudoku)):
        r.append((list(map(lambda x: x[len(sudoku)-i-1], sudoku))))
    return [*reversed(r)]

def get_all_possible_values_for_cell(sudoku: [[int]], position: (int, int)):
    possible = set(range(1, len(sudoku)+1))
    for i in possible:
        if not (if_exists(i, sudoku[position[0]]) or
                if_exists(i, transpose(sudoku)[position[1]]) or
                if_exist_in_box(i, generate_box(sudoku, position))):
            yield i


def solve(sudoku: [[int]]):
    zn = [*find_zeros(sudoku)]
    def pos(i: int):
        if not (i < len(zn)):
            yield deepcopy(sudoku)
            return
        ps = zn[i]
        vs = [*get_all_possible_values_for_cell(sudoku, ps)]
        if len(vs) == 0:
            return
        for val in vs:
            sudoku[ps[0]][ps[1]] = val
            yield from pos(i+1)
        sudoku[ps[0]][ps[1]] = 0
    yield from pos(0)

# question = [
# [0, 0, 3, 0, 2, 0, 6, 0, 0],
# [9, 0, 0, 3, 0, 5, 0, 0, 1],
# [0, 0, 1, 8, 0, 6, 4, 0, 0],
# [0, 0, 8, 1, 0, 2, 9, 0, 0],
# [7, 0, 0, 0, 0, 0, 0, 0, 8],
# [0, 0, 6, 7, 0, 8, 2, 0, 0],
# [0, 0, 2, 6, 0, 9, 5, 0, 0],
# [8, 0, 0, 2, 0, 3, 0, 0, 9],
# [0, 0, 5, 0, 1, 0, 3, 0, 0],
# ]
#
question = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

for i in solve(question):
    pprint(i)

