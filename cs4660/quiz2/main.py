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
from queue import *
#from Queue import PriorityQueue
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













def BFS(start, end):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
 
#   print(32222222222222222222323332)
#   print(destn_node)
    

#   print("asasas")
#   print(visited)
#   addVertex.append(get_state(initial_node))

    # Creating Dictonary of Distances and starPredeccsor 
    starPredeccsor={}
    distanceFrom = {} 
    #Calculating distance and predecossr of initial Node
    #distanceFrom[initial_node] =0
    #starPredeccsor[initial_node['id']] = None

    v={}
#   startExploringNodes=[]
#   startExploringNodes.append(get_state(start))
#   print(startExploringNodes)
#   a23 = get_state(initial_node)

    initial_node = get_state(start)
    dest_node = get_state(end)




#   rer=get_state(initial_node)
#   print(rer["neighbors"])
#   print(rer["location"]["name"])
#   print(rer)
#   print(get_state(initial_node))


    addVertex=[initial_node] 

 
    visited = [initial_node['id']] 


    while len(addVertex)>0:
        currentVertex = addVertex.pop(0)
        for nbr in currentVertex['neighbors']:
            toNode = get_state(nbr['id'])
            distanceTo = transition_state(currentVertex['id'], toNode['id'])
            
            if toNode['id'] == dest_node['id']:
                print("Inside IF")
                visited.append(toNode['id'])
                starPredeccsor[toNode['id']] = currentVertex['id']
                distanceFrom[toNode['id']] = distanceTo
                direction = []
                while dest_node['id'] in starPredeccsor:
                    direction.append(distanceFrom[dest_node['id']])
                    dest_node['id'] = starPredeccsor[dest_node['id']]

                hp = 0
                for p in direction:
                    
                    prev_node = get_state(initial_node['id'])
                    next_id = p['id']
                    hp = hp + p['event']['effect']

                    print ("%s(%s):%s(%s): %i" % (prev_node['location']['name'], initial_node['id'], p['action'], p['id'], p['event']['effect']))
                    initial_node['id'] = next_id
                print("   ")
                print("\nTotal HP Resulted For BFS As : %i" % hp)
                print("   ")
            
                return



            elif toNode['id'] not in visited:
             #   print("Inside Elfse If")
                visited.append(toNode['id'])
                starPredeccsor[toNode['id']] = currentVertex['id']
                distanceFrom[toNode['id']] = distanceTo
                addVertex.append(toNode)
            else:
                continue






    
def finder(node_id, starPredeccsor, distanceFrom,start):
    direction = []
    while node_id in starPredeccsor:
        direction.append(distanceFrom[node_id])
        node_id = starPredeccsor[node_id]
    #

    prev_id = start
    hp1 = 0
    for i in direction:
        prev_node = get_state(prev_id)
        next_id = i['id']
        hp1 = hp1+ i['event']['effect']
        print ("%s(%s):%s(%s): %i" % (prev_node['location']['name'], prev_id, i['action'], i['id'], i['event']['effect']))
        prev_id = next_id
    print("\nTotal HP Resulted For Dijsktra Search As:  %i" % hp1)

	




     

       





def Dijkstra_Search(initial_node,dest_node):
   


#   print(32222222222222222222323332)
#   print(destn_node)

    # Creating Dictonary of Distances and starPredeccsor 
    starPredeccsor={}
    distance = {} 


    # list to store the list of nodes visited
    visited= []

    addVertex = PriorityQueue()

    addVertex.put((0, initial_node))

    distance[initial_node] =0
    distanceFrom = {}
    
    #visited = []


    
    exploredNodes = []
   # distance[initial_node] = 0
   # starPredeccsor[initial_node] = None
    starPredeccsor2 ={}
    exploredNodes.append((0,initial_node))

    while not addVertex.empty():

        toNode =get_state(addVertex.get()[1])

        #print(45555555555454)
        #print(toNode)


        visited.append(toNode['id'])
        #(555)
        for nbr in toNode['neighbors']:
        #	print(nbr)
            start21 = transition_state(toNode['id'], nbr['id'])
            # print(inside For)
            x = distance[toNode['id']] + int(start21['event']['effect'])

            if ((nbr['id'] not in visited) and ((nbr['id'] not in distance) or (x > distance[nbr['id']]))):
                # print(Inside If)
                addVertex.put((-x, nbr['id']))
                distance[nbr['id']] = x
                #print(2222222)
                starPredeccsor[nbr['id']] = toNode['id']
                distanceFrom[nbr['id']] = start21
                #print(distanceFrom)

    finder(dest_node, starPredeccsor, distanceFrom, initial_node)    


 




    











if __name__ == "__main__":

    # Your code starts here
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    #print(empty_room)
    #print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
    css={}
    test =[]


    #Finding shortest path  usinf BFS And storing it into list

    initial_node =('7f3dc077574c013d98b2de8f735058b4')
    destn_node = ('f1f131f647621a4be7c71292e79613f9')
    room = transition_state(empty_room['id'], empty_room['neighbors'][0]['id'])
    #print(333333333333333333)
    css[0] = readFile

    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')

    dest_room = get_state('f1f131f647621a4be7c71292e79613f9')

    print("\n BFS Path")
    BFS(initial_node,destn_node)

    print("\n Dijsktra path")

    Dijkstra_Search(initial_node,destn_node)