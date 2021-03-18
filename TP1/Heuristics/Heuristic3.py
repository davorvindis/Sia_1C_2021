# La heuristica 3 devuelve la minimia suma de
# distancia del jugador a la caja mas cercana (h2)
# + la suma de la mínima distancia entre los objetivos y cualquier caja (h1)

def heuristic3(graph, node):

    return heuristic1(graph, node) + heuristic2(graph, node)

