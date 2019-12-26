class Planet():
    def __init__(self,pos):
        self.pos = pos
        self.vel = [0, 0, 0]
        self.acc = [0, 0, 0]

        self.kin = 0
        self.pot = 0
        self.energy = 0
        print('{}  --  {}'.format(self.pos, self.vel))

    def move(self,planets):
        for planet in planets:
            for val in range(3):
                if self.pos != planet.pos:
                    diff = self.pos[val] - planet.pos[val]
                    if abs(diff)>0:
                        self.vel[val] +=(diff)//abs(diff)

        self.pos = list(map(sum, zip(self.pos, self.vel)))
        print('{}  --  {}'.format(self.pos, self.vel))

    def energy(self):
        self.pot = sum(map(abs, self.pos))
        self.kin = sum(map(abs, self.vel))
        self.energy = self.kin + self.pot

positions = [[-1, 0, 2],
            [2, -10, -7],
            [4, -8, 8],
            [3, 5, -1]]

planets = []
for pos in positions:
    planets.append(Planet(pos))
print('_______________' * 2)


steps = 10
for ii in range(steps):
    for planet in planets:
        planet.move(planets)
    print('_______________'*2)
