import numpy as np

def getInitialPositions(map):

    '''Given a numpy.nd.array map -> return Player, box, goals, and wall positions'''

    wall   = '#'
    player = '+'
    goals  = '*'
    boxes  = '@'

    WALLS, GOALS, PLAYER, BOXES = list(),list(),list(),list()

    for coord, obj in np.ndenumerate(map):
        if obj == wall:   WALLS.append(coord)
        if obj == goals:  GOALS.append(coord)
        if obj == player: PLAYER.append(coord)
        if obj == boxes:  BOXES.append(coord)

    return WALLS, GOALS, PLAYER, BOXES