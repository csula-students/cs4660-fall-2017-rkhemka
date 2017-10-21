"""
utils package is for some quick utility methods

such as parsing
"""
from . import graph as g
class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)
    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y) + self.symbol)



    



 


def parse_grid_file(graph, file_path):
    """
    ParseGridFile parses the grid file implementation from the file path line
    by line and construct the nodes & edges to be added to graph
    Returns graph object
    """
    # TODO: read the filepaht line by line to construct nodes & edges

    # TODO: for each node/edge above, add it to graph

    

    f = open(file_path)

    rows = []

    for line in f:
        if line[0] == '+' or line[0] == '-':
            continue

        l = line[1:-2]
        rows.append([l[i:i+2] for i in range(0, len(l), 2)])
    
    f.close()

    nodeFrom = []

    nodeTo = []

    y = 0
    for i in rows:
        x = 0

        for block in i:

            if block == '##':

                x = x + 1
                continue

            currentVertex = g.Node(Tile(x, y, block))
            nodeFrom.append(currentVertex)
            

            up = (x, y + 1)
            down = (x, y - 1)
            right = (x + 1, y)
            left = (x - 1, y)

            neighbors = [right,left,up,down]   
            
            for nbr in neighbors:
                if nbr[0] >= len(rows[0]) :  
                    continue

                elif nbr[0] < 0 :
                    continue

                elif nbr[1] >= len(rows):
                    continue

                elif nbr[1] < 0:
                    continue

                
                nextN = rows[nbr[1]][nbr[0]]



                if nextN == '##':
                    continue
                
                NBR = g.Node(Tile(nbr[0], nbr[1], nextN))
                
                nodeTo.append(g.Edge(currentVertex, NBR, 1))
            
            x = x + 1
        y =y + 1


    for i in nodeFrom:
        graph.add_node(i)

    for j in nodeTo:
        graph.add_edge(j)

    return graph


def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile
    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    """

    explored = []

    for n in edges:
        
        if n.source.data.x > n.destination.data.x:
            explored.append('W')
        
        elif n.source.data.x < n.destination.data.x:
            explored.append('E')
        
        elif n.source.data.y > n.destination.data.y:
            explored.append('N')
        
        else:
            explored.append('S')


    return ''.join(explored)