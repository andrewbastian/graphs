"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() # hold edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("no vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()

        queue.enqueue(starting_vertex) # load starting value into the stack

        while queue.size() > 0:  # while queue is not empty
            vertex = queue.dequeue()  # remove the node at the front and set this node as our current vertex/node
            if vertex not in visited:  # if we have not visited the vertex
                visited.add(vertex)  # add the vertex to `visited`
                print(vertex)
                for neighbors in self.get_neighbors(vertex):  # get the neighboring node
                    queue.enqueue(neighbors)  # add the `neighbor` node to the queue

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()  # create a stack
        visited = set()  # set tracking visited nodes

        stack.push(starting_vertex)  # push the starting node to the stack

        while stack.size() > 0:  # while the stack is empty
            vertex = stack.pop()  # add the top node to the stack
            if vertex not in visited:  # if the node has not be visited yet
                visited.add(vertex) # add the node to visited
                print(vertex)
                for neighbor in self.get_neighbors(vertex):  # for each neighbor of the current node
                    stack.push(neighbor)  # add the neighbor node to the stack

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()  # create set for tracking visited nodes

        def dft(vertex):  # new depth first order function with node args
            if vertex in visited:  # if the node has been visited, do nothing
                return
            else:
                visited.add(vertex)  # if it has not been visited add the current node to `visited`
                print(vertex)
            neighbor = self.get_neighbors(vertex)  # create a var that is the neighbors of the current node

            for n in neighbor:  # for the all the neighbors of the current node
                dft(n)  # run the neigbor back through this function

        dft(starting_vertex)  # pass starting node for recursive loop

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue() 

        queue.enqueue([starting_vertex])  # load starting nodes into queue

        visited = set()

        while queue.size() > 0:  # while the queue is empty
            vertex = queue.dequeue()  # create a var and remove the current node from the queue

            last_vertex = vertex[-1] # create a var that finds the last node

            if last_vertex in visited:  # if the last node has been visited, do nothing
                continue
            else:
                visited.add(last_vertex)  # if the node has not been visited add it to `visited`

            for neighbor in self.get_neighbors(last_vertex):
                next_path = vertex[:]
                next_path.append(neighbor)

                if neighbor is destination_vertex:
                    return next_path

                else:
                    queue.enqueue(next_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()

        stack.push([starting_vertex])

        visited = set()

        while stack.size() > 0:
            vertex = stack.pop()

            last_vertex = vertex[-1]

            if last_vertex in visited:
                continue
            else:
                visited.add(last_vertex)

            for neighbor in self.get_neighbors(last_vertex):
                next_path = vertex[:]
                next_path.append(neighbor)

                if neighbor is destination_vertex:
                    return next_path

                else:
                    stack.push(next_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited = set()

        def dfs(path):
            last_path = path[-1]

            if last_path in visited:
                return None

            else:
                visited.add(last_path)

            if last_path is destination_vertex:
                return path

            for neighbor in self.get_neighbors(last_path):
                next_path = path[:]
                next_path.append(neighbor)

                found_path = dfs(next_path)

                if found_path:
                    return found_path

            return None

        return dfs([starting_vertex])

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
