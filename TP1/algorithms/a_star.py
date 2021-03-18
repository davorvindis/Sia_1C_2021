from Heuristics.Manhattan import manhattan
import copy

def moves_available(self):
    """
    @return array (move, cost)
        move: available moves in [u,r,d,l]
        cost:   2 if pushing a box,
                1 otherwise
    Checks that moves that involve pushing a block are possible given the
    placement of walls.
    """


def add_to_astar_queue(nodes, queue, _node, cost):
    nodes[hash(_node)] = cost
    add_last = True
    for index, node in enumerate(queue):
        if cost <= node.depth + node.h_cost:
            queue.insert(index, _node)
            add_last = False
            break
    if add_last:
        queue.append(_node)


def a_star(graph, root):
    graph.nodes_to_visit_queue.append(root)
    visited_nodes = set()
    nodes = {hash(root): 0}

    while graph.nodes_to_visit_queue:
        graph.current_node = graph.nodes_to_visit_queue.popleft()
        if graph.check_win(graph.current_node):
            print("Los pasos para ganar fueron: " + str(graph.current_node.steps))
            print("La profundidad fue: " + str(graph.current_node.depth))
            print("En total se expandieron " + str(len(visited_nodes)) + " nodos")
            print("En total quedaron " + str(len(graph.nodes_to_visit_queue)) + " nodos frontera")
            print("win")
            return
        for move in graph.DIRECTION:
            child_node = copy.deepcopy(graph.current_node)  # copio nodo
            child_node.player_position.move_position(graph.DIRECTION[move])  # lo muevo
            child_node.add_cost()  # agrego costo
            if graph.check_if_wall(child_node.player_position):  # chequeo si vale -> no es pared
                continue
            if graph.check_if_box(child_node.player_position):  # chequeo si hay caja
                for box in child_node.boxes_positions:
                    if box == child_node.player_position:
                        box.move_position(graph.DIRECTION[move])
                    if not graph.check_if_wall(box) and not graph.check_if_box(box):  # ACÁ EL MOVIMIENTO VALE
                        child_node.steps.append(move)  # Agrego el movimiento al nodo
                        heuristic_cost = manhattan(graph, child_node)
                        child_node.add_h_cost(heuristic_cost)
                        total_cost = child_node.h_cost + child_node.depth
                        if child_node not in visited_nodes:  # Me fijo si no lo visite
                            visited_nodes.add(child_node)
                            add_to_astar_queue(nodes, graph.nodes_to_visit_queue, child_node, total_cost)
                            nodes[hash(child_node)] = total_cost
                        else:  # si lo visité
                            if nodes[hash(child_node)] > total_cost:
                                nodes[hash(child_node)] = total_cost
                    else:
                        continue
                continue
            else:
                child_node.steps.append(move)  # Agrego el movimiento al nodo
                heuristic_cost = manhattan(graph, child_node)
                child_node.add_h_cost(heuristic_cost)
                total_cost = child_node.h_cost + child_node.depth
                if child_node not in visited_nodes:  # Me fijo si no lo visite
                    visited_nodes.add(child_node)
                    add_to_astar_queue(nodes, graph.nodes_to_visit_queue, child_node, total_cost)
                    nodes[hash(child_node)] = total_cost
                else:  # si lo visité
                    if nodes[hash(child_node)] > total_cost:
                        nodes[hash(child_node)] = total_cost
    print("Solucion no encontrada")
