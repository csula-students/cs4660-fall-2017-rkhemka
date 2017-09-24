"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if
     the edge already existed
* remove_edge

    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""




from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):
    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph
    """
    f = open(file_path, encoding='utf-8')
    line = f.readline()
    for i in range(int(line)):
        graph.add_node(Node(i))
    text = f.read()
    lines = text.split('\n')
    for line in lines:
        if len(line) > 0:
            values = line.split(':')
            edge = Edge( Node( int( values[0] ) ), Node( int( values[1] ) ), int( values[2] ) )
            graph.add_edge(edge)
    return graph




class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)

class Edge(object):

    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.source, self.destination, self.weight)
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.source, self.destination, self.weight)

    def __eq__(self, other_node):
        return self.source == other_node.source and self.destination == other_node.destination and self.weight == other_node.weight
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.source, self.destination, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}
        a = len(self.adjacency_list)
     


    def adjacent(self, node_1, node_2):
    	if node_2 not in self.adjacency_list[node_1] :
    		if node_1 not in self.adjacency_list[node_2]:
    			return False
    		
    	elif node_2  in self.adjacency_list[node_1] :
    			return True
    	
    	



    def neighbors(self, node):
    	list1 =[]
    	if(len(self.adjacency_list[node])==0):
    		return list1
    	elif(len(self.adjacency_list[node])!=0):
    		return list(self.adjacency_list[node]);



    def add_node(self, node):
    	if(node not in self.adjacency_list):
    		self.adjacency_list[node] ={}
    		return True
    	elif(node in self.adjacency_list):
    		return False


    def remove_node(self, node):	
        if(node not in self.adjacency_list):
        	return False
        elif(node in self.adjacency_list):
        	for i in self.adjacency_list:
        		self.adjacency_list[i] ={}
        	return True;


    def add_edge(self, edge):
    	source = edge.source;
    	destination= edge.destination;
    	if(destination in self.adjacency_list[source]):
    		return False;
    	elif(destination not in self.adjacency_list[source]):
    		self.adjacency_list[source][destination] = edge.weight;
    		return True;



       

    def remove_edge(self, edge):
    	source = edge.source
    	destination= edge.destination

    	
    	if(destination not in self.adjacency_list[source]):
    		return False
    	elif(destination in self.adjacency_list[source]):
    		self.adjacency_list[source] = {} 
    		self.adjacency_list[destination] ={}
    		return True








class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []



    def __get_node_index(self, node):
    	return self.nodes.index(node)



    def add_node(self, node):
    	x = len(self.nodes);
    	if (node not in self.nodes):
    		list=[0 for j in range(x)]
    		self.adjacency_matrix.append(list)
    		(self.nodes).append(node)
    		for i in range(len(self.adjacency_matrix)):
    			self.adjacency_matrix[i].append(0)
    		return True


    	elif(node in self.nodes):
    		return False
       	



    def add_edge(self, edge):
        
        source = edge.source;
        destination = edge.destination;
        isource = self.__get_node_index(source)
        idestination = self.__get_node_index(destination)
        if (self.adjacency_matrix[isource][idestination] == edge.weight):

        	return False;
                      

        elif (self.adjacency_matrix[isource][idestination] != edge.weight):

        	self.adjacency_matrix[isource][idestination] = edge.weight
        	return True



    def remove_node(self, node):

    	if node not in self.nodes:
    		return False

    	elif node in self.nodes:
        	isource = self.__get_node_index(node);
        	(self.nodes).remove(node);
        	self.adjacency_matrix.pop(isource);
        	for i in range(len(self.adjacency_matrix)):
        		self.adjacency_matrix[i].pop(isource)
        	
        	return True


        




    def remove_edge(self, edge):
    	source = edge.source
    	destination = edge.destination
    	isource=self.__get_node_index(source)
    	idestination=self.__get_node_index(destination)

    	if (self.adjacency_matrix[isource][idestination] != 0):
    		self.adjacency_matrix[isource][idestination] = 0
    		 
    		return True

    		
    	elif (self.adjacency_matrix[isource][idestination] == 0):
    			return False

    




    def adjacent(self, node_1, node_2):
    	isource = self.__get_node_index(node_1);
    	idestination = self.__get_node_index(node_2);

    	if(self.adjacency_matrix[isource][idestination]==0):
    		return False;
    	elif(self.adjacency_matrix[isource][idestination]!=0):
    		return True;

        

    def neighbors(self, node):
        list = []
        isource = self.__get_node_index(node)
        x =(len(self.adjacency_matrix[isource]))
        for  i in range(x) :
        	if(self.adjacency_matrix[isource][i])!=0:
        		list.append(self.nodes[i])
     #   print(list)


        return list
        





class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []




    def add_node(self, node):
       

        if (node in self.nodes):
            return False;

        elif (node not in self.nodes):
        	(self.nodes).append(node)
        	return True
           

    def add_edge(self, edge):
        
        if (edge in self.edges):
            
            return False

        elif (edge not in self.edges):
            (self.edges).append(edge)
            return True
            
            

    def remove_node(self, node):


        if node not in self.nodes:           
            return False;
        elif node in self.nodes:
            
            (self.nodes).remove(node)
            
            for i in (self.edges):
                if (i.source == node):
                    self.remove_edge(i);
                elif(i.destination == node ):
                	self.remove_edge(i)

            return True


    def remove_edge(self, edge):
         if edge not in self.edges:
         	return False
         elif edge in self.edges:
         	(self.edges).remove(edge)
         	return True
         	
    def adjacent(self, node_1, node_2):
    	for i in range (len (self.edges)):
    		if ( self.edges[i].source== node_1):
    			if(self.edges[i].destination==node_2):
    				return True

    	return False;
       



    def neighbors(self, node):
        list = []

        for i in range (len (self.edges)):
        	if (self.edges[i].source == node):
        		list.append(self.edges[i].destination);
   #     print (list)
        return list



