from structure.position import Position


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
        self.h_cost = 0


    def add_step(self, move):
        self.steps.append(move)

    def add_cost(self):
        self.depth += 1

    def add_h_cost(self, cost):
        self.h_cost = cost

    def __eq__(self, other):
        return self.player_position == other.player_position and self.boxes_positions == other.boxes_positions

    def __str__(self):
        str_node = ""
        print("node: player= " + str(self.player_position) + " boxes= ")
        for b in self.boxes_positions:
            print(b)
        return str_node

    def __hash__(self):
        return hash(self.player_position) + hash(str(self.boxes_positions.sort())) + hash(str(self.h_cost))