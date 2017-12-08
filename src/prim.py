from pythonds.graphs import PriorityQueue, Graph, Vertex

def prim(Graph, source):
    pq = PriorityQueue()
    source.setDistance(0)
    total_weight = 0
    for n in Graph:
        n.setDistance(sys.maxsize)
        n.setPred(None)
    pq.buildHeap([n.getDistance(), n) for n in Graph]) #(distance, node)

    while (pq):
        currNode = pq.delMin() #get min value from priority queue
        for adj in currNode.getConnections(): #for all adjacacent nodes to the current node
            weight = currNode.getWeight(adj) #weight of adj node
            if adj in pq: #if it is in the pq ie not already in the mst
                if weight < adj.getDistance(): #new weight is minimum
                    adj.setPred(currNode) #set the previous node of adjacent node
                    adj.setDistance(weight) #set weight
                    total_weight += weight
                    pq.decreaseKey(adj, weight) #take the adj node out of the pq
return total_weight
