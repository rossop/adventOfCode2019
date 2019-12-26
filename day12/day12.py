class Planet():
    def __init__(self,pos):
        self.pos = pos
        self.newpos = [0, 0, 0]
        self.vel = [0, 0, 0]
        self.acc = [0, 0, 0]

        self.kin = 0
        self.pot = 0
        self.en = 0

    def move(self,planets):
        for planet in planets:
            for val in range(3):
                if self.pos != planet.pos:
                    diff = planet.pos[val]-self.pos[val]
                    if abs(diff)>0:
                        self.vel[val] +=(diff)//abs(diff)

        self.newpos = list(map(sum, zip(self.pos, self.vel)))

    def update(self):
        self.pos = self.newpos

    def energy(self):
        self.pot = sum(map(abs, self.pos))
        self.kin = sum(map(abs, self.vel))
        self.en = self.kin * self.pot

positions = [[-1, 0, 2],
            [2, -10, -7],
            [4, -8, 8],
            [3, 5, -1]]

planets = []
for pos in positions:
    planets.append(Planet(pos))


steps = 100
for ii in range(steps):
    for planet in planets:
        planet.move(planets)

    for planet in planets:
        planet.update()

energy = 0

for planet in planets:
    planet.energy()
    energy += planet.en

print(energy)