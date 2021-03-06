from pprint import pprint



def spiral(width, height, dir = 'cw'):
    NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)  # directions

    # direction
    if dir == 'cw':
        turn = {NORTH: E, E: S, S: W, W: NORTH}  # old -> new direction
    elif dir == 'acw':
        turn = {NORTH: W, W: S, S: E, E: NORTH}  # old -> new direction

    # input validity
    if width < 1 or height < 1:
        raise ValueError


    x, y = width // 2, height // 2 # start near the center
    dx, dy = NORTH # initial direction
    matrix = [[None] * width for _ in range(height)]

    print(matrix)
    count = 0
    while True:
        count += 1
        matrix[y][x] = count # visit
        # try to turn right
        new_dx, new_dy = turn[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go


def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:0%dd}" % width
    for row in matrix:
        pprint(" ".join("_"*width if el is None else fmt.format(el) for el in row))


print(spiral(6,3))