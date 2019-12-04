def dist(x,y):
    '''
    calculate taxicab between two poins ona plane
    :param x: coordinates of a point on a plane
    :param y: coordinates of a point on a plane
    :return: manhattan distance
    '''

    return abs(x[0]-y[0]) + abs(x[1]-y[1])


def wiring(directions):
    centralPort = [0, 0]  # [[x,y]]
    wirePos = []
    opsDict = {'R': [1, 0],
               'U': [0, 1],
               'L': [-1, 0],
               'D': [0, -1]}
    last_point = centralPort

    for step in directions:
        dir = opsDict[step[0]]
        for ii in range( int(step[1:]) ):
           last_point = [x + y for x, y in zip(last_point, dir)]
           wirePos.append(last_point)

    return wirePos


with open('day03_input.txt') as f:
    dirList = f.readlines()
    intDirLst = []
    for lst in dirList:
        intDirLst.append(lst.split(","))


wire0 = set(map(tuple,wiring(intDirLst[0])))
wire1 = set(map(tuple,wiring(intDirLst[1])))
intersections = wire0.intersection(wire1)
intersectDist = []

point = min([dist(value,(0,0)) for value in intersections])
print(point)

intersectionsLst = list(map(list,intersections))

wire0 = wiring(intDirLst[0])
wire1 = wiring(intDirLst[1])
print( min([wire0.index(intersectionPoint) + wire1.index(intersectionPoint)+2 for intersectionPoint in intersectionsLst]))
