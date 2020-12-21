Searching Algorithms
====================

Quick Start Guide
------------------

``Searching Algorithms`` :- Searching is also a common and well-studied task. This task can be described formally as follows:


Given a list of values, a function that compares two values and a desired value, find the position of the desired value in the list.


We will look at various algorithms that perform this task:


``linear search``, which simply checks the values in sequence until the desired value is found

Linear search is the simplest searching algorithm that searches for an element in a list in sequential order. We start at one end and check every element until the desired element is not found.


Linear Search Algorithm::

      LinearSearch(array, key)
     for each item in the array
     if item == value
          return its index



``binary search``, which requires a sorted input list, and checks for the value in the middle of the list, repeatedly discarding the half of the list which contains values which are definitely either all larger or all smaller than the desired value


Binary search can be implemented only on a sorted list of items. If the elements are not sorted already, we need to sort them first.


- Binary Search Algorithm can be implemented in two ways which are discussed below.
     + Iterative Method
     + Recursive Method

     
The recursive method follows the divide and conquer approach.


- Binary Search Algorithm

     Iteration Method::

      do until the pointers low and high meet each other.
          mid = (low + high)/2
          if (x == arr[mid])
               return mid
          else if (x > A[mid]) // x is on the right side
               low = mid + 1
          else                       // x is on the left side
               high = mid - 1



     Recursive Method::

      binarySearch(arr, x, low, high)
          if low > high
               return False 
          else
               mid = (low + high) / 2 
               if x == arr[mid]
                    return mid
               else if x < data[mid]        // x is on the right side
                    return binarySearch(arr, x, mid + 1, high)
               else                               // x is on the right side
                    return binarySearch(arr, x, low, mid - 1)


         
``Jump Search`` :- Like binary search, Jump search is a searching algorithm for sorted array.

    The basic idea is to check fewer elements by jumping ahead by fixed steps or skipping
    some elements in the place of searching all elements


    For example : 
    suppose we have an array[] of size n and block (to be jumped ) size m . then we search
    at the indexes array[0],array[m],array[2m],.....array[km]and so on.


    Once we find the interval (array[km] < X < array[(k+1)m]),we perform a linear search 
    operation from the index km to find the element x.



    Example:: 
          let array : [0,2,6,8,10,21,34,66,89,120,124,300,350,500,549,600]

          len(array)  = 16 

          key  = 66

          Assume block size = 4

          1 . Jump from index 0 to index 4 
          2 . jump from index 4 ot index 8
          3 . since element at index 8 (89) is greater than the key element (66) so we will jump back to index 4
          4 . now from here we will perform linear search from index 4 to index 8 to get our key element 66
     



``Interpolation Search`` :- Interpoaltion search algorithm is a search algorithm that has been inspired by the way humans search 
    through a telephone book for a particular name,the key value by which book's entries are ordered.


    It is an improvement above binary search, in binary search ,we always move to the middle element 
    whereas interpolation search moves to a different element in order to reduce the search space further.


    for example : if the value of the key is closer to the last element ,interpolation search is likely to 
    start towards the end side.


``Fibonacci Search`` :- Fibonacci search is an efficient search algorithm based on divide and conquer principle that
    can find an element in the given sorted array with the help of fibonacci series in O(Logn) time complexity.

    On Avg , fibonacci search require 4% more comparisons than binary search


There are numerous other searching techniques. Often they rely on the construction of more complex data structures to facilitate repeated searching. Examples of such structures are hash tables (such as Python’s dictionaries) and prefix trees. Inexact searches that find elements similar to the one being searched for are also an important topic.


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


Below is the simple example for how to use queue using this package.


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
    ----------------

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


   

    








