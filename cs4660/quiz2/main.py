"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
import codecs

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.
    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    reader = codecs.getreader("utf-8")
    response = json.load(reader(urlopen(req, jsondataasbytes)))
    return response

def readFile():
    f = open("http://192.241.218.106:9000/secret", encoding='utf-8')
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
    #print(graph)
    return graph


    pass






if __name__ == "__main__":

    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    #print(empty_room)
    print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
    css={}
    test =[]


    #Finding shortest path  usinf BFS And storing it into list

    initial_node ='7f3dc077574c013d98b2de8f735058b4'
    destn_node = 'f1f131f647621a4be7c71292e79613f9'
    room = transition_state(empty_room['id'], empty_room['neighbors'][0]['id'])
    print(333333333333333333)
    css[0] = readFile
    print(css.keys())
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
    v={}

    name    = "a" 

    x = {}

    
    while (len(visited)>0):
        currentVertex = visited.pop(0)
        
        for nbr in get_state(currentVertex):
            
            if nbr not in addVertex:
                
                visited.append(nbr)
                print(232323)
                v=(transition_state(currentVertex,nbr))

#                print(v.get('id'))
#                name= v.get('id')
                key = v.get('id')

                if len(key)==0:
                    d=0
                else:
                    d=len(key)
                
                distance[nbr] = distance[currentVertex]+ d
                starPredeccsor[nbr]= currentVertex
                addVertex.append(nbr)
                
        if destn_node in addVertex:
            #print("I breaked")
            break
    list =[]

    while starPredeccsor[destn_node] is not None:
        list = [graph.get_edge(starPredeccsor[destn_node], destn_node)] + list
   #     print (list)
        destn_node= starPredeccsor[destn_node]
    #print(list)





# Dijkstra Algorithm

    



    exploredNodes =[]
    startExploringNodes ={}
    

    # copyOfExploredNodes will check if the node was initilly considered for dijkstra or not
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

    x1=destn_node
    d1 =-1


    #a=graph.distance(initial_node,dest_node)
    #a =(graph.size())
  

    while len(exploredNodes)>0:
        currentVertex = max(startExploringNodes, key=startExploringNodes.get)#_edge)
        #visited.pop(currentVertex)
        

        

        startExploringNodes.pop(currentVertex)
        exploredNodes.append(currentVertex)
        copyOfExploredNodes.append(currentVertex)




        for nbr in get_state(currentVertex):
            #print("Inside For")
            if nbr in copyOfExploredNodes:
                #print("Inside If")
                break
            else:

                #print(distance[nbr])

                if( (nbr not in startExploringNodes and nbr not in exploredNodes) or (distance[nbr]>distance[currentVertex]+transition_state(currentVertex,nbr))):
                    copyOfExploredNodes.append(nbr)

                    print(232323)
                    v=(transition_state(currentVertex,nbr))
                    key = v.get('id')
                    if len(key)==0:
                        d1=0
                    else:
                        d1=len(key)



                    startExploringNodes[nbr] =distance[currentVertex]+ d1
                    distance[nbr] = distance[currentVertex]+ d1
                    starPredeccsor[nbr] = currentVertex
                    exploredNodes.append(nbr)
                    #print("ex")

        if destn_node in exploredNodes:
            break




    list1 =[]

    while starPredeccsor[x1] is not None:

        list1 = [graph.get_edge(starPredeccsor[x1], x1)] + list1
        x= starPredeccsor[x1]




  #  return list


                

       





