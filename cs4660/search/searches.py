"""
Searches module defines all different search algorithms
"""
import queue as q1
from heapq import heappush, heappop 

def bfs(graph, initial_node, dest_node):

    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
# refered Algorith from 
# http://interactivepython.org/runestone/static/pythonds/Graphs/ImplementingBreadthFirstSearch.html


    exploredNodes=[]
    exploredNodes.append(initial_node)
    copyOfExploredNodes =[]
    copyOfExploredNodes.append(initial_node)
    
    
    # Creating Dictonary of Distances and starPredeccsor 
    starPredeccsor={}
    distance = {}

    # Calculating distance and predecossr of initial Node
    distance[initial_node] =0
    starPredeccsor[initial_node] = None

    

    while (len(copyOfExploredNodes)>0):
        currentVertex = copyOfExploredNodes.pop(0)
        
        for nbr in graph.neighbors(currentVertex):
            
            if nbr not in exploredNodes:
                
                exploredNodes.append(nbr)

                distance[nbr] = distance[currentVertex]+ graph.distance(currentVertex,nbr)
                
                starPredeccsor[nbr]= currentVertex
            #	print(starPredeccsor)
                copyOfExploredNodes.append(nbr)
                
        if dest_node in exploredNodes:
            #print("I breaked")
            break

            




    list =[]

    while starPredeccsor[dest_node] is not None:
        list = [graph.get_edge(starPredeccsor[dest_node], dest_node)] + list
        #print (list)
        dest_node= starPredeccsor[dest_node]




    return list


def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
## refered algorithm from
# http://interactivepython.org/runestone/static/pythonds/Graphs/GeneralDepthFirstSearch.html
    
 #   
    addVertex=[]    
    exploredNodes = []
    copyOfExploredNodes =[]
    
    
    # Creating Dictonary of Distances and starPredeccsor 
    starPredeccsor={}
    distance = {}

    # Calculating distance and predecossr of initial Node
    distance[initial_node] =0
    starPredeccsor[initial_node] = None

    addVertex.append(initial_node)

    exploredNodes.append(initial_node)
    copyOfExploredNodes.append(initial_node)



 #  print("Start")
 #  print(exploredNodes)



    while (len(copyOfExploredNodes)>0):
        currentVertex = copyOfExploredNodes[0]
       # explored.pop(0)

       # print ("start printing x 0"); print(" ") ;  print(x); print("end"); print("  ")

        flag=True




        order = graph.neighbors(currentVertex)
        order.sort(key=lambda x1 : x1.data)

        


        for nbr in order :

            if nbr not in exploredNodes:

                flag =False
              # print(nbr)
             
                
                
                exploredNodes.append(nbr)
                
                
                #explored.append(nbr)
                #print ("start printing visited 3" ); print(" ") ;  print(explored); print("end"); print("  ")
                distance[nbr] = distance[currentVertex]+ graph.distance(currentVertex,nbr)
               # print ("start printing Distace 4"); print(" ") ;  print(distance); print("end"); print("  ")
                starPredeccsor[nbr]= currentVertex
               # print ("start printing parent 5"); print(" ") ;  print(starPredeccsor); print("end"); print("  ")
                
                copyOfExploredNodes = [nbr] + copyOfExploredNodes

                break

        if dest_node in exploredNodes:

            break

        if flag:

            copyOfExploredNodes.pop(0)

         #   print("sassasa") 



    list =[]

    while starPredeccsor[dest_node] is not None:

        list = [graph.get_edge(starPredeccsor[dest_node], dest_node)] + list
        
        dest_node= starPredeccsor[dest_node]




    return list


#   	pass

