import math
from pprint import pprint

def spiral_b(X, Y):
    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            print (x, y)
            # DO STUFF...
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

# spiral_b(10,5)


def spiral(N, M):
    """
    Generator created by [] found on stackoverflow
    :param N:
    :param M:
    :return:
    """
    x,y = 0,0
    dx, dy = 0, -1

    for dumb in range(N*M):
        if abs(x) == abs(y) and [dx,dy] != [1,0] or x>0 and y == 1-x:
            dx, dy = -dy, dx            # corner, change direction

        if abs(x)>N/2 or abs(y)>M/2:    # non-square
            dx, dy = -dy, dx            # change direction
            x, y = -y+dx, x+dy          # jump

        yield x, y
        x, y = x+dx, y+dy

R = 3
C = 5
M = [[(row,col) for col in range(C)] for row in range(R)]

pprint(M)
print(M[1][1])

def spiral(M,x,y):
    m,n = s
    return 0


def sspiral(n):
        k=math.ceil((math.sqrt(n)-1)/2)
        t=2*k+1
        m=t**2
        t=t-1
        if n>=m-t:
            return [k-(m-n),-k]
        else:
            m=m-t

        if n>=m-t:
            return [-k,-k+(m-n)]
        else:
            m=m-t
            if n>=m-t:
                return [-k+(m-n),k]
            else:
                return [k,k-(m-n-t)]

print(sspiral(9))
