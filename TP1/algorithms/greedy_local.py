import heapq 

def greedy_local(self, root, heuristic):

    # Use heapify to add root
    heapq.heappush(self.priority_queue, root) 

    self.current_node = root

    # Pop first elem
    elem = heapq.heappop(self.priority_queue)

    # Simulate a Do-While
    flag = False

    while True:
        if flag:
            try:
                elem = heapq.heappop(self.priority_queue)
            except IndexError:
                return

        flag = True
        self.current_node = elem

        # Verify if the node is a win
        if self.check_win(self.current_node):
            print(self.current_node.steps)
            print("There you have the steps to win")
            return

        # If node has not been visited
        if self.current_node not in self.visited_nodes:

            # Add it to the list of visited
            self.visited_nodes.add(self.current_node)

            # Expand
            self.expand_possible_moves_using_priority_queue(self.current_node, heuristic)

    print("There was no solution with the given maxDepth")
    