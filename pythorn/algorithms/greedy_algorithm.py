"""
Author : Robin Singh

Programs List:
1 . Activity Selection Problem 
2 . Dijkstra's Algorithm
3 . Egyptian Fraction
4 . Fractional Knapsack
5 . Minimum Coin Exchange Problem
6 . Kruskals Algorithm
7 . Prims Algorithm

"""

import inspect
import math
import operator


class ActivitySelection(object):
    """
    Implementation Of Activity Selection Problem Using Greedy Approch

    here we have n activities with their start and finish times. Select the maximum number of activities
    that can be performed by a single person, assuming that a person can only work on a single activity at a time

    """

    def __init__(self, start=None, finish=None):
        """
        :param start: array for start values
        :param start: array for finish values
        """

        self.start = start
        self.finish = finish

    def activity_selection(self):
        """
        activity selection main function

        :prints: Prints a maximum set of activities that can be done by a single person, one at a time
        """
        print("Following Activities Are selected :")
        j = 0
        print("Index\tStart\tFinish")
        print(f"{j}\t{self.start[j]} -->\t{self.finish[j]}")
        for i in range(1, len(self.start)):
            if self.start[i] >= self.finish[j]:
                print(f"{i}\t{self.start[i]} -->\t{self.finish[i]}")
                j = i

    @staticmethod
    def time_complexity():
        """

        :return: time complexity
        """
        return "Time Complexity : O(n log n) time if input activities may not be sorted ,"\
            "Time Complexity : O(n) time when it is given that input activities are always sorted"

    @staticmethod
    def get_code():
        """

        :return:source code
        """
        return inspect.getsource(ActivitySelection)


class Dijkstra(object):
    """
    Implementation of Dijkstra's Algorithm

    Dijkstra’s algorithm finds the shortest path in a weighted graph containing only positive edge weights from a single source
    """

    def __init__(self, start, finish, graph):
        """
        :param start: start vertex
        :param start: end vertex
        :param graph:  weighted graph containing only positive edge weights from a single source
        """

        self.start = start
        self.finish = finish
        self.graph = graph

    def dijkstra(self):
        """
        Calculates the optimal path from start to end on the graph

        :prints: prints the optimal path if exists
        """
        shortest_dist = {}
        track_prev_nodes = {}
        not_visited_nodes = self.graph
        infinity = 1000000000000  # infinity can be considerd a very large number
        path = []  # going to trace our journey back to the source node

        for node in not_visited_nodes:
            shortest_dist[node] = infinity
        shortest_dist[self.start] = 0

        while not_visited_nodes:
            min_dist_node = None

            for node in not_visited_nodes:
                if min_dist_node is None:
                    min_dist_node = node

                elif shortest_dist[node] < shortest_dist[min_dist_node]:
                    min_dist_node = node

            path_options = self.graph[min_dist_node].items()

            for adj_node, weight in path_options:
                if weight + shortest_dist[min_dist_node] < shortest_dist[adj_node]:
                    shortest_dist[adj_node] = weight + \
                        shortest_dist[min_dist_node]
                    track_prev_nodes[adj_node] = min_dist_node

            not_visited_nodes.pop(min_dist_node)

        curreentNode = self.finish

        while curreentNode != self.start:

            try:
                path.insert(0, curreentNode)
                curreentNode = track_prev_nodes[curreentNode]
            except KeyError:
                print("We Can't Reach To The Destination Node")
                break

        path.insert(0, self.start)
        if shortest_dist[self.finish] != infinity:
            print(
                f"Single Source Shortest Path :{path} --> COST : {shortest_dist[self.finish]}")

    @staticmethod
    def time_complexity():
        """

        :return: time complexity
        """
        return "Time Complexity  : O((E+V)Log(V))"

    @staticmethod
    def get_code():
        """

        :return:source code
        """
        return inspect.getsource(Dijkstra)


class EgyptianFraction(object):
    """
    Implementation of Eqyption Fraction

    Every positive fraction can be represented as sum of unique unit fractions

    A fraction is unit fraction if numerator is 1 and denominator is a positive integer, for example 1/3 is a unit fraction

    Such a representation is called Egyptian Fraction as it was used by ancient Egyptians
    """

    def __init__(self, numerator, denominator):
        """
        :param numerator: numerator value
        :param denominator:  denominator value
        """
        self.numerator = numerator
        self.denominator = denominator

    def egyptian_fraction(self):
        """
        :prints: prints the value of numnerator/denominator
        """
        ef = []
        while self.numerator != 0:

            x = math.ceil(self.denominator / self.numerator)  # Main
            ef.append(x)
            self.numerator = x * self.numerator - self.denominator
            self.denominator = self.denominator * x
        for i in range(len(ef)):
            if i != len(ef) - 1:
                print(f" 1/{ef[i]} +", end=" ")

            else:
                print(f"1/{ef[i]}", end=" ")

    @staticmethod
    def time_complexity():
        """

        :return: time complexity
        """
        return "No Data"

    @staticmethod
    def get_code():
        """

        :return: source code
        """
        return inspect.getsource(EgyptianFraction)


