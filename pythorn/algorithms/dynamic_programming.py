"""
Author : Robin Singh

Programs List :

1 . Bellman Ford
2 . Floyd Warshall
3 . Longest Common Subsequence
4 . Coin Change Problem 1
5 . Coin Change Problem 2
6 . Subset Sum

"""

import inspect
INF = 9999999999999


class BellmanFord(object):
    """
    Implementation of Bellman Ford Algorithm(Dynamic Programming) ,
    Bellman Ford algorithm helps us find the shortest path from a vertex to all other vertices of a weighted graph.
    It is similar to Dijkstra's algorithm but it can work with graphs in which edges can have negative weights.
    """

    def __init__(self, graph, source):
        """
        :param graph: graph
        :param source: source vertex
        """
        self.graph = graph
        self.source = source

    def bellman_ford(self):
        """
        :prints: prints all the calculated distances from source and predecssor vertices
        """
        dist = dict()
        prev = dict()
        for node in self.graph:
            dist[node] = float('Inf')
            prev[node] = None
        dist[self.source] = 0

        for _ in range(len(self.graph)-1):
            for node in self.graph:
                for neighbour in self.graph[node]:
                    if dist[neighbour] > dist[node]+self.graph[node][neighbour]:
                        dist[neighbour] = dist[node] + \
                            self.graph[node][neighbour]
                        prev[neighbour] = node

        for node in self.graph:
            for neighbour in self.graph[node]:
                assert dist[neighbour] <= dist[node] + \
                    self.graph[node][neighbour], "Error,Graph Has Negative Weight Cycle"

        print("distances from source", dist), print(
            "predecssor vertices", prev)

    @staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return "Time Complexity : Best Case = O(E) , Worst Case = Average Case  = O(VE)"

    @staticmethod
    def get_code():
        """
        
        :return: source code
        """
        return inspect.getsource(BellmanFord)


class FloydWarshall(object):
    """
    Implementation of Floyd Warshall's Algorithm

    Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the pairs of vertices in a weighted graph

    This algorithm works for both the directed and undirected weighted graphs. But, it does not work for the graphs
    with negative cycles
    """

    def __init__(self, graph, vertex):
        """
        :param graph: Matrix Graph
        :param vertex: Number of vertexes
        """
        self.graph = graph
        self.vertex = vertex

    def floyd_warshall(self):
        """
        :prints: prints final matrix having shortest path between all the pairs of vertices
        """

        APSP = self.graph
        for k in range(self.vertex):
            for i in range(self.vertex):
                for j in range(self.vertex):
                    APSP[i][j] = min(APSP[i][j], APSP[i][k] + APSP[k][j])

        for i in range(self.vertex):
            for j in range(self.vertex):
                if(APSP[i][j] == INF):
                    print("INF", end=" ")
                else:
                    print(APSP[i][j], end="  ")
            print(" ")

    @staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return "Time Complexity : O(n^3)"

    @staticmethod
    def get_code():
        """
        
        :return: source code
        """
        return inspect.getsource(FloydWarshall)


class LongestCommonSubsequence(object):
    """
    Implementation Of LCS(Dynamic Approch)

    Given two sequences,here we have to find the length of longest subsequence present in both of them

    Example : 

    LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

    LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
    """

    def __init__(self, string1, string2):
        """
        :param string1: 1st string
        :param string2: 2st string
        """

        self.string1 = string1
        self.string2 = string2

    def longest_common_subsequence(self):
        """
        :prints: prints longest common subsequence with length of subsequence
        """
        arr = [['' for i in range(len(self.string2))]
               for x in range(len(self.string1))]
        for i in range(len(self.string1)):
            for j in range(len(self.string2)):
                if self.string1[i] == self.string2[j]:
                    if i == 0 or j == 0:
                        arr[i][j] = self.string1[i]
                    else:
                        arr[i][j] = arr[i-1][j-1] + self.string1[i]
                else:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1], key=len)

        s3 = arr[-1][-1]
        print(f"Lenth Of Sequence : {len(s3)}, And Sequence is : {s3}")

    @staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return "Time Complexity : O(MN)"

    @staticmethod
    def get_code():
        """
        
        :return:source code

        """
        return inspect.getsource(LongestCommonSubsequence)


