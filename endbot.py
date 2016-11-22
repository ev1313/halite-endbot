from hlt import *
from networking import *

myID, gameMap = getInit()
moves = []

sendInit("Endbot init")

#
# general helperfunctions
#

#
# doMove moves the field in the given direction, it simply appends the move to the list.
#
def doMove(location, direction):
    moves.append(Move(location, direction))

#
# checkStrength returns true if location is stronger than location2
#
def checkStrength(location, location2):
    return gameMap.getSite(location).strength > gameMap.getSite(location2).strength

#
# getLocation returns a Location, but x,y modulo gameMap.width,height
#
def getLocation(x,y):
    return Location(x % gameMap.width, y % gameMap.height)

# main loop
while True:
    gameMap = getFrame()

    # iterate over map
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            site = gameMap.getSite(location)

            # only handle own fields
            if site.owner == myID:
                if random.randint(0, 1) == 0 and checkStrength(location, getLocation(x + 1, y)):
                    doMove(location, EAST)
                elif random.randint(0, 1) == 1 and checkStrength(location, getLocation(x - 1, y)):
                    doMove(location, WEST)
                elif random.randint(0, 1) == 0 and checkStrength(location, getLocation(x, y - 1)):
                    doMove(location, NORTH)
                elif random.randint(0, 1) == 1 and checkStrength(location, getLocation(x, y + 1)):
                    doMove(location, SOUTH)
                else:
                    doMove(location, STILL)

    sendFrame(moves)
