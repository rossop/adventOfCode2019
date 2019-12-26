import pprint
pp = pprint.PrettyPrinter(indent=4)
flatten = lambda l: [item for sublist in l for item in sublist]


def spiral(matrix, CW = True, M = False,N = False):
    '''
    # R, num of Rows - len(data)
    # C, num of Cols - len(data[0])
    # M, START row
    # N, START column

    :param matrix: matrix to be iterated over
    :param CW: Clockwise or anticlockwise direction
    :param M: Start Row
    :param N: Start Column
    :return:
    '''
    flatten = lambda l: [item for sublist in l for item in sublist]
    R = len(matrix)
    C = len(matrix[0])
    if M or N:
        M = R//2
        N = C//2
    check_matrix = [[False] * len(lst) for lst in matrix]
    m = M
    n = N

    if CW:
        change_dir = {'NORTH': 'E',
                      'E': 'S',
                      'S': 'W',
                      'W': 'NORTH'}
    else:
        change_dir = {'NORTH': 'W',
                      'W': 'S',
                      'S': 'E',
                      'E': 'NORTH'}
    direction = {'NORTH': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    dir = 'NORTH'

    dir_r, dir_c = direction[dir]

    count = 1
    while not all(flatten(check_matrix)):
        print('{},{}'.format(m,n))
        (check_r, check_c) = direction[change_dir[dir]]
        #print(direction[change_dir[dir]])
        if True:
            Turn = check_matrix[m + check_r][n + check_c]
            #print(Turn)
            if not Turn and count > 1:
                dir = change_dir[dir]

            if (0 <= m <= R) and (0 <= n <= C):
                # do something
                check_matrix[m][n] = True
                #print(dir)
                pp.pprint(check_matrix)

            dir_r, dir_c = direction[dir]
            m, n = m + dir_r, n + dir_c
            count += 1

        else:
            'skip to end of side'

        # yield 'something'

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]

R = len(matrix)
C = len(matrix[0])
M = 2
N = 2
check_matrix = [[False ]*len(lst) for lst in matrix]
m = M
n = N

CW = True

spiral(matrix, CW, M ,N)