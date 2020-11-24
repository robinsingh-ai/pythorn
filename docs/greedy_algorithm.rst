Greedy Algorithms
=================

Quick Start Guide
------------------


Time Complexity 

+------------------------+------------------------------------------+
|   Greedy  Algorithms   |             Time Complexity              | 
|                        |                                          |                  
+========================+==========================================+
| Activity Selection     | O(n log n) when sorted else O(n)         |   
+------------------------+------------------------------------------+
| Dijkstra               | O((E+V)Log(V))                           |      
+------------------------+------------------------------------------+
| Fractional Knapsack    | O(nLogn)                                 |      
+------------------------+------------------------------------------+
| Kruskal                | O(ElogE) or O(ElogV)                     |      
+------------------------+------------------------------------------+
| Prims                  | O(ElogV)                                 |      
+------------------------+------------------------------------------+
| Egyptian Fraction      | ---                                      |      
+------------------------+------------------------------------------+
| Minimum Coin Exchange  | O(N*logN)                                |      
+------------------------+------------------------------------------+


Greedy Programs
---------------

.. automodule:: pythorn.algorithms.greedy_algorithm
   
   Activity Selection
   ------------------

   Implementation Of Activity Selection Problem Using Greedy Approch:

    
    here we have n activities with their start and finish times. Select the maximum number of activities
    that can be performed by a single person, assuming that a person can only work on a single activity at a time

    -- Robin Singh

   Example :
        .. code-block:: python
        

            # import required algorithm
            >>> from pythorn.algorithms.greedy_algorithm import ActivitySelection

            # Start values
            >>> start_value = [5,9,10,6,2,3,7]

            # finish values
            >>> finish_values = [10,9,6,10,1,3,8]

            # pass start and finish values as an argument
            >>> a = ActivitySelection(start_value,finish_values)
            >>> a.activity_selection()
            Following Activities Are selected :
            Index   Start   Finish
            0       5 -->   10
            2       10 -->  6
            3       6 -->   10

   .. autoclass:: ActivitySelection
       :members:





   Dijkstra
   --------

   Implementation of Dijkstra's Algorithm:

    Dijkstra’s algorithm finds the shortest path in a weighted graph containing only positive edge weights from a single source

    -- Robin Singh

   Example :
        .. code-block:: python

            # import required algorithm
            >>> from pythorn.algorithms.greedy_algorithm import Dijkstra

            # creating graph
            >>> graph = {
            ...         'a':{'b':4,'h':8},
            ...         'b':{'a':4,'h':11,'c':8},
            ...         'c':{'b':8,'i':2,'d':7},
            ...         'd':{'e':9,'c':7,'f':14},
            ...         'e':{'d':9,'f':10},
            ...         'f':{'d':14,'e':10,'g':2},
            ...         'g':{'i':6,'f':2,'h':1},
            ...         'h':{'a':8,'b':11,'i':7,'g':1},
            ...         'i':{'c':2,'g':6,'h':7}
            ...     }

            # entre source and destination node
            >>> source = 'c'
            >>> dest = 'h'

            # pass all the 3 parameters as argument
            >>> d = Dijkstra(source,dest,graph)
            >>> d.dijkstra()
            Single Source Shortest Path :['c', 'i', 'h'] --> COST : 9
         



   .. autoclass:: Dijkstra
       :members:



   Fractional Knapsack
   ------------------

   Implementation Of Fractional Knapsack:

    

    - Given weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack

    - n Fractional Knapsack, we can break items for maximizing the total value of knapsack

    - This problem in which we can break an item is also called the fractional knapsack problem

    - An efficient solution is to use Greedy approach. The basic idea of the greedy approach is to calculate
    the ratio value/weight for each item and sort the item on basis of this ratio. Then take the item with

    - the highest ratio and add them until we can’t add the next item as a whole and at the end add the next item as much as we can

    - Which will always be the optimal solution to this problem

    -- Robin Singh



   Example :
        .. code-block:: python

            # import required algorithm
            >>> from pythorn.algorithms.greedy_algorithm import FractionalKnapsack

            # create a list with profit values
            >>> profit = [10,9,7,12,30,16]

            # create a list with weight of the items in the same order
            >>> weight = [5,7,3,10,6,7]

            # capacity of the knapsack
            >>> capacity = 15

            # weight,profit,capacity as an argument in the same order
            >>> a = FractionalKnapsack(weight,profit,capacity)

            # call the function
            >>> a.fractional_knapsack()
            Fractional Knapsack
            Profit :30              Weight  : 6             Profit/Weight : 5.0
            Profit :7               Weight  : 3             Profit/Weight : 2.3333333333333335
            Profit :16              Weight  : 7             Profit/Weight : 2.2857142857142856
            Total Profit : 50.714285714285715


   .. autoclass:: FractionalKnapsack
       :members:




   Kruskal's Algorithm
   -------------------


   Implementation of Kruskal's Algorithm:

    Minimum Cost Spanning Tree of a given connected, undirected and weighted graph

    It is a greedy algorithm in graph theory as it finds a minimum spanning tree for a connected weighted graph adding increasing cost at each step

    -- Robin Singh


   Example :
        .. code-block:: python

            # Here we have to import two classes 1st is Kruskal itself and second is Edge (for making source ,destination edge with weight of the edge)

            >>> from pythorn.algorithms.greedy_algorithm import Kruskal
            >>> from pythorn.algorithms.greedy_algorithm import Edge

            # Creating Edge (Source,Destination,Weight)
            >>> A = Edge(1, 6, 10)
            >>> B = Edge(3, 4, 12)
            >>> C = Edge(7, 2, 14)
            >>> D = Edge(2, 3, 16)
            >>> E = Edge(7, 4, 18)
            >>> F = Edge(4, 5, 22)
            >>> G = Edge(5, 7, 24)
            >>> H = Edge(5, 6, 25)
            >>> I = Edge(1, 2, 28)

            # declaring number of nodes
            >>> num_nodes = 8

            # pass number of nodes and list of all the edges as argument
            >>> a = Kruskal(num_nodes,[A,B,C,D,E,F,G,H,I])
            >>> a.kruskal()
            MCST
            SOURCE  DESTINATION  WEIGHT
            1    -->  6     -->     10
            3    -->  4     -->     12
            7    -->  2     -->     14
            2    -->  3     -->     16
            4    -->  5     -->     22
            5    -->  6     -->     25

            MCST(MINIMUM COST) :  99

   .. autoclass:: Kruskal
       :members:



   Prims
   -----

   Implementation of prims algorithm:

    

    In Prim's Algorithm, a conquered territory (initialized with any start vertex)
    is chosen in which we keep adding the vertices as we go through the algorithm. 

    To get the minimum spanning tree, we keep adding vertices to the conquered edges
    with the greedy paradignm that we select the edge with the minimum weight of all the edges starting the
    conquered territory and ending at the unconquered territory. The end of the minimum weight edge thus chosen is
    then added to the conquered territory and removed from the unconquered territory. In such a way,
    we go on till the conquered territory spans all the vertices of the graph

   Example :
        .. code-block:: python
            # import required algorithms
            >>> from pythorn.algorithms.greedy_algorithm import Prims

            # creating a graph 
            >>> list = {}
            >>> list[1] = [(6, 10), (2, 28)]
            >>> list[2] = [(1, 28), (3, 16), (0, 14)]
            >>> list[3] = [(2, 16), (4, 12)]
            >>> list[4] = [(3, 12), (5, 22), (0, 18)]
            >>> list[5] = [(4, 22), (6, 25), (0, 24)]
            >>> list[6] = [(1, 10), (5, 25)]
            >>> list[0] = [(2, 14), (4, 18), (5, 24)]

            # pass source node and graph as an argument
            >>> primss = Prims(3,list)
            >>> primss.prims()
            3 -->   4 -->   2 -->   0 -->   5 -->   6 -->   1 -->   Cost :  99



   
   .. autoclass:: Prims
       :members:



   Egyptian Fraction
   ------------------

   Implementation of Eqyption Fraction:

    Every positive fraction can be represented as sum of unique unit fractions

    A fraction is unit fraction if numerator is 1 and denominator is a positive integer, for example 1/3 is a unit fraction

    Such a representation is called Egyptian Fraction as it was used by ancient Egyptians

   Example :
        .. code-block:: python


            >>> from pythorn.algorithms.greedy_algorithm import EgyptianFraction
            >>> a = EgyptianFraction(7,19)

            >>> a.egyptian_fraction()

            1/3 +  1/29 + 1/1653 


   


   .. autoclass:: EgyptianFraction
       :members:



   Minimum Coin Exchange
   ---------------------


   Implementation of Minimum Coin Exchange Problem:

    Here we have a value V, if we want to make a change for V Rs, and we have an infinite supply of each of the denominations in Indian currency, i.e., we have an infinite supply of { 1, 2, 5, 10, 20, 50, 100, 500, 2000} valued coins/notes

    Then what is the minimum number of coins or notes are needed to make the change

   Example :
        .. code-block:: python

            # import required algorithm
            >>> from pythorn.algorithms.greedy_algorithm import *

            # pass money 
            >>> a = MinimumCoinExchange(2589)
            >>> a.minimum_coin_exchange()
            2  2  5  10  20  50  500  2000

   .. autoclass:: MinimumCoinExchange
       :members:



