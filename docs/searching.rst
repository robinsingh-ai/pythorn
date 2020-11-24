Searching Algorithms
====================

Quick Start Guide
------------------

+------------------------+------------------------------------------+
|  Searching Algorithms  |             Time Complexity              | 
|                        |                                          |
+========================+============+==============+==============+
|  Searching             |   Best     | Average      | Worst        |
+------------------------+------------+--------------+--------------+
| Binary Search          | O(1)       | O(Logn)      | O(Logn)      |
+------------------------+------------+--------------+--------------+
| Fibonacci Search       | O(1)       | O(Logn)      | O(Logn)      |
+------------------------+------------+--------------+--------------+
| Interpolation Search   | O(1)       | O(Log Logn)  | O(n)         |       
+------------------------+------------+--------------+--------------+
| Jump Search            | O(1)       | O(√n)        | O(√n)        |       
+------------------------+------------+--------------+--------------+
| Linear Search          | O(1)       | O(n)         | O(n)         |       
+------------------------+------------+--------------+--------------+


.. code-block:: python

    # impor required algorithm
    >>> from pythorn.data_structures.searching import LinearSearch

    # create list
    >>> a = [1,5,9,10,78,90,650]

    # pass list and key
    >>> b = LinearSearch(a,10)

    # call the function
    >>> b.linear_search()
    Key found at index :  3


Searching Programs
------------------

.. automodule:: pythorn.data_structures.searching
    
    

    Binary Search
    -------------

    .. autoclass:: BinarySearch
          
         :members:



    Fibonacci Search
    -----------------
            

    .. autoclass:: FibonacciSearch
         :members:


    Interpolation Search
    --------------------
            

    .. autoclass:: InterpolationSearch
         :members:


    Jump Search
    -----------
            

    .. autoclass:: JumpSearch
         :members:


    Linear Search
    -------------
            

    .. autoclass:: LinearSearch
         :members:




    








