from AStar import Node, AStarSolution, Graph
import networkx as nx
import matplotlib.pyplot as plt
import random
import time

def euclidean_heuristic(node_a, node_b):
    dist_x = node_a.pos_x - node_b.pos_x
    dist_y = node_a.pos_y - node_b.pos_y
    return (dist_x ** 2 + dist_y ** 2) ** 0.5

def get_edge_attributes(graph, attribute_name):
        return {(u, v): data[attribute_name] for u, v, data in graph.edges(data=True) if attribute_name in data}



# a = Node("A", 0, 0)
# b = Node("B", 1, 1)
# c = Node("C", 2, 2)

# nodes = {a, b, c}
# edges = {(a, b): 1.4, (b, c): 1.4}


def generate_graph_dataset(num_nodes=8, coord_range=(-100, 100)):
    nodes = set()
    edges = {}
    random.seed(time.time())
    
    for i in range(num_nodes):
        node_name = chr(ord("A"[0])+i)
        pos_x = random.randint(*coord_range)
        pos_y = random.randint(*coord_range)
        nodes.add(Node(node_name,pos_x,pos_y))

    #zaburzenia i polaczenia
    for i in nodes:
        for j in nodes:
            if random.random() > 0.63:
                if i==j:
                    continue
                distance=euclidean_heuristic(i,j)
                noisy_distance = round(distance / random.uniform(0.4,0.9), 2)
                edges[(i,j)]=noisy_distance
            
    return nodes, edges


nodes, edges = generate_graph_dataset()

graph = Graph(nodes, edges)


a_star = AStarSolution(random.choice(list(nodes)), random.choice(list(nodes)), graph)
path = a_star.A_Star(euclidean_heuristic)


if path:
    print("Path:", " -> ".join([node.name for node in path]))

    G = nx.DiGraph() 

    for node in nodes:
        G.add_node(node.name, pos=(node.pos_x, node.pos_y))
    
    for (node1, node2), weight in edges.items():
        G.add_edge(node1.name, node2.name, weight=weight)

    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800)

    path_edges = [(path[i].name, path[i+1].name) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    edge_labels = get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.show()
else:
    print("Path does not exist")