class FractionalKnapsack(object):

    """
    Implementation Of Fractional Knapsack

    - Given weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack

    - n Fractional Knapsack, we can break items for maximizing the total value of knapsack

    - This problem in which we can break an item is also called the fractional knapsack problem

    - An efficient solution is to use Greedy approach. The basic idea of the greedy approach is to calculate
    the ratio value/weight for each item and sort the item on basis of this ratio. Then take the item with

    - the highest ratio and add them until we can’t add the next item as a whole and at the end add the next item as much as we can

    - Which will always be the optimal solution to this problem
    """

    def __init__(self, weight, profit, capacity):
        """

        :param weight: list of weights of items in the knapsack
        :param profit: list of profits of items in the knapsack
        :param capacity: maximum capacity of knapsack

        """

        self.weight = weight
        self.profit = profit
        self.capacity = capacity

    def fractional_knapsack(self):
        """
        :prints: prints maximum total value of the knapsack
        """
        n = len(self.profit)
        new_list = []
        for i in range(n):
            new_list.append([self.profit[i], self.weight[i],
                             self.profit[i]*1.0/self.weight[i]])

        new_list = sorted(new_list, reverse=True, key=operator.itemgetter(2))
        max_profit = 0
        fractional_val = 0
        table_profit = []
        table_weight = []
        ratio_table = []

        for i in range(n):
            if self.capacity > 0 and new_list[i][1] < self.capacity:
                self.capacity -= new_list[i][1]
                max_profit += new_list[i][0]
                table_profit.append(new_list[i][0])
                table_weight.append(new_list[i][1])
                ratio_table.append(new_list[i][2])

            else:
                fractional_val = i
                table_profit.append(new_list[i][0])
                table_weight.append(new_list[i][1])
                ratio_table.append(new_list[i][2])

                break

        if self.capacity > 0:
            max_profit += self.capacity * \
                (new_list[fractional_val][0])/(new_list[fractional_val][1])

        o = len(table_profit)
        print("Fractional Knapsack")
        for x in range(o):
            print(
                f"Profit :{table_profit[x]}\t\tWeight  : {table_weight[x]}\t\tProfit/Weight : {ratio_table[x]}")
        print("Total Profit :", max_profit)

    @staticmethod
    def time_complexity():
        """


        :return: time complexity
        """
        return "Time Complexity  : O(nLogn)"

    @staticmethod
    def get_code():
        """

        :return: source code
        """
        return inspect.getsource(FractionalKnapsack)