def dijkstra_search(graph, initial_node, dest_node):

    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """


    exploredNodes =[]

    startExploringNodes ={}
    

    # copyOfExploredNodes will check if the node was initilly considered for dijkstra or not
    # copyOfExploredNodes is to implement an array of True or False Like we have in virtuailiztion Link
    copyOfExploredNodes=[]

   

    # Creating Dictonary of Distances and starPredeccsor 
    starPredeccsor={}
    distance = {}



    startExploringNodes[initial_node] = 0
    
    # Calculating distance and predecossr of initial Node
    
    distance[initial_node] = 0
    starPredeccsor[initial_node] = None

    # path[initial_node]=-1
    exploredNodes.append(initial_node)



    #a=graph.distance(initial_node,dest_node)
    #a =(graph.size())
  

    while len(startExploringNodes)>0:

        currentVertex = min(startExploringNodes, key=startExploringNodes.get)
    
        

        

        startExploringNodes.pop(currentVertex)
        exploredNodes.append(currentVertex)



        for nbr in graph.neighbors(currentVertex):
        	
        	if nbr not in copyOfExploredNodes and nbr not in exploredNodes:


        		startExploringNodes[nbr] =distance[currentVertex]+ graph.distance(currentVertex,nbr)

        		distance[nbr] = distance[currentVertex]+ graph.distance(currentVertex,nbr)
        		
        		starPredeccsor[nbr] = currentVertex
	        	
	        	copyOfExploredNodes.append(nbr)

	        elif distance[nbr]>distance[currentVertex]+graph.distance(currentVertex,nbr):

	        	startExploringNodes[nbr] =distance[currentVertex]+ graph.distance(currentVertex,nbr)

	        	distance[nbr] = distance[currentVertex]+ graph.distance(currentVertex,nbr)

	        	starPredeccsor[nbr] = currentVertex

	        	copyOfExploredNodes.append(nbr)



#	        	elif :



        if dest_node in exploredNodes:
            break




    list =[]
    while starPredeccsor[dest_node] is not None:

        list = [graph.get_edge(starPredeccsor[dest_node], dest_node)] + list

        dest_node = starPredeccsor[dest_node]

       # print(list)




    return list


                

       



    #




def a_star_search(graph, initial_node, dest_node):

    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """



    #print (dest_node)

    startAStar = {}
    defect = {}
    
    exploredNodes = []
    copyOfExploredNodes = []

    # Creating Dictonary of Distances and starPredeccsor 
    starPredeccsor = {}
    distance = {}


    defect[initial_node] = distanceFromPoints(initial_node, dest_node)

    # Calculating distance and predecossr of initial Node

    starPredeccsor[initial_node] = None
    distance[initial_node] = 0
    startAStar[initial_node] = 0
    
    exploredNodes.append(initial_node)

    while (len(startAStar)>0):
        currentVertex = min(defect, key=defect.get)

        defect.pop(currentVertex)

        startAStar.pop(currentVertex)
        
        exploredNodes.append(currentVertex)



        for nbr in graph.neighbors(currentVertex):

            if  nbr not in exploredNodes and nbr not in copyOfExploredNodes  :
                
                startAStar[nbr] = distance[currentVertex] + graph.distance(currentVertex, nbr)
                
                defect[nbr] = distanceFromPoints(nbr, dest_node) + graph.distance(currentVertex, nbr)
                
                distance[nbr] = distance[currentVertex] + graph.distance(currentVertex, nbr)
                
                starPredeccsor[nbr] = currentVertex
                
                copyOfExploredNodes.append(nbr)

            elif distance[nbr] > distance[currentVertex] + graph.distance(currentVertex, nbr):


                startAStar[nbr] = distance[currentVertex] + graph.distance(currentVertex, nbr)
                
                defect[nbr] = distanceFromPoints(nbr, dest_node) + graph.distance(currentVertex, nbr)
                
                distance[nbr] = distance[currentVertex] + graph.distance(currentVertex, nbr)
                
                starPredeccsor[nbr] = currentVertex
                
                copyOfExploredNodes.append(nbr)


        if (dest_node in exploredNodes):
            break







    list = []
    while starPredeccsor[dest_node] is not None:

        list = [graph.get_edge(starPredeccsor[dest_node], dest_node)] + list
        dest_node = starPredeccsor[dest_node]
  


    return list




def distanceFromPoints(x,y):
    X = ((x.data.x - y.data.x) ** 2)
    Y = ((x.data.y - y.data.y) ** 2)
    value = ((X + Y)**0.5)
    return value











