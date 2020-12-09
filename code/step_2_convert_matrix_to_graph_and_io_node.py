import networkx as nx
import numpy as np
 
def createGraphAndIoNodes (matrix):
    
    # Size of a matrix
    m = len(matrix)
    n = len(matrix[0])
    
    # Check that if the a matrix is valid or not
    for i in range(m):
        temp = 0
        for j in range(n):
            temp = temp + matrix[i, j]
        if temp == 0:
            raise ValueError("Problem in previous step")
    
    for j in range(n):
        temp = 0
        for i in range(m):
            temp = temp + matrix[i, j]
        if temp == 0:
            raise ValueError("Problem in previous step")
    
    # Create a new graph G, an input node, and an output node.
    G = nx.DiGraph()
    
    # Add node to graph G
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            # Only consider when there is no impediment in this position
            if (matrix[i, j] == 0):                    
                G.add_node((i, j, "up"))
                G.add_node((i, j, "down"))
                G.add_node((i, j, "right"))
                G.add_node((i, j, "left"))
                
    # Consider the node in the boundary
    for j in range(n):
        if (matrix[0, j] == 0):
            G.add_node((0, j, "down"))
            input_node = (0, j, "down")
            break
        
    for j in range(n):
        if (matrix[m - 1, j] == 0):
            G.add_node((m - 1, j, "down"))
            output_node = (m - 1, j, "down")
            break
               
    
    # Add edge to graph G
    # Firstly, consider the first row
    for j in range(n):
        if (matrix[0, j] == 0):
            G.add_edge((0, j, "down"), (1, j, "down"))
            break
    
    # Next, consider the following row
    for i in range(1, m - 1):
        for j in range(n):
            # Consider only when the position is empty:
            if (matrix[i, j] == 0):
                #     C
                #  E  A  D
                #     B
                Aup = (i, j, "up")
                Adown = (i, j, "down")
                Aleft = (i, j, "left")
                Aright = (i, j, "right")
                
                Bup = (i + 1, j, "up")
                Bdown = (i + 1, j, "down")
                Bleft = (i + 1, j, "left")
                Bright = (i + 1, j, "right") 
                
                Cup = (i - 1, j, "up")
                Cdown = (i - 1, j, "down")
                Cleft = (i - 1, j, "left")
                Cright = (i - 1, j, "right")
                
                Dup = (i, j + 1, "up")
                Ddown = (i, j + 1, "down")
                Dleft = (i, j + 1, "left")
                Dright = (i, j + 1, "right")
                
                Eup = (i, j - 1, "up")
                Edown = (i, j - 1, "down")
                Eleft = (i, j - 1, "left")
                Eright = (i, j - 1, "right")
                
                if (matrix[i, j + 1] == 0):
                    G.add_edge(Aright, Dright)
                else:
                    if (matrix[i + 1, j] == 0):
                        G.add_edge(Aright, Bdown)
                    if (matrix[i - 1, j] == 0):
                        G.add_edge(Aright, Cup)
                        
                if (matrix[i, j - 1] == 0):
                    G.add_edge(Aleft, Eleft)
                else:
                    if (matrix[i + 1, j] == 0):
                        G.add_edge(Aleft, Bdown)
                    if (matrix[i - 1, j] == 0):
                        G.add_edge(Aleft, Cup)
                
                if (matrix[i + 1, j] == 0):
                    G.add_edge(Adown, Bdown)
                else:
                    if (matrix[i, j - 1] == 0):
                        G.add_edge(Adown, Eleft)
                    if (matrix[i, j + 1] == 0):
                        G.add_edge(Adown, Dright)
                
                if (matrix[i - 1, j] == 0):
                    G.add_edge(Aup, Cup)
                else:
                    if (matrix[i, j - 1] == 0):
                        G.add_edge(Aup, Eleft)
                    if (matrix[i, j + 1] == 0):
                        G.add_edge(Aup, Dright)
                        
#   The result of the function is a list, which contains a graph, an input node,
#   and an output node.
    return [G, input_node, output_node]

if __name__ == '__main__':
    matrix = np.array([[1, 1, 0, 1, 1, 1, 1, 1],
                       [1, 1, 0, 0, 1, 1, 1, 1],
                       [1, 1, 1, 0, 1, 1, 1, 1],
                       [1, 0, 0, 0, 1, 1, 1, 1],
                       [1, 0, 1, 1, 1, 1, 1, 1]
                       ])
    graph_list = createGraphAndIoNodes(matrix)
    G = graph_list[0]
    print(G)
