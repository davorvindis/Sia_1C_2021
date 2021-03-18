# La Heuristica 1 va a calcular la suma de la mínima distancia 
# entre los objetivos y cualquier caja para cada objetivo

def heuristic1(graph, node):
   
    flag = True
    minimum_distance = 0
    result = 0
    for goal in graph.goals:
        for box in node.boxes_positions:
            possible_minimum_distance = box.distance_to(goal)
            if flag == True:
                minimum_distance = possible_minimum_distance
                flag = False
            else:
                if possible_minimum_distance < minimum_distance:
                    minimum_distance = possible_minimum_distance
        result += minimum_distance
        flag = True
    return result