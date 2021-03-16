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
