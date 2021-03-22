import copy
from collections import deque
import heapq

def id_a_star(graph, root, heuristic):

    visited_nodes = set()
    root.add_h_cost(heuristic(graph, root))
    frontierHeap = [(root.get_Fvalue(), root)]
    heapq.heapify(frontierHeap)
    nodosExpandidos = 0

    while frontierHeap:

        node = heapq.heappop(frontierHeap)
        node = node[1]

        if node not in visited_nodes:
            visited_nodes.add(node)

        graph.nodes_to_visit_queue.append(node)
        limit = node.get_Fvalue()
        #print('Limit : ', limit)

        while graph.nodes_to_visit_queue:

            graph.current_node = graph.nodes_to_visit_queue.popleft()
            
            if graph.check_win(graph.current_node):
                print("Los pasos para ganar fueron : {0}".format(str(graph.current_node.steps)))
                print("La profundidad fue          : {0}".format(str(graph.current_node.depth)))
                print("En total se expandieron     : {0} nodos ".format(nodosExpandidos))
                print("En total quedaron           : {0} nodos frontera".format(len(frontierHeap)))
                return

            else: #not victory

                nodosExpandidos += 1

                for move in graph.DIRECTION:

                    child_node = copy.deepcopy(graph.current_node)
                    child_node.player_position.move_position(graph.DIRECTION[move])
                    child_node.add_cost()

                    if graph.check_if_wall(child_node.player_position): #hit wall
                        continue

                    if graph.check_if_box(child_node.player_position): #hit box
                        for box in child_node.boxes_positions:         #which box
                            if box == child_node.player_position: 
                                box.move_position(graph.DIRECTION[move]) #move box in the same direction.
                            if not graph.check_if_wall(box) and not graph.check_if_box(box):

                                child_node.steps.append(move)
                                heuristic_cost = heuristic(graph, child_node)
                                child_node.add_h_cost(heuristic_cost)
                                F_score = child_node.get_Fvalue()
                                
                                if child_node not in visited_nodes:
                                    visited_nodes.add(child_node) # getLevel() ?
                                    if F_score > limit:
                                        heapq.heappush(frontierHeap, (F_score, child_node))
                                    else: 
                                        graph.nodes_to_visit_queue.append(child_node)
                            else:
                                continue
                        continue

                    else:

                        #not(hit,wall): OK
                        child_node.steps.append(move)
                        heuristic_cost = heuristic(graph, child_node)
                        child_node.add_h_cost(heuristic_cost)
                        F_score = child_node.get_Fvalue()
                        
                        if child_node not in visited_nodes:
                            visited_nodes.add(child_node)
                            if F_score > limit:
                                heapq.heappush(frontierHeap, (F_score, child_node))
                            else: 
                                graph.nodes_to_visit_queue.append(child_node)

    print('Solucion no encontrada\n')
