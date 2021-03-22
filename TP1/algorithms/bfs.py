
def bfs(graph, root, board):
    graph.nodes_to_visit_queue.append(root)
    graph.current_node = root
    while graph.nodes_to_visit_queue:
        graph.print_move(board, graph.current_node)
        graph.visited_nodes.add(graph.current_node)
        graph.nodes_to_visit_queue.popleft()
        if graph.check_moves(graph.current_node):
            print("Se encontró solucion")
            return
        if not len(graph.nodes_to_visit_queue) == 0:
            graph.current_node = graph.nodes_to_visit_queue[0]
            graph.current_node.add_cost()
    print("solution not found")
