Dynamic Programming
===================

Quick Start Guide
------------------






Dynamic Programming
-------------------


.. automodule:: pythorn.algorithms.dynamic_programming

   Bellman Ford
   -------------

    Implementation of Bellman Ford Algorithm(Dynamic Programming) :

    Bellman Ford algorithm helps us find the shortest path from a vertex to all other vertices of a weighted graph.

    It is similar to Dijkstra's algorithm but it can work with graphs in which edges can have negative weights.



   Example :
        .. code-block:: python

            # import required algorithm
            >>> from pythorn.algorithms.dynamic_programming import BellmanFord

            # create graph
            >>> graph = {
            ...         'a':{'b':6,'c':4,'d':5},
            ...         'b':{'e':-1},
            ...         'c':{'e':3,'b':-2},
            ...         'd':{'c':-2,'f':-1},
            ...         'e':{'f':3},
            ...         'f':{}
            ...     }

            # pass graph and source node
            >>> a = BellmanFord(graph,'a')
           
            >>> a.bellman_ford()
            distances from source {'a': 0, 'b': 1, 'c': 3, 'd': 5, 'e': 0, 'f': 3}
            predecssor vertices {'a': None, 'b': 'c', 'c': 'd', 'd': 'a', 'e': 'b', 'f': 'e'}


   .. autoclass:: BellmanFord
      :members:



   Floyd Warshall
   --------------

   Implementation of Floyd Warshall's Algorithm:

   Floyd-Warshall Algorithm is an algorithm for finding the shortest path between all the pairs of vertices in a weighted graph

   This algorithm works for both the directed and undirected weighted graphs. But, it does not work for the graphs
   with negative cycles

   Example :
      .. code-block:: python

         # import required algorithm
         >>> from pythorn.algorithms.dynamic_programming import FloydWarshall

         # initialize a infinity value
         >>> INF = 999999999999

         # create a graph in matrix form
         >>> G = [[0, 9, -4, INF],
         ...          [6, 0, INF, 2],
         ...          [INF, 5, 0, INF],
         ...          [INF, INF, 1, 0]]

         # pass graph and no of vertices as an argument
         >>> a = FloydWarshall(G,4)
         >>> a.floyd_warshall()
         0  1  -4  3
         6  0  2  2
         11  5  0  7
         12  6  1  0


         
   .. autoclass:: FloydWarshall
      :members:



   Longest Common Subsequence
   --------------------------


   Implementation Of LCS(Dynamic Approch):


      Given two sequences,here we have to find the length of longest subsequence present in both of them

      Example 

      LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

      LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

   Example :

      .. code-block:: python

         # import required algorithm
         >>> from pythorn.algorithms.dynamic_programming import LongestCommonSubsequence

         # entre string1 and string2 
         >>> string1 = "ABCDEFABC"
         >>> string2 = "CDASCVCE"

         # pass both the strings as argument
         >>> a = LongestCommonSubsequence(string1,string2)
         >>> a.longest_common_subsequence()
         Lenth Of Sequence : 4, And Sequence is : CDAC



   .. autoclass:: LongestCommonSubsequence
      :members:




   Subset Sum
   ----------


   Implementation of Subset Sum:


      Implementation of Subset Sum problem which will return true if at least one sub set exists of the required sum


   Example :

      .. code-block:: python


         # import required algorithm
         >>> from package.pygostructures.algorithms.dynamic_programming import SubsetSum

         # create a array
         >>> array = [2,9,7,6,3,4,15,12,32]

         # pass array and value 
         >>> a = SubsetSum(array,14)
         >>> a.subset_sum()
         Yes,There Exists At least One Sub-Set whose sum of the elements is 14



   .. autoclass:: SubsetSum
      :members:



   Coin Change Problem 1
   ---------------------



   Coin Exchange:


      Implementaion of Number Of Coins Change(Number Of ways to get required Sum)


   Example :

      .. code-block:: python

         # import required algorithm
         >>> from pythorn.algorithms.dynamic_programming import CoinChange01

         # pass amount value
         >>> a = CoinChange01(90)
         >>> a.coin_change()
         Number Of Ways To get Sum 90 = 559



   .. autoclass:: CoinChange01
      :members:



   Coin Change Problem 2
   ---------------------



   Coin Exchange 2:


      Implementaion Of minimum number Of coins required to get the sum of given Value  


   Example :

      .. code-block:: python

         # import required algorithm
         >>> from pythorn.algorithms.dynamic_programming import CoinChange02


         #Coins denominations are coins = [2, 3, 5, 10]

         # pass amount value
         >>> a = CoinChange02(50)
         >>> a.coin_change()
         Minimum Number Of Coins Required to get the sum of 50 = 5 Coins


   .. autoclass:: CoinChange02
      :members:














   

   


   