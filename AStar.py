# 
# Funkcja została zaimplementowana z pseudokodu znajdujacego sie w Pseudokod.txt
# Zrodlem owego pseudokodu jest wikipedia, jak napisane w jego naglowku
# 


from queue import PriorityQueue

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.insert(0, current)
    return total_path

class Node:
    def __init__(self,name,pos_x,pos_y):
        self.name=name
        self.pos_x=pos_x
        self.pos_y=pos_y
        
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return (self.pos_x==other.pos_x and self.pos_y==other.pos_y) #porownywanie powinno byc koordynatami
    #miasta takie jak Warszawa- woj. mazowieckie, Warszawa- woj. śląskie, Warszawa- woj. świętokrzyskie
    def __hash__(self):
        return hash(self.name)

class Graph:
    def __init__(self,nodes:dict(),edges):
        self.nodes=nodes #zbiór(set) nodeów.
        self.edges=edges # format: {(node:A,node:B): koszt)}
        
    def get_neighbors(self,node):
        neighbors=[]
        for element in self.edges:
            localtuple=element
            if (localtuple[0]==node):
                neighbors.append(localtuple[1])
        return neighbors
                

class AStarSolution:
     
    def __init__(self,start,end,graph:Graph):
        self.start=start
        self.goal=end
        self.graph=graph


    def A_Star(self,heurisitc_function):
        
        main_queue=PriorityQueue() #format: (cost,data)
        main_queue.put((0,self.start))
        
        came_from={}
        
        g_cost={node: float('inf') for node in self.graph.nodes}
        g_cost[self.start]=0
        
        f_cost={node: float('inf') for node in self.graph.nodes}
        f_cost[self.start]=heurisitc_function(self.start,self.goal)
        
        
        while not main_queue.empty():
            
            priority ,current_node=main_queue.get()
            
            if current_node==self.goal:
                return reconstruct_path(came_from,current_node)
            
            for neighbor in self.graph.get_neighbors(current_node):
                total_g_cost=g_cost[current_node] + self.graph.edges[(current_node,neighbor)]
                
                if total_g_cost < g_cost[neighbor]:
                    came_from[neighbor]=current_node
                    g_cost[neighbor]=total_g_cost
                    f_cost[neighbor]=total_g_cost+heurisitc_function(neighbor,self.goal)

                    if neighbor not in [item[1] for item in main_queue.queue]:
                        main_queue.put((f_cost[neighbor],neighbor))
        
        return None # nie znaleziono zadnej sciezki
    