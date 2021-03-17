def bfs(self, root):
    self.nodes_to_visit_queue.append(root)
    self.current_node = root
    while len(self.nodes_to_visit_queue) != 0:
        self.visited_nodes.add(self.current_node)
        self.nodes_to_visit_queue.popleft()
        if self.check_moves(self.current_node):
            print("Se encontró solucion")
            return
        if not len(self.nodes_to_visit_queue) == 0:
            self.current_node = self.nodes_to_visit_queue[0]
            self.current_node.add_cost()
    print("solution not found")
