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
<<<<<<< HEAD
    print(222)
    print(file_path)
    f = open("http://192.241.218.106:9000/secret", encoding='utf-8')
=======
    f = open(file_path, encoding='utf-8')
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
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
<<<<<<< HEAD
 
=======

>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
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
<<<<<<< HEAD
=======
        a = len(self.adjacency_list)
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
     


    def adjacent(self, node_1, node_2):
    	if node_2 not in self.adjacency_list[node_1] :
<<<<<<< HEAD
            return False
    		#if node_1 not in self.adjacency_list[node_2]:
    		#		return False
    		
    	else:
            return True
    			
=======
    		if node_1 not in self.adjacency_list[node_2]:
    			return False
    		
    	elif node_2  in self.adjacency_list[node_1] :
    			return True
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
    	
    	



    def neighbors(self, node):
<<<<<<< HEAD
        return list(self.adjacency_list[node])
#           return list(self.adjacency_list[node]);
=======
    	list1 =[]
    	if(len(self.adjacency_list[node])==0):
    		return list1
    	elif(len(self.adjacency_list[node])!=0):
    		return list(self.adjacency_list[node]);
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193



    def add_node(self, node):
<<<<<<< HEAD
    	if node not in self.adjacency_list:
    		self.adjacency_list[node] ={}
    		return True
    	else:
=======
    	if(node not in self.adjacency_list):
    		self.adjacency_list[node] ={}
    		return True
    	elif(node in self.adjacency_list):
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
    		return False


    def remove_node(self, node):	
<<<<<<< HEAD
        if node not in self.adjacency_list:
        	return False
        else:
            self.adjacency_list.pop(node)
            for i in self.adjacency_list.keys():
                if node in self.adjacency_list[i]:
                    self.adjacency_list[i].pop(node)
        return True
=======
        if(node not in self.adjacency_list):
        	return False
        elif(node in self.adjacency_list):
        	for i in self.adjacency_list:
        		self.adjacency_list[i] ={}
        	return True;

>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193

    def add_edge(self, edge):
    	source = edge.source;
    	destination= edge.destination;
    	if(destination in self.adjacency_list[source]):
    		return False;
<<<<<<< HEAD
    	else:
=======
    	elif(destination not in self.adjacency_list[source]):
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
    		self.adjacency_list[source][destination] = edge.weight;
    		return True;



       

    def remove_edge(self, edge):
    	source = edge.source
    	destination= edge.destination

    	
    	if(destination not in self.adjacency_list[source]):
    		return False
<<<<<<< HEAD
    	else:
            self.adjacency_list[source] = {}
            return True 
    		#self.adjacency_list[destination].pop(source)
#    		return True


    def distance(self,source, destination):
        return (self.adjacency_list[source][destination])

    def get_edge(self,source,destination):
        return Edge(source,destination,self.adjacency_list[source][destination])

    def get_graph(self):
        return None
=======
    	elif(destination in self.adjacency_list[source]):
    		self.adjacency_list[source] = {} 
    		self.adjacency_list[destination] ={}
    		return True



>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193





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


<<<<<<< HEAD
    	else:
=======
    	elif(node in self.nodes):
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
    		return False
       	



    def add_edge(self, edge):
        
        source = edge.source;
        destination = edge.destination;
        isource = self.__get_node_index(source)
        idestination = self.__get_node_index(destination)
        if (self.adjacency_matrix[isource][idestination] == edge.weight):

        	return False;
                      

<<<<<<< HEAD
        else:
=======
        elif (self.adjacency_matrix[isource][idestination] != edge.weight):
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193

        	self.adjacency_matrix[isource][idestination] = edge.weight
        	return True



    def remove_node(self, node):

    	if node not in self.nodes:
    		return False

<<<<<<< HEAD
    	else:
=======
    	elif node in self.nodes:
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
        	isource = self.__get_node_index(node);
        	(self.nodes).remove(node);
        	self.adjacency_matrix.pop(isource);
        	for i in range(len(self.adjacency_matrix)):
<<<<<<< HEAD
        		self.adjacency_matrix[i].pop(isource)#={}
=======
        		self.adjacency_matrix[i].pop(isource)
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
        	
        	return True


        




    def remove_edge(self, edge):
    	source = edge.source
    	destination = edge.destination
    	isource=self.__get_node_index(source)
    	idestination=self.__get_node_index(destination)

    	if (self.adjacency_matrix[isource][idestination] != 0):
    		self.adjacency_matrix[isource][idestination] = 0
<<<<<<< HEAD
    		self.adjacency_matrix[idestination][isource] =0 
    		return True

    		
    	else:
            return False
=======
    		 
    		return True

    		
    	elif (self.adjacency_matrix[isource][idestination] == 0):
    			return False
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193

    




    def adjacent(self, node_1, node_2):
    	isource = self.__get_node_index(node_1);
    	idestination = self.__get_node_index(node_2);

    	if(self.adjacency_matrix[isource][idestination]==0):
    		return False;
<<<<<<< HEAD
    	else:
=======
    	elif(self.adjacency_matrix[isource][idestination]!=0):
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
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
        


<<<<<<< HEAD
    def __get_node_index(self, node):
        return self.nodes.index(node);
        pass


    def distance(self, source , destination):
        isource = self.__get_node_index(source)
        idestination = self.__get_node_index(destination)
        return self.adjacency_matrix[isource][idestination]

    def get_edge(self, source, destination):
        isource = self.__get_node_index(source)
        idestination = self.__get_node_index(destination)
        return Edge(source, destination, self.adjacency_matrix[isource][idestination])


    def get_graph(self):
        return None

        
=======
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193



class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []




    def add_node(self, node):
       

        if (node in self.nodes):
            return False;

<<<<<<< HEAD
        else:
=======
        elif (node not in self.nodes):
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
        	(self.nodes).append(node)
        	return True
           

    def add_edge(self, edge):
        
        if (edge in self.edges):
            
            return False

<<<<<<< HEAD
        else:
=======
        elif (edge not in self.edges):
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
            (self.edges).append(edge)
            return True
            
            

    def remove_node(self, node):


        if node not in self.nodes:           
            return False;
<<<<<<< HEAD
        else:
=======
        elif node in self.nodes:
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
            
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
<<<<<<< HEAD
         else:
=======
         elif edge in self.edges:
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
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



<<<<<<< HEAD
    def distance(self,source, destination):
        for i in self.edges:
            if i.source == source and i.destination == destination:
                return i.weight

    def get_edge(self, source, destination):
        for i in self.edges:
            if i.source == source and i.destination == destination:
                return i

    def get_graph(self):
        return self.nodes
=======
>>>>>>> 440f2780bb22ac635173ad60658d5ce982ce2193
