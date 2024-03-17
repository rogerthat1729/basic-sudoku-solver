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

def solve_dfs(puzzle, i=0, j=0):
    if i == 9:  
        return True
    if j == 9: 
        return solve_dfs(puzzle, i + 1, 0)
    if puzzle[i][j] != 0: 
        return solve_dfs(puzzle, i, j + 1)

    for number in range(1, 10): 
        if number in check_possible(puzzle, i, j): 
            puzzle[i][j] = number
            if solve_dfs(puzzle, i, j + 1):
                return True
            puzzle[i][j] = 0 
            
    return False 


def print_puzzle(puzzle):
    for i in range(9):
        for j in range(9):
            print(puzzle[i][j], end=' ')
        print()

def txt_to_puzzle(filename):
    puzzle = []
    with open(filename, 'r') as f:
        for line in f:
            l = []
            for ch in line:
                if ch.isdigit():
                    l.append(int(ch))
                elif ch == '.':
                    l.append(0)
            puzzle.append(l)
    return puzzle

puzzle = txt_to_puzzle('input.txt')
if solve_dfs(puzzle):
    print_puzzle(puzzle)
else:
    print('Not solvable by this method')