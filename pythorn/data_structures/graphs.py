"""
Author : Robin Singh

Programs List : 
1 . Adjancey List with Node Class
2 . Adjancey Matrix
3 . Breath First Search
4 . Depth First Search
5 . Topological Sort

"""

import inspect


class Node(object):

    """
    Node class for creating a node

    """

    def __init__(self, value, next='*'):
        """
        :param value: given value assigned to node
        :param next: default value given to node's next
        """
        self.value = value
        self.next = next

    def get_Next(self):
        """
        function for getting the next node
        """
        return self.next

    def get_Value(self):
        """
        function for getting the value of current node
        """
        return self.value

    def set_Next(self, next):

        self.next = next

    def set_Value(self, value):
        """
        function for setting the value
        """
        self.value = value


class AdjanceyList(object):
    """
    Adjancey list implementation
    """

    def __init__(self, number_of_nodes):
        """
        :param number_of_nodes: Number of nodes to set
        :param nodes: empty array
        :param create_nodes: for creating given number of nodes
        """
        self.number_of_nodes = number_of_nodes
        self.nodes = []
        self.create_nodes()

    def create_nodes(self):
        """
        function for creating nodes
        """
        for n in range(self.number_of_nodes):
            self.nodes.append(0)

    def last_node(self, first_node):
        """
        function for getting the last node
        """
        node = first_node
        while not node.get_Next() == '*':
            node = node.get_Next()
        return node

    def add_edge(self, node1, node2):
        """
        function for adding new edges 

        :param node1: from vertex (source)
        :param node2: to vertex (destination)
        """
        if self.nodes[node1-1] == 0:
            # Here new_node is creating a new node with help of Node class
            new_node = Node(node2-1)
            self.nodes[node1-1] = new_node
        else:
            new_node = Node(node2-1)
            _last_node = self.last_node(self.nodes[node1-1])
            _last_node.set_Next(new_node)

        if self.nodes[node2-1] == 0:
            new_node = Node(node1-1)
            self.nodes[node2-1] = new_node
        else:
            new_node = Node(node1-1)
            _last_node = self.last_node(self.nodes[node2-1])
            _last_node.set_Next(new_node)

    def print_adjancey(self, node, node_No):
        """

        :prints: prints adjancey list for a specific node
        """
        if node == 0:
            print('node {} :No Edges Present'.format(node_No+1))
        else:
            op = ''
            while not node == '*':
                op = op+str(node.get_Value()+1)+' '
                node = node.get_Next()
            print('node {} -> {}'.format(node_No+1, op))

    def print_list(self):
        """
        function for printing all the node's adjancey list
        """
        for nodes in range(0, self.number_of_nodes):
            self.print_adjancey(self.nodes[nodes], nodes)

    @staticmethod
    def get_code():
        """


        :return: source code
        """
        return inspect.getsource(AdjanceyList)

    @staticmethod
    def time_complexity():
        """


        :return: time complexity

        """
        return "Time Complexity : O(|V|+|E|)"


class AdjanceyMatrix(object):
    """
    Adjancey Matrix Implementation


    """

    def __init__(self, no_of_verices):
        """
        :param no_of_vertics: given numbe of nodes or vertices
        :param matrix: empty array to store edges in the form of 0/1
        :param make_matrix: for making matrix 
        """

        self.Nodes = no_of_verices
        self.matrix = []
        self.make_matrix()

    def make_matrix(self):
        """
        function for making matrix of NxN. where n is the number of vertices
        """
        for i in range(self.Nodes):
            v = []
            for i in range(self.Nodes):
                v.append(0)
            self.matrix.append(v)

    def add_edge(self, node1, node2):
        """
        function for adding an edge 

        :param node1: vertex 1 (source)
        :param node2: vertex 2 (destination)
        """
        self.matrix[node1-1][node2-1] = 1
        self.matrix[node2-1][node1-1] = 1

    def print_matrix(self):
        """
        function for printing the matrix
        """
        for row in self.matrix:
            print(row)
        return print(row)

    @staticmethod
    def get_code():
        """

        :return: source code
        """
        return inspect.getsource(AdjanceyMatrix)

    @staticmethod
    def time_complexity():
        """


        :return: time complexity

        """
        return "Time Complexity : O(N^2)"


class BFS(object):
    """
    BFS implementation with adjancey list

    """

    def __init__(self, graph, start):
        """
        :param graph: adjancey list
        :param start: start vertex

        """

        self.list = graph
        self.start = start

    def bfs(self):
        """
        :return: BFS path
        """
        path = []
        queue = [self.start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in path:

                path.append(vertex)
                queue.extend(self.list[vertex])
        return path

    @staticmethod
    def get_code():
        """
        :return: source code
        """
        return inspect.getsource(BFS)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """
        return 'Time Complexity : O(V + E)'\
            "V = vertex  , E = edges"


class DFS(object):
    """
    DFS implementation with adjancey list

    """

    def __init__(self, graph, start, path=[]):
        """
        :param graph: adjancey list
        :param start: start vertex

        """

        self.list = graph
        self.start = start
        self.path = path

    def dfs(self):
        """
        :return: DFS path
        """

        if self.start not in self.path:
            self.path.append(self.start)
            for n in self.list[self.start]:

                new_dfs = DFS(self.list, n, self.path)
                new_dfs.dfs()
        return self.path

    @staticmethod
    def get_code():
        """
        :return: source code
        """
        return inspect.getsource(DFS)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """
        return 'Time Complexity : O(V + E)'\
            "V = vertex  , E = edges"


class TopologicalSort():
    """
    Topological Sort Implementation
    """

    def __init__(self, vertices):
        """
        :param vertices: Number of vertices

        """
        self.vertex = {}
        self.count = vertices

    def print_list(self):
        """
        function for printing graph
        """
        for i in self.vertex.keys():

            print(i, "Vertex :", ' -> ',
                  ' -> '.join([str(j) for j in self.vertex[i]]))

    def add_edge(self, node1, node2):
        """
        :param node1: from vertex (source)
        :param node2: to vertex (destination)     
        """

        if node1 in self.vertex.keys():
            self.vertex[node1].append(node2)
        else:

            self.vertex[node1] = [node2]
            self.vertex[node2] = []

    def topological_Sort(self):
        visited = [0] * self.count

        stack = []
        for vertex in range(self.count):

            if visited[vertex] == False:
                self.topo(vertex, visited, stack)

        print('--> '.join([str(i) for i in stack]))

    def topo(self, vertices, visited, s):

        visited[vertices] = True

        try:
            for adj_node in self.vertex[vertices]:
                if visited[adj_node] == False:
                    self.topo(adj_node, visited, s)
        except KeyError:
            return

        s.insert(0, vertices)

    @staticmethod
    def get_code():
        """

        :return: source code
        """
        return inspect.getsource(TopologicalSort)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """

        return "Time Complexity: O(V+E)"
