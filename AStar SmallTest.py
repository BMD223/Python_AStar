from AStar import Node,AStarSolution,Graph


def euclidean_heuristic(node_a, node_b):
    dist_x = node_a.pos_x - node_b.pos_x
    dist_y = node_a.pos_y - node_b.pos_y
    return (dist_x ** 2 + dist_y ** 2) ** 0.5

a=Node("A", 0, 0)
b=Node("B", 1, 1)
c=Node("C", 2, 2)
nodes = {a,b,c}
edges = {( a, b): 1.4, (b,c): 1.4}

graph = Graph(nodes, edges)
a_star = AStarSolution(a,c,graph)
path = a_star.A_Star(euclidean_heuristic)
print([node.name for node in path])