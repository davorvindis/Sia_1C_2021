from load_map import getInitialPositions
import time

from boards.board0 import board0
from boards.board1 import board1
from boards.board2 import board2
from boards.board3 import board3
from boards.board4 import board4
from boards.board5 import board5
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.iddfs import iddfs
from algorithms.a_star import a_star
from structure.node import Node
from structure.position import Position
from structure.graph import Graph
from Heuristics.Manhattan import manhattan

#boards = [board0, board1, ..., board5]
WALLS, GOALS, PLAYER, BOXES = getInitialPositions(board1) #Choose board
player_position = Position(PLAYER[0][1], PLAYER[0][0])
walls_positions = [Position(coord[1], coord[0]) for coord in WALLS]
boxes_positions = [Position(coord[1], coord[0]) for coord in BOXES]
goals_positions = [Position(coord[1], coord[0]) for coord in GOALS]

root = Node(player_position, boxes_positions, [])
g = Graph(walls_positions, goals_positions)

maxDepth = 35
start_time = time.time()
# a_star(g, root)
# iddfs(g, root, maxDepth)
# dfs(g, root)
# bfs(g, root)
print("--- %s seconds ---" % (time.time() - start_time))
