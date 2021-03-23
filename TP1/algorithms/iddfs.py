def iddfs(self, _root, maxDepth):

    self.nodes_to_visit_queue.append(_root)
    self.current_node = _root

    while len(self.nodes_to_visit_queue) != 0:

        self.current_node = self.nodes_to_visit_queue.pop()

        # Verify if the node is a win
        if self.check_win(self.current_node):
            print("Los pasos para ganar fueron: " + str(self.current_node.steps))
            print("La profundidad fue: " + str(self.current_node.depth))
            print("En total se expandieron " + str(len(self.visited_nodes)) + " nodos")
            print("En total quedaron " + str(len(self.nodes_to_visit_queue)) + " nodos frontera")
            print("There you have the steps to win")
            return

        #if node has not been visited
        if self.current_node not in self.visited_nodes:

            #Add it to the list of visited
            self.visited_nodes.add(self.current_node)

            #Verify maxDepth & Expand
            if self.current_node.depth != maxDepth:
                self.expand_with_depth(self.current_node)

    print("There was no solution with the given maxDepth")
