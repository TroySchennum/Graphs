class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")
def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Build edges in reverse
        graph.add_edge(pair[1], pair[0])
    # Do a BFS (storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        # If the path is longer or equal and the value is smaller, or if the path is longer)
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor


# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)

# class Graph:

#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         """
#         Add a vertex to the graph.
#         """
#         self.vertices[vertex_id] = set()

#     def add_edge(self, v1, v2):
#         """
#         Add a directed edge to the graph.
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise IndexError("nonexistent vertex")

#     def get_neighbors(self, vertex_id):
#         """
#         Get all neighbors (edges) of a vertex.
#         """
#         return self.vertices[vertex_id]

# def earliest_ancestor(ancestors, starting_node):

#     g = Graph()

#     for pair in ancestors:
#         g.add_vertex(pair[0]) # add parent node
#         g.add_vertex(pair[1]) # add child node
#         g.add_edge(pair[1], pair[0]) # connect parent and child node
#         print(g.vertices)

#     q = Queue()
#     q.enqueue([starting_node])

#     oldest_ancestor = -1 # this is what is returned if node has no parents
#     max_path_length = 1

#     while q.size() > 0:
#         path = q.dequeue()

#         vertex = path[-1] #[-1] = the last position in the list

        
#         # If there is more than one ancestor tied for "earliest", return the one # with the lowest numeric ID
#         # If the input individual has no parents, function returns 1

#         if len(path) >= max_path_length and vertex < oldest_ancestor: 
#             oldest_ancestor = vertex
#             max_path_length = len(path)

#         elif len(path) > max_path_length:
#             oldest_ancestor = vertex
#             max_path_length = len(path)   
            
#         for neighbor in g.vertices[vertex]:
#             path_copy = list(path)
#             path_copy.append(neighbor)
#             q.enqueue(path_copy)

#     return oldest_ancestor
            
            
    # def earliest_ancestor(ancestors, starting_node):
    # # Build the graph
    # graph = Graph()
    # for pair in ancestors:
    #     graph.add_vertex(pair[0])
    #     graph.add_vertex(pair[1])
    #     # Build edges in reverse
    #     graph.add_edge(pair[1], pair[0])
    # # Do a BFS (storing the path)
    # q = Queue()
    # q.enqueue([starting_node])
    # max_path_len = 1
    # earliest_ancestor = -1
    # while q.size() > 0:
    #     path = q.dequeue()
    #     v = path[-1]
    #     # If the path is longer or equal and the value is smaller, or if the path is longer)
    #     if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
    #         earliest_ancestor = v
    #         max_path_len = len(path)
    #     for neighbor in graph.vertices[v]:
    #         path_copy = list(path)
    #         path_copy.append(neighbor)
    #         q.enqueue(path_copy)
    # return earliest_ancestor
       
            
            
           # return path
       # if v not in visited:
          #  visited.add(v)
          #  for neighbor in self.vertices[v]:
             #   path_copy = list(path)
              #  path_copy.append(neighbor)
              #  q.enqueue(path_copy)



# create a graph
# take a starting node and see which node is the furthest away
# bfs
# if count is the same for two items return the smaller value
# take in length of paths. choose longest path. assign last node as == last. 
# return last of longest path/paths
