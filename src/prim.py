#sorry this is such garbage rn, really struggling here...
from pythonds.graphs import PriorityQueue, Graph, Vertex

def prim(Graph):
    pq = PriorityQueue()
    source = #how are we defining the source??????
    source.setDistance(0)
    for n in Graph:
        n.setDistance(sys.maxsize)
        n.setPred(None)
    pq.buildHeap([n.getDistance(), n) for n in Graph])

    while pq:
        currNode = pq.delMin() #get min value from priority queue
        for adj in currNode.getConnections(): #for all adjacacent nodes to the current node
            weight = currNode.getWeight(adj) #weight of adj node
            if adj in pq: #if it is in the pq ie not already in the mst
                if weight < adj.getDistance(): #new weight is minimum
                    adj.setPred(currNode) #set the previous node of adjacent node
                    adj.setDistance(weight) #set weight
                    pq.decreaseKey(adj, weight) #take the adj node out of the pq
