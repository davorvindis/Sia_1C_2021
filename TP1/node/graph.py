import copy
from collections import deque
from collections import defaultdict 
from node.node import Node
from node.position import Position


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
