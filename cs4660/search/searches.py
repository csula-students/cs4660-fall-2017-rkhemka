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

    visited =[]
    visited.append(initial_node)
    addVertex=[]
    addVertex.append(initial_node)

    
    
    # Creating Dictonary of Distances and starPredeccsor 
    starPredeccsor={}
    distance = {}
    # Calculating distance and predecossr of initial Node
    distance[initial_node] =0
    starPredeccsor[initial_node] = None

    

    while (len(visited)>0):
        currentVertex = visited.pop(0)
        
        for nbr in graph.neighbors(currentVertex):
            
            if nbr not in addVertex:
                
                visited.append(nbr)
                distance[nbr] = distance[currentVertex]+ graph.distance(currentVertex,nbr)
                starPredeccsor[nbr]= currentVertex
                addVertex.append(nbr)
                
        if dest_node in addVertex:
            #print("I breaked")
            break

            




    list =[]

    while starPredeccsor[dest_node] is not None:
        list = [graph.get_edge(starPredeccsor[dest_node], dest_node)] + list
        print (list)
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
    visited =[]
    visited.append(initial_node)
    addVertex=[]    
    
    
    # Creating Dictonary of Distances and starPredeccsor 
    starPredeccsor={}
    distance = {}
    # Calculating distance and predecossr of initial Node
    distance[initial_node] =0
    starPredeccsor[initial_node] = None
    addVertex.append(initial_node)



    while (len(visited)>0):
        currentVertex = visited[0]
        #visited.pop(0)

       # print ("start printing x 0"); print(" ") ;  print(x); print("end"); print("  ")

        flag=True


        G = graph.neighbors(currentVertex)
        
    


        for nbr in  graph.neighbors(currentVertex): #graph.neighbors(currentVertex):
            if nbr not in addVertex:
                flag =False
             
                
                
                visited = [nbr] + visited
                
                #visited.append(nbr)
                #print ("start printing visited 3" ); print(" ") ;  print(visited); print("end"); print("  ")
                distance[nbr] = distance[currentVertex]+ graph.distance(currentVertex,nbr)
                print ("start printing Distace 4"); print(" ") ;  print(distance); print("end"); print("  ")
                starPredeccsor[nbr]= currentVertex
               # print ("start printing parent 5"); print(" ") ;  print(starPredeccsor); print("end"); print("  ")
                addVertex.append(nbr)
                #print ("start printing parent 6"); print(" ") ;  print(addVertex); print("end"); print("  ")
                break
        if dest_node in addVertex:
            break
        if flag:
            visited.pop(0)
            print("sassasa") 
#                visited.pop(0)
#    visited.pop(0)





    list =[]

    while starPredeccsor[dest_node] is not None:
        list = [graph.get_edge(starPredeccsor[dest_node], dest_node)] + list
        dest_node= starPredeccsor[dest_node]




    return list


   # pass

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
    distance[initial_node] =0
    starPredeccsor[initial_node] = None
    #path[initial_node]=-1
    exploredNodes.append(initial_node)

    x=dest_node


    #a=graph.distance(initial_node,dest_node)
    #a =(graph.size())
  

    while len(exploredNodes)>0:
        currentVertex = min(startExploringNodes, key=startExploringNodes.get)#_edge)
        #visited.pop(currentVertex)
        

        

        startExploringNodes.pop(currentVertex)
        exploredNodes.append(currentVertex)
        copyOfExploredNodes.append(currentVertex)




        for nbr in graph.neighbors(currentVertex):
            #print("Inside For")
            if nbr in copyOfExploredNodes:
                #print("Inside If")
                break
            else:

                #print(distance[nbr])

                if( (nbr not in startExploringNodes and nbr not in exploredNodes) or (distance[nbr]>distance[currentVertex]+graph.distance(currentVertex,nbr))):
                    copyOfExploredNodes.append(nbr)
                    startExploringNodes[nbr] =distance[currentVertex]+ graph.distance(currentVertex,nbr)
                    distance[nbr] = distance[currentVertex]+ graph.distance(currentVertex,nbr)
                    starPredeccsor[nbr] = currentVertex
                    exploredNodes.append(nbr)
                    #print("ex")

        if dest_node in exploredNodes:
            break




    list =[]

    while starPredeccsor[x] is not None:

        list = [graph.get_edge(starPredeccsor[x], x)] + list
        x= starPredeccsor[x]




    return list


                

       



    #





def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """



    
    
                
                
   
   # pass

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
    distance[initial_node] =0
    starPredeccsor[initial_node] = None
    #path[initial_node]=-1
    exploredNodes.append(initial_node)

    x=dest_node


    #a=graph.distance(initial_node,dest_node)
    #a =(graph.size())
  

    while len(exploredNodes)>0:
        currentVertex = exploredNodes[0] 
        #visited.pop(currentVertex)
        
        copyOfExploredNodes.append(currentVertex)

        for nbr in graph.neighbors(currentVertex):
            #print("Inside For")
            if nbr in copyOfExploredNodes:
                #print("Inside If")
                break
            else:
                new_cost = distance[currentVertex]+graph.distance(currentVertex, nbr)
                if(nbr not in cost_so_far or new_cost <cost_so_far[nbr]):
                    cost_so_far[nbr]= new_cost
                    priority = new_cost+ heuristic(dest_node, nbr)
                    startExploringNodes.append(nbr)
                    starPredeccsor[nbr]= currentVertex
                    copyOfExploredNodes.append(nbr)
            if dest_node in exploredNodes:
                break
    list =[]
    while starPredeccsor[x] is not None:
        list = [graph.get_edge(starPredeccsor[x], x)] + list
        x= starPredeccsor[x]
    return list


                #print(distance[nbr])
'''33
                if( (nbr not in startExploringNodes and nbr not in exploredNodes) or (distance[nbr]>distance[currentVertex]+graph.distance(currentVertex,nbr))):
                    copyOfExploredNodes.append(nbr)
                    startExploringNodes[nbr] =distance[currentVertex]+ graph.distance(currentVertex,nbr)
                    distance[nbr] = distance[currentVertex]+ graph.distance(currentVertex,nbr)
                    starPredeccsor[nbr] = currentVertex
                    exploredNodes.append(nbr)
                    #print("ex")
'''
##            break


 