class CoinChange01(object):
    """
    Implementaion of Number Of Coins Change(Number Of ways to get required Sum)
    """

    def __init__(self, sum):
        """
        :param sum: Required Sum
        """
        self.sum = sum

    def coin_change(self):
        """
        :prints: Prints no of ways to get the required sum
        """
        # Coins denominations
        coins = [2, 3, 5, 10]
        size = len(coins)
        arr = [[0 for x in range(self.sum+1)]for x in range(size+1)]
        for i in range(size + 1):
            arr[i][0] = 1
        for i in range(1, size + 1):
            for j in range(1, self.sum + 1):
                if coins[i - 1] > j:
                    arr[i][j] = arr[i - 1][j]
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i][j - coins[i - 1]]
        print(f"Number Of Ways To get Sum {self.sum} = {arr[size][self.sum]}")

    @staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return "Time Complexity : O(Coins*Sum)"

    @staticmethod
    def get_code():
        """
        
        :return: source code
        """
        return inspect.getsource(CoinChange01)


class CoinChange02(object):
    """
    Implementaion Of minimum number Of coins required to get the sum of given Value    """

    def __init__(self, sum):
        """
        :param sum: Required Sum
        """
        self.sum = sum

    def coin_change(self):
        """
        :prints: Prints no of coins to get the required sum
        """
        # Coins denominations
        coins = [2, 3, 5, 10]
        size = len(coins)
        arr = [[0 for x in range(self.sum+1)]for x in range(size+1)]
        for i in range(size + 1):
            arr[i][0] = 0
        for j in range(self.sum + 1):
            arr[0][j] = 99999999
        for i in range(1, size + 1):
            for j in range(1, self.sum + 1):
                if coins[i - 1] > j:
                    arr[i][j] = arr[i - 1][j]
                else:
                    arr[i][j] = min(
                        1 + arr[i][j - coins[i - 1]], arr[i - 1][j])
        print(
            f"Minimum Number Of Coins Required to get the sum of {self.sum} = {arr[size][self.sum]} Coins")

    @staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return "Time Complexity : O(Coins*Sum)"

    @staticmethod
    def get_code():
        """
        
        :return: source code
        """
        return inspect.getsource(CoinChange02)


class SubsetSum(object):
    """
    Implementation of Subset Sum

    Implementation of Subset Sum problem which will return true if at least one sub set exists of the required sum


    """

    def __init__(self, array, sum):
        """
        :param array: array of elements
        :param sum: Required sum
        """

        self.array = array
        self.sum = sum

    def subset_sum(self):
        """
        :prints: prints true if subset exists else prints flase
        """
        size = len(self.array)
        table = [[0 for x in range(self.sum+1)]for x in range(size+1)]  # this
        for i in range(size+1):
            table[i][0] = True

        for j in range(1, self.sum+1):
            table[0][j] = False
            for i in range(1, size+1):
                for j in range(1, self.sum+1):
                    if table[i-1][j] == True:
                        table[i][j] = True

                    else:
                        if self.array[i-1] > j:
                            table[i][j] = False
                        else:
                            table[i][j] = table[i-1][j-self.array[i-1]]

        if (table[size][self.sum]):
            print(
                f"Yes,There Exists At least One Sub-Set whose sum of the elements is {self.sum}")
        else:
            print(f"No Sub-Set Exists ")

    @staticmethod
    def time_complexity():
        """

        :return: time complexity
        """
        return "Time Complexity : O(N*Sum)"

    @staticmethod
    def get_code():
        """
        
        :return: source code
        """
        return inspect.getsource(SubsetSum)
