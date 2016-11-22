from hlt import *
from networking import *

myID, gameMap = getInit()
sendInit("Endbot init")

while True:
    moves = []
    gameMap = getFrame()

    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            site = gameMap.getSite(location)

            if site.owner == myID:
                if random.randint(0, 1) == 0 and x < gameMap.width-1 and site.strength > gameMap.getSite(Location(x + 1, y)).strength:
                    moves.append(Move(location, EAST))
                elif random.randint(0, 1) == 1 and x > 0 and site.strength > gameMap.getSite(Location(x - 1, y)).strength:
                    moves.append(Move(location, WEST))
                elif random.randint(0, 1) == 0 and y > 0 and site.strength > gameMap.getSite(Location(x, y - 1)).strength:
                    moves.append(Move(location, NORTH))
                elif random.randint(0, 1) == 1 and y < gameMap.height-1 and site.strength > gameMap.getSite(Location(x, y + 1)).strength:
                    moves.append(Move(location, SOUTH))
                else:
                    moves.append(Move(location, STILL))

    sendFrame(moves)
