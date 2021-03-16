import copy
from collections import deque
from collections import defaultdict 


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
    current_node = {}
    nodes_to_visit_queue = deque()
    visited_nodes = set()

    walls = [Position(0, 0), Position(0, 1), Position(0, 2), Position(0, 3), Position(0, 4), Position(1, 0),
             Position(2, 0), Position(3, 0), Position(3, 1), Position(3, 2), Position(3, 3), Position(3, 4),
             Position(1, 4), Position(2, 4)]
    goals = [Position(1, 1)]

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
                    if not self.check_if_wall(box):
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

    def breadth_first_search(self, root):
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

    def addNeighbours(self, node, neighbours):
        for move in DIRECTION:
            aux_node = copy.deepcopy(node)
            aux_node.player_position.move_position(DIRECTION[move])
            if self.check_if_wall(aux_node.player_position):
                continue
            if self.check_if_box(aux_node.player_position):
                for box in aux_node.boxes_positions:
                    if box == aux_node.player_position:
                        box.move_position(DIRECTION[move])
                    else:
                        continue
                    if not self.check_if_wall(box):
                        if not self.check_if_box(box):
                            if self.check_win(aux_node):
                                aux_node.steps.append(move)
                                print(aux_node.steps)
                                return True
                            self.add_node(aux_node, move)
                            neighbours.add(aux_node)
                    else:
                        continue
                continue
            else:
                self.add_node(aux_node, move)
                neighbours.add(aux_node)
        return False

    def iddfs(self, node, depth, maxDepth):
        if depth == maxDepth: return
        print("error1")
        if self.visited_nodes.__contains__(node): return
        self.visited_nodes.add(node)
        print("error2")
        neighbours = deque()
        if self.addNeighbours(node, neighbours): return
        print("error3")
        for next in iter(neighbours.get, None):
            depth += 1
            print("error4")
            iddfs(self, next, depth, maxDepth)


root = Node(Position(2, 2), [Position(1, 2)], [])
g = Graph()
# g.breadth_first_search(root)
initialDepth = 0
maxDepth = 3
g.iddfs(root, initialDepth, maxDepth)
