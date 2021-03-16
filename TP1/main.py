import copy
from collections import deque
from collections import defaultdict 
from load_map import getInitialPositions

from boards.board0 import board0
from boards.board1 import board1
from boards.board2 import board2
from boards.board3 import board3
from boards.board4 import board4
from boards.board5 import board5

class Position:
    """(x,y)"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_position(self, position):
        self.x += position.x
        self.y += position.y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return (self.x < other.x) and (self.y < other.y)

    def __hash__(self):
        return hash(hash(self.x)+hash(self.y))


DIRECTION = {
    'up': Position(0, -1),
    'down': Position(0, 1),
    'right': Position(1, 0),
    'left': Position(-1, 0)
}


class Node:
    """Has the dinamic content of the board: {player_position, boxes_positions} && Node structure"""

    def __init__(self, player_position, boxes_positions, steps):
        self.player_position = player_position
        self.boxes_positions = boxes_positions
        self.steps = steps
        self.depth = 0

    def add_step(self, move):
        self.steps.append(move)

    def __eq__(self, other):
        return self.player_position == other.player_position and self.boxes_positions == other.boxes_positions

    def __str__(self):
        str_node = ""
        print("node: player= " + str(self.player_position) + " boxes= ")
        for b in self.boxes_positions:
            print(b)
        return str_node

    def __hash__(self):
        return hash(self.player_position) + hash(str(self.boxes_positions.sort()))
        

class Graph:
    """ Has the static content of the game: {walls, goals} && Graph structure and game analytics"""
    
    def __init__(self, walls, goals):
        self.walls = walls
        self.goals = goals

    current_node = {}
    nodes_to_visit_queue = deque()
    visited_nodes = set()

    def check_win(self, _node):
        aux = 0
        for b in _node.boxes_positions:
            if b in self.goals:
                aux += 1
            if aux == len(_node.boxes_positions):
                print(self.current_node.steps)
                return True
        return False

    def add_node(self, aux_node, move):
        aux_node.steps.append(move)
        if aux_node not in self.visited_nodes:
            self.nodes_to_visit_queue.append(aux_node)

    def add_node_with_depth(self, aux_node, move, newDepth):
        aux_node.depth = newDepth
        aux_node.steps.append(move)
        if aux_node not in self.visited_nodes:
            self.nodes_to_visit_queue.append(aux_node)

    def check_if_wall(self, position):
        if position in self.walls:
            return True
        return False

    def check_if_box(self, position):
        if position in self.current_node.boxes_positions:
            return True
        return False

    def move_box(self, _node, old_position, new_position):
        _node.boxes_positions.remove(old_position)
        _node.boxes_positions.append(new_position)
        _node.boxes_positions.sort()
        self.check_win(_node)
        return _node

    def check_moves(self, _node):
        for move in DIRECTION:
            aux_node = copy.deepcopy(_node)
            aux_node.player_position.move_position(DIRECTION[move])
            if self.check_if_wall(aux_node.player_position):
                continue
            if self.check_if_box(aux_node.player_position):
                for box in aux_node.boxes_positions:
                    if box == aux_node.player_position:
                        box.move_position(DIRECTION[move])
                    if not self.check_if_wall(box) and not self.check_if_box(box):
                        if self.check_win(aux_node):
                            aux_node.steps.append(move)
                            print(aux_node.steps)
                            return True
                        self.add_node(aux_node, move)
                    else:
                        continue
                continue
            else:
                self.add_node(aux_node, move)
        return False

    def bfs(self, root):
        self.nodes_to_visit_queue.append(root)
        self.current_node = root
        while len(self.nodes_to_visit_queue) != 0:
            print(self.current_node.steps)
            self.visited_nodes.add(self.current_node)
            self.nodes_to_visit_queue.popleft()
            if self.check_moves(self.current_node):
                print("win")
                return
            if not len(self.nodes_to_visit_queue) == 0:
                self.current_node = self.nodes_to_visit_queue[0]

    def dfs(self, root):

        self.nodes_to_visit_queue.append(root)
        self.current_node = root
        
        while len(self.nodes_to_visit_queue) != 0:
            
            print('> ', self.current_node.steps)
            self.current_node = self.nodes_to_visit_queue.pop()
            #Verify if the node is a win

            if self.check_win(self.current_node):
                print("Win")
                return

            #if node has not been visited
            if self.current_node not in self.visited_nodes:
                #Add it to the list of visited
                self.visited_nodes.add(self.current_node)
                #Expand actual node
                self.expand(self.current_node)


    def expand(self, _node):
        newDepth = _node.depth + 1
        for move in DIRECTION:
            aux_node = copy.deepcopy(_node)
            aux_node.player_position.move_position(DIRECTION[move])
            if self.check_if_wall(aux_node.player_position):
                continue
            if self.check_if_box(aux_node.player_position):
                for box in aux_node.boxes_positions:
                    if box == aux_node.player_position:
                        box.move_position(DIRECTION[move])
                    if not self.check_if_wall(box) and not self.check_if_box(box):
                        self.add_node_with_depth(aux_node, move, newDepth)
                    else:
                        continue
                continue
            else:
                self.add_node_with_depth(aux_node, move, newDepth)
        return False

    def iddfs(self, _root, maxDepth):

        self.nodes_to_visit_queue.append(_root)
        self.current_node = _root
        
        while len(self.nodes_to_visit_queue) != 0:
             
            # print('> ', self.current_node.steps)
            self.current_node = self.nodes_to_visit_queue.pop()
            
            # Verify if the node is a win
            if self.check_win(self.current_node):
                print("There you have the steps to win")
                return

            #if node has not been visited
            if self.current_node not in self.visited_nodes:
                
                #Add it to the list of visited
                self.visited_nodes.add(self.current_node)
                
                #Verify maxDepth & Expand
                if self.current_node.depth != maxDepth:
                    self.expand(self.current_node)

        print("There was no solution with the given maxDepth")


#boards = [board0, board1, ..., board5]
WALLS, GOALS, PLAYER, BOXES = getInitialPositions(board0) #Choose board
player_position = Position(PLAYER[0][1], PLAYER[0][0])
walls_positions = [Position(coord[1], coord[0]) for coord in WALLS]
boxes_positions = [Position(coord[1], coord[0]) for coord in BOXES]
goals_positions = [Position(coord[1], coord[0]) for coord in GOALS]

root = Node(player_position, boxes_positions, [])
g = Graph(walls_positions, goals_positions)
g.dfs(root)

#g = Graph()
# g.bfs(root)
#maxDepth = 3
#g.iddfs(root, maxDepth)

