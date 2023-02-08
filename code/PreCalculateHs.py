def manhattan(tile, goal,puzzle, size):
    h = 0
    tile_index = puzzle.index(tile)
    goal_index = puzzle.index(goal)
    goal_x = goal_index % size[1]
    goal_y = int((goal_index - goal_x) / size[1])
    curr_x = tile_index % size[1]
    curr_y = int((tile_index - curr_x) / size[1])

    temp = abs(goal_x - curr_x) + abs(goal_y - curr_y)
    h = h + temp
    return h

def generate_puzzle(size):
    puzzle = []
    for i in range(size[0]*size[1]):
        puzzle.append(i)
    return puzzle

def run(size):
    puzzle = generate_puzzle(size)
    tiles = []
    for i in range(len(puzzle)):
        h = []
        for j in range(len(puzzle)):
            h.append(manhattan(i,j,puzzle, size))
        tiles.append({'tile':i, 'h':h})

    distances = tiles
    return distances


