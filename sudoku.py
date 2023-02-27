#========
digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits

squares = []
def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]
squares = cross(rows, cols)

unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

units = {}
for s in squares:
    for u in unitlist:
        if s in u:
            if s not in units:
                units[s] = []
            units[s].append(u)

peers = {}
for s in squares:
    unit_set = set()
    for unit in units[s]:
        for square in unit:
            if square != s:
                unit_set.add(square)
    peers[s] = unit_set

def test():
    "A set of unit tests."
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units['C2'] == [
      ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
      ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
      ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(
      ['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
       'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
       'A1', 'A3', 'B1', 'B3'])
    print('All tests pass.')
# =============Step 1 resulved

def grid_values(grid1):
    grid1_chars = []
    for c in grid1:
        if c in digits or c in '0.':
            grid1_chars.append(c)
    assert len(grid1_chars) == 81
    grid1_values = {}
    for k, v in zip(squares, grid1_chars):
        grid1_values[k] = v
    return grid1_values


def parse_grid(grid):
    # Convert grid to a dict of possible values, {square: digits}, or
    # return False if a contradiction is detected."""
    # To start, every square can be any digit; then assign values from the grid.
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():
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

def display(values):
    width = 1+max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF': 
            print(line)
    print()

def solve(grid): return search(parse_grid(grid))

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

if __name__ == '__main__':
    example_board = "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"
    display(solve(example_board))