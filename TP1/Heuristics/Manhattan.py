def manhattan(graph, node):

    """ Devuelve la distancia del jugador a la caja libre mas cercana + la distancia de esta caja al goal mas cercano """

    flag = True
    result = 0
    for box in node.boxes_positions:
        for goal in graph.goals:
            distance_to_goal = box.distance_to(goal)
            if distance_to_goal != 0: # Esta caja no esta en un goal
                distance_to_box = node.player_position.distance_to(box)
                auxiliar = distance_to_box + distance_to_goal
                if flag == True:
                    result = auxiliar
                    flag = False
                else:
                    if auxiliar < result:
                        result = auxiliar
    return result

