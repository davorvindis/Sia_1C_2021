# La Heuristica 2 va a calcular la distancia entre el jugador y la caja mas cercana

def heuristic2(graph, node):
   
    flag = True
    result = 0
    for box in node.boxes_positions:
        distance_to_box = node.player_position.distance_to(box)
        if flag == True:
            result = distance_to_box
            flag = False
        else:
            if distance_to_box < result:
                result = distance_to_box
    return result