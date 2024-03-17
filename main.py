possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def union(l1, l2):
    l = l1
    for i in l2:
        if i not in l1:
            l.append(i)
    l.sort()
    return l

def check_possible_row(puzzle, i):
    l = []
    for j in range(9):
        if puzzle[i][j]!=0:
            l.append(puzzle[i][j])
    return l

def check_possible_col(puzzle, j):
    l = []
    for i in range(9):
        if puzzle[i][j]!=0:
            l.append(puzzle[i][j])
    return l

def check_possible_square(puzzle, i, j):
    l = []
    i1 = i//3
    j1 = j//3
    for i2 in range(3):
        for j2 in range(3):
            if puzzle[i1*3+i2][j1*3+j2]!=0:
                l.append(puzzle[i1*3+i2][j1*3+j2])
    return l

def check_possible(puzzle, i, j):
    l1 = check_possible_row(puzzle, i)
    l2 = check_possible_col(puzzle, j)
    l3 = check_possible_square(puzzle, i, j)
    l = union(l1, union(l2, l3))
    m = [p for p in possible if p not in l]
    return m

def solve_once(puzzle):
    possible_vals = [[[] for _ in range(9)] for __ in range(9)]
    cnt = 0
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]==0:
                cnt += 1
                possible_vals[i][j] = check_possible(puzzle, i, j)
    for i in range(9):
        for j in range(9):
            if len(possible_vals[i][j])==1:
                cnt += 1
                puzzle[i][j] = possible_vals[i][j][0]
    return (puzzle, cnt)

def solve(puzzle):
    cnt = 81
    while cnt>0:
        puzzle, cnt = solve_once(puzzle)
    return puzzle

def print_puzzle(puzzle):
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j], end=' ')
        print()

puzzle = [[0, 2, 9, 0, 0, 5, 1, 7, 0],
          [0, 5, 8, 0, 2, 6, 9, 0, 3],
          [3, 0, 0, 0, 0, 0, 6, 0, 2],
          [0, 0, 0, 4, 7, 9, 0, 0, 1],
          [4, 0, 0, 1, 6, 0, 0, 0, 0],
          [9, 0, 0, 5, 0, 8, 4, 0, 0],
          [8, 0, 0, 9, 0, 0, 0, 2, 4],
          [0, 4, 3, 0, 0, 7, 0, 1, 0],
          [0, 0, 0, 0, 5, 4, 3, 8, 6]]

print_puzzle(solve(puzzle))
                