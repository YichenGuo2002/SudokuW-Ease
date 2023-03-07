#========
import math
import time

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

def setup(size):
    global digits, rows, cols, squares, peers, units, unitlist
    squares = []
    units = {}
    peers = {}
    unitlist = ()

    if(size == 4):
        digits = '1234'
        rows = 'ABCD'
        cols = digits
        unitlist = ([cross(rows, c) for c in cols] +
                [cross(r, cols) for r in rows] +
                [cross(rs, cs) for rs in ('AB','CD') for cs in ('12','34')])
    elif(size == 9):
        digits = '123456789'
        rows = 'ABCDEFGHI'
        cols = digits
        unitlist = ([cross(rows, c) for c in cols] +
                [cross(r, cols) for r in rows] +
                [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
    elif(size == 16):
        digits = ['1', '2', '3', '4', '5', '6', '7','8','9','10','11','12','13','14', '15', '16']
        rows = 'ABCDEFGHIJKLMNOP'
        cols = digits
        unitlist = ([cross(rows, [c]) for c in cols] +
                [cross(r, cols) for r in rows] +
                [cross(rs, cs) for rs in ('ABCD','EFGH','IJKL', 'MNOP') for cs in ('1234','5678',['9','10','11','12'],['13','14','15','16'])])
    elif(size == 25):
        digits = ['1', '2', '3', '4', '5', '6', '7','8','9','10','11','12','13','14', '15', '16', '17', '18', '19', '20', '21','22',
                         '23', '24', '25']
        rows ='ABCDEFGHIJKLMNOPQRSTUVWXY'
        cols = digits
        unitlist = ([cross(rows, [c]) for c in cols] +
                    [cross(r, cols) for r in rows] +
                    [cross(rs, cs) for rs in ('ABCDE','FGHIJ','KLMNO', 'PQRST', 'UVWXY') for cs in ('12345',['6','7','8','9','10'],['11','12','13','14','15'], ['16','17','18','19','20'], ['21','22','23','24','25'])])
    else:
        print("Wrong size")

    squares = cross(rows, cols)
    for s in squares:
        for u in unitlist:
            if s in u:
                if s not in units:
                    units[s] = []
                units[s].append(u)
    for s in squares:
        unit_set = set()
        for unit in units[s]:
            for square in unit:
                if square != s:
                    unit_set.add(square)
        peers[s] = unit_set

def test(size):
    "A set of unit tests."
    assert len(squares) == size * size
    assert len(unitlist) == size * 3
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == (2*size-2+(math.sqrt(size)-1)**2) for s in squares)
    # length of peers for sudoku of any size is 2n-2+(sqrt(n)-1)^2.
    print('All tests pass.')

# ============= Question setup

def grid_values(grid1, size):
    grid1_chars = []
    for c in grid1:
        if str(c) in digits or str(c) in '0.*':
            grid1_chars.append(str(c))
    assert len(grid1_chars) == size * size
    grid1_values = {}
    for k, v in zip(squares, grid1_chars):
        grid1_values[k] = v
    return grid1_values

def grid_values_separated(grid1, size, separator): # if each value is separated by comma or anything
    grid1_divided = grid1.split(separator)
    grid1_chars = []
    for c in grid1_divided:
        if c in digits or c in '0.*':
            grid1_chars.append(c)
    assert len(grid1_chars) == size * size
    grid1_values = {}
    for k, v in zip(squares, grid1_chars):
        grid1_values[k] = v
    return grid1_values


def parse_grid(grid, size):
    # Convert grid to a dict of possible values, {square: digits}, or
    # return False if a contradiction is detected."""
    # To start, every square can be any digit; then assign values from the grid.
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid, size).items():
        if d in digits and not assign(values, s, d):
            return False ## (Fail if we can't assign d to square s.)
    return values

def assign(values, s, d):
    # Eliminate all the other values (except d) from values[s] and propagate.
    # Return values, except return False if a contradiction is detected."""
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False
    
def eliminate(values, s, d):
    # Eliminate d from values[s]; propagate when values or places <= 2.
    # Return values, except return False if a contradiction is detected.
    if d not in values[s]:
        return values ## Already eliminated
    values[s] = values[s].replace(d,'')

    ## (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False ## Contradiction: removed last value
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False

    ## (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False ## Contradiction: no place for this value
        elif len(dplaces) == 1:
            # d can only be in one place in unit; assign it there
            if not assign(values, dplaces[0], d):
                return False
    return values

def display(values, size):
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*int(math.sqrt(size)))]*int(math.sqrt(size)))
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF': 
            print(line)
    print()

def search(values):
    # "Using depth-first search and propagation, try all possible values."
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in squares): 
        return values ## Solved!
    ## Chose the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d)) 
        for d in values[s])

def some(seq):
    # "Return some element of seq that is true."
    for e in seq:
        if e: return e
    return False

def solve(grid, size): 
    setup(size)
    result = {}
    start_time = time.time()
    resultDict = search(parse_grid(grid, size))
    result['time'] = time.time() - start_time
    solution = []
    for key, value in resultDict.items():
        solution.append(int(value))
    result['solution'] = solution
    return result

