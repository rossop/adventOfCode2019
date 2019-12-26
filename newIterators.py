import pprint
pp = pprint.PrettyPrinter(indent=4)
flatten = lambda l: [item for sublist in l for item in sublist]


def spiral(matrix, CW = True, M = False,N = False):
    '''
    iTERATOR Yields cordinates to a matrix so that it can be iterated spirally.
    :param matrix: matrix to be iterated over
    :param CW: Clockwise or anticlockwise direction
    :param M: Start Row
    :param N: Start Column
    :return:
    '''
    flatten = lambda l: [item for sublist in l for item in sublist]
    R = len(matrix)- 1
    C = len(matrix[0]) - 1
    # if not(M or N):
    #     M = R//2
    #     N = C//2
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
    break_count = 1
    while not all(flatten(check_matrix)):
        (check_r, check_c) = direction[change_dir[dir]]
        print('{} : {},{} in {} by {}'.format(count, m, n, R + 1, C + 1))
        if (0 <= m + check_r <= R) and (0 <= n + check_c <= C):
            notTurn = check_matrix[m + check_r][n + check_c]
            print(count)
            if not notTurn and count > 1:
                dir = change_dir[dir]

            if ((0 <= m <= R) and (0 <= n <= C)):
                # print('{} : {},{} in {} by {}'.format(count, m, n, R + 1, C + 1))
                matrix[m][n] = count
                check_matrix[m][n] = True
                count += 1

            dir_r, dir_c = direction[dir]
            m, n = m + dir_r, n + dir_c
            break_count += 1

        else:
            try:
                Turn = check_matrix[m + check_r][n + check_c]
                print(Turn)
            except:
                Turn = False

            if not Turn:
                dir = change_dir[dir]
                dir_r, dir_c = direction[dir]

            m, n = m + dir_r, n + dir_c
            break_count += 1

        if break_count > 30:
            break


    return check_matrix


matrix = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]

R = len(matrix) -1
C = len(matrix[0])-1
M = 0
N = 4
check_matrix = [[False ]*len(lst) for lst in matrix]
m = M
n = N

CW = True
res = spiral(matrix, CW, M ,N)
pp.pprint(res)