class MinimumCoinExchange(object):
    """
    Implementation of Minimum Coin Exchange Problem

    Here we have a value V, if we want to make a change for V Rs, and we have an infinite supply of each of the denominations in Indian currency, i.e., we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 2000} valued coins/notes

    Then what is the minimum number of coins or notes are needed to make the change
    """

    def __init__(self, money):
        """
        :param money: Money to be exchanged
        """
        self.money = money

    def minimum_coin_exchange(self):
        """
        :prints: prints all denominations change 
        """
        Notes_coin = [.50, 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        exchanges = []
        i = len(Notes_coin)-1
        while i >= 0:
            while self.money >= Notes_coin[i]:
                self.money = self.money - Notes_coin[i]
                exchanges.insert(0, Notes_coin[i])

            i -= 1
        for i in range(0, len(exchanges)):
            print(f" {exchanges[i]} ", end="")

    @staticmethod
    def time_complexity():
        """

        :return: time complexity
        """
        return "Time Complexity: O(N*logN)."

    @staticmethod
    def get_code():
        """

        :return:source code
        """
        return inspect.getsource(MinimumCoinExchange)


class Edge(object):
    """
    for storing Source , destination and weight of the edge
    """

    def __init__(self, s, d, w):
        self.s = s
        self.d = d
        self.w = w


class Kruskal(object):

    """
    Implementation of Kruskal's Algorithm,

    Minimum Cost Spanning Tree of a given connected, undirected and weighted graph

    It is a greedy algorithm in graph theory as it finds a minimum spanning tree for a connected weighted graph adding increasing cost at each step
    """

    def __init__(self, num_nodes=None, edgelist=None):
        """
        :param num_nodes: Number of nodes present
        :param edgelist: edge list with weight
        """
        self.num_nodes = num_nodes
        self.edgelist = edgelist
        self.parent = []
        self.rank = []

        # MCST stores edges of the minimum cost spanning tree
        self.mcst = []

    def _Parent(self, node):
        """
        for finding the parent of the given node
        """

        if self.parent[node] == node:
            return node
        return self._Parent(self.parent[node])

    def kruskal(self):
        """
        main function

        :prints: prints minimum cost of the given graph
        """

        self.edgelist.sort(key=lambda Edge: Edge.w)

        self.parent = [None] * self.num_nodes
        self.rank = [None] * self.num_nodes

        for n in range(self.num_nodes):
            # every node in the beginning is parent of itself
            self.parent[n] = n
            self.rank[n] = 0
            # in the beginning rank of every node is 0

        for edge in self.edgelist:
            r1 = self._Parent(edge.s)
            r2 = self._Parent(edge.d)

            # if parents of source and destination are not in same subset then add that edge in the MCST
            if r1 != r2:
                self.mcst.append(edge)
                if self.rank[r1] < self.rank[r2]:
                    self.parent[r1] = r2
                    self.rank[r2] += 1
                else:
                    self.parent[r2] = r1
                    self.rank[r1] += 1

        print("MCST")
        print(f"SOURCE  DESTINATION  WEIGHT")
        cost = 0
        for edge in self.mcst:
            print(f"{edge.s}    -->  {edge.d}     -->     {edge.w}")

            cost += edge.w
        print("\nMCST(MINIMUM COST) : ", cost)

    @staticmethod
    def time_complexity():
        """

        :return: time complexity
        """
        return "Time Complexity  : O(ElogE) or O(ElogV)"

    @staticmethod
    def get_code():
        """

        :return: source code
        """
        return inspect.getsource(Kruskal)

    # Input Example
    # Make Edges first with source,destination and weight
    # num_nodes = 8
    # A = Edge(1, 6, 10)
    # B = Edge(3, 4, 12)
    # C = Edge(7, 2, 14)
    # D = Edge(2, 3, 16)
    # E = Edge(7, 4, 18)
    # F = Edge(4, 5, 22)
    # G = Edge(5, 7, 24)
    # H = Edge(5, 6, 25)
    # I = Edge(1, 2, 28)
    # g1 = Kruskal(num_nodes, [A, B, C, D, E, F, G, H, I])
    # g1.kruskal()


class Node(object):
    """
    :param source: initializing a Node
    """

    def __init__(self, source=None):
        self._num = source


class Prims(object):
    """
    Implementation of prims algorithm

    In Prim's Algorithm, a conquered territory (initialized with any start vertex)
    is chosen in which we keep adding the vertices as we go through the algorithm
    To get the minimum spanning tree, we keep adding vertices to the conquered edges
    with the greedy paradignm that we select the edge with the minimum weight of all the edges starting the
    conquered territory and ending at the unconquered territory. The end of the minimum weight edge thus chosen is
    then added to the conquered territory and removed from the unconquered territory. In such a way,
    we go on till the conquered territory spans all the vertices of the graph
    """

    def __init__(self, source, graph):
        """
        :param source: Source node
        :param graph: Graph
        """
        self.source = source
        self._list = graph

    def prims(self):
        """
        :prints: prints MCST for the given graph
        """
        MCST_Cost = 0
        queue = {Node(self.source): 0}
        added = [0]*len(self._list)

        while queue:
            # choosing the adjancent Node having the minimum cost
            node = min(queue, key=queue.get)
            cost_Node = queue[node]
            # Delete that Node from the Dict
            del queue[node]

            if added[node._num] == 0:  # If node is not Visited
                MCST_Cost += cost_Node

                added[node._num] = True  # Mark Visited

                print(f"{node._num} -->  ", end=" ")

                for n in self._list[node._num]:
                    adjancent_node = n[0]
                    adjancent_cost = n[1]
                    if added[adjancent_node] == 0:
                        queue[Node(adjancent_node)] = adjancent_cost
        print("Cost : ", MCST_Cost)

    @staticmethod
    def time_complexity():
        """

        :return: time complexity
        """
        return "Time Complexity : O(ElogV)"

    @staticmethod
    def get_code():
        """

        :return:source code
        """
        return inspect.getsource(Prims)
