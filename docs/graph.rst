Graphs
======


Quick Start Guide
------------------


.. code-block:: python

    # import required data structures
    >>> from pythorn.data_structures.graphs import AdjanceyList

    # pass number of nodes
    >>> a = AdjanceyList(5)

    # add edge with source node and destination node
    >>> a.add_edge(0,1)
    >>> a.add_edge(0,3)
    >>> a.add_edge(4,3)
    >>> a.add_edge(2,4)

    # printing Adjancey List 
    >>> a.print_list()
    node 1 -> 5
    node 2 -> 4
    node 3 -> 0 4
    node 4 -> 3 2
    node 5 -> 5 3




Graph Programs
--------------


.. automodule:: pythorn.data_structures.graphs


    Adjancey List
    -------------

    .. autoclass:: AdjanceyList
       :members:


    Adjancey Matrix
    ---------------

    Example :
        .. code-block:: python

            >>> from pythorn.data_structures.graphs import AdjanceyMatrix
            >>> a = AdjanceyMatrix(5)
            >>> a.add_edge(1,5)
            >>> a.add_edge(1,4)
            >>> a.add_edge(2,4)
            >>> a.add_edge(3,4)
            >>> a.add_edge(3,2)
            >>> a.add_edge(3,1)
            >>> a.print_matrix()
            [0, 0, 1, 1, 1]
            [0, 0, 1, 1, 0]
            [1, 1, 0, 1, 0]
            [1, 1, 1, 0, 0]
            [1, 0, 0, 0, 0]
            [1, 0, 0, 0, 0]

    .. autoclass:: AdjanceyMatrix
       :members:


    BFS 
    ---



    Example :
        .. code-block:: python

            # import required algorithm
            >>> from pythorn.data_structures.graphs import BFS

            # create graph
            >>> graph={  0: [1, 3,4],
            ...             1: [2],
            ...             2: [3],
            ...             3: [1,4],
            ...             4: [0,2] }

            # pass graph and value 0 as argument
            >>> bfs1 = BFS(graph,0)

            # call bfs main function 
            >>> z = bfs1.bfs()

            >>> print(z)
            [0, 1, 3, 4, 2]


    .. autoclass:: BFS
       :members:



    DFS
    ---

    Example :
        .. code-block:: python

            # import required algorithm
            >>> from package.pygostructures.data_structures.graphs import DFS

            # create graph
            >>> graph1 = {
            ...             0: [1, 3,4],
            ...             1: [2],
            ...             2: [3],
            ...             3: [1,4],
            ...             4: [0,2]}

            # pass graph and start vertex as argument
            >>> dfs1 = DFS(graph1,2)

            # call the function
            >>> z = dfs1.dfs()

            >>> print(z)
            [2, 3, 1, 4, 0]


    .. autoclass:: DFS
       :members:



    Topological Sort
    ----------------

    Example :
        .. code-block:: python

            # import required algorithm
            >>> from package.pygostructures.data_structures.graphs import *

            # pass number of vertices as argument
            >>> a = TopologicalSort(5)

            # adding edge with source and destination vertex
            >>> a.add_edge(0,3)
            >>> a.add_edge(0,4)
            >>> a.add_edge(0,3)
            >>> a.add_edge(2,3)
            >>> a.add_edge(2,1)
            >>> a.add_edge(2,4)


            # printing list
            >>> a.print_list()
            0 Vertex :  ->  3 -> 4 -> 3
            3 Vertex :  ->
            2 Vertex :  ->  3 -> 1 -> 4

            # call main function
            >>> a.topological_Sort()
            2--> 0--> 3


    .. autoclass:: TopologicalSort
       :members:

