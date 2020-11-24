Sorting Algorithms
==================


Quick Start Guide
------------------

Time Complexity And Space Complexity

+------------------------+------------------------------------------+------------------+
|   Sorting Algorithms   |             Time Complexity              | Space Complexity |
|                        |                                          |                  |
+========================+============+==============+==============+==================+
|  Sorting               |   Best     | Average      | Worst        |       Worst      |
+------------------------+------------+--------------+--------------+------------------+
| Bubble Sort            | O(n)       | O(n^2)       | O(n^2)       |       O(1)       |
+------------------------+------------+--------------+--------------+------------------+
| Insertion Sort         | O(n)       | O(n^2)       | O(n^2)       |       O(1)       |
+------------------------+------------+--------------+--------------+------------------+
| Selection Sort         | O(n^2)     | O(n^2)       | O(n^2)       |       O(1)       |
+------------------------+------------+--------------+--------------+------------------+
| Counting Sort          | O(n+k)     | O(n+k)       | O(n+k)       |       O(k)       |
+------------------------+------------+--------------+--------------+------------------+
| Merge Sort             | O(nLogn)   | O(nLogn)     | O(nLogn)     |       O(n)       |
+------------------------+------------+--------------+--------------+------------------+
| Heap Sort              | O(nLogn)   | O(nLogn)     | O(nLogn)     |       O(1)       |
+------------------------+------------+--------------+--------------+------------------+
| Quick Sort             | O(nLogn)   | O(nLogn)     | O(n^2)       |     O(nLogn)     |
+------------------------+------------+--------------+--------------+------------------+
| ShellSort              | O(n)       | O((nLogn)^2) | O((nLogn)^2) |      O(1)        |
+------------------------+------------+--------------+--------------+------------------+






.. code-block:: python

    # import required algorithm
    >>> from package.pygostructures.data_structures.sorting import BubbleSort

    # create array
    >>> my_array = [4,1,77,2,3,0,99,100,65]

    # pass the array as argument
    >>> b = BubbleSort(my_array)

    # call the function
    >>> b.bubblesort()
    Sorted Array :  [0, 1, 2, 3, 4, 65, 77, 99, 1

   

Sorting Algorithms
------------------

.. automodule:: pythorn.data_structures.sorting

    Bubble Sort
    -----------

    .. autoclass:: BubbleSort
       :members:


    Counting Sort
    -------------


    .. autoclass:: CountingSort
       :members:




    Insertion Sort
    --------------


    .. autoclass:: InsertionSort
       :members:


    Merge Sort
    ----------


    .. autoclass:: MergeSort
       :members:


    Quick Sort
    ----------

    Example :
        .. code-block:: python

            # import required algorithm
            >>> from pythorn.data_structures.sorting import QuickSort

            # create array
            >>> f = [2,6,9,10,100,20,3,6,9,78,98,2,1500]

            # pass array , value zero and len(array)-2 as an argument 
            >>> b = QuickSort(f,0,len(f)-2)
            >>> b.quick_sort()

            # call the function
            [2, 2, 3, 6, 6, 9, 9, 10, 20, 78, 98, 100, 1500]

    .. autoclass:: QuickSort
       :members:

    
    Selection Sort
    -------------


    .. autoclass:: SelectionSort
       :members:


    Shell Sort
    -----------


    .. autoclass:: ShellSort
       :members:

       
    HeapSort
    -----------


    .. autoclass:: HeapSort
       :members:


    
