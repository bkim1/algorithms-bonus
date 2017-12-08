'''Package to find the minimum spanning tree using Boruvka's Algorithm

Graph represented as a dict:

Key: Value
Node: [(u, v, w)]
'''

def boruvka(graph):
    '''Boruvka's Minimum Spanning Tree Algorithm'''
    # Process graph to get list of all edges
    edges = []

    for node in graph:
        for u, v, w in graph[node]:
            edges.append((u, v, w))

    # Stores the roots & rankings for all nodes in graph
    roots = []
    rank = []

    # Stores the minimum weight edges for the roots
    min_weights = []

    # Initialize other variables
    total_weight = 0
    num_trees = len(graph)

    # Initialize the roots, rank, & min_weights arrays
    # Not initializing through list comprehension to avoid multiple
    # loops through the original graph
    for node in graph:
        roots.append(node)
        rank.append(0)
        min_weights.append(-1)

    # Loop through until there is only one tree left
    # Follows pseudo-code from lecture
    while num_trees > 1:
        # Find the minimum edge weights for each root
        # Loops through all edges in graph
        for u, v, w in edges:
            root_u = find_root(roots, u)
            root_v = find_root(roots, v)

            # Only continue if the roots aren't part of the same tree
            if root_u != root_v:
                # Update the min_weights if necessary
                # Similar to pseudo code for updating the 'cheapest' edges
                if min_weights[root_u] != -1 or min_weights[root_u] < w:
                    min_weights[root_u] = (u, v, w)
                if min_weights[root_v] != -1 or min_weights[root_v] < w:
                    min_weights[root_v] = (u, v, w)

        # Merge graphs together if necessary
        for node in graph:
            # Check if there's an edge to connect together
            if min_weights[node] != -1:
                u, v, w = min_weights[node]
                root_u = find_root(roots, u)
                root_v = find_root(roots, v)

                # The two trees need to be merged
                if root_u != root_v:
                    merge_trees(roots, rank, root_u, root_v)
                    total_weight += w
                    num_trees -= 1

        # Reset min_weights for roots
        min_weights = [-1 for node in graph]
    
    return total_weight






def find_root(roots, i):
    '''Finds the root of a set'''
    if roots[i] == i:
        return i
    return find_root(roots, roots[i])

def merge_trees(roots, rank, set_x, set_y):
    '''Merges two roots together by rank'''
    # Find the roots of both sets
    root_x = find_root(roots, set_x)
    root_y = find_root(roots, set_y)

    # Merge the two roots based on their rank
    # Higher rank has precedence
    if rank[root_x] < rank[root_y]:
        roots[root_x] = root_y
    elif rank[root_y] < rank[root_x]:
        roots[root_y] = root_x
    else:
        roots[root_y] = root_x
        rank[root_x] += 1