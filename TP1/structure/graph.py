import copy
from collections import deque
from collections import defaultdict 
from structure.node import Node
from structure.position import Position


DIRECTION = {

    'up': Position(0, -1),
    'down': Position(0, 1),
    'right': Position(1, 0),
    'left': Position(-1, 0)
}

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

