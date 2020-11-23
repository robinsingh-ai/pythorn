"""
Author : Robin Singh

Programs List : 
1 . Binary Search (Iterative Method)
2 . Fibonacci Search
3 . Interpolation Search
4 . Jump Search
5 . Linear Search

"""

import inspect
from data_structures.recursion import fibonacci
import math


class BinarySearch(object):
    """
    Binary Search Implementation
    """

    def __init__(self, array=None, key=None):
        """
        :param array: array of elements
        :param key: key to be search in the given array

        """
        self.array = array
        self.key = key

    def binary_search(self):
        """
        Implementation of Binary Search Recursive Method

        Below function perform an binary search on a sorted list
        and returns the index of the item if it;s present else returns false

        :return: index of key if its found in the sorted list else returns false

        Example :
        A = [5  9   10  45  65  78  98  102 1045]
        Key  = 11

        a = BinarySearch(A,11)
        a.binary_search()

        Solution :
        Not Present

        ==============================================


        A = [5  9   10  45  65  78  98  102 1045]
        Key  = 65

        a = BinarySearch(A,65)
        a.binary_search()


        Solution :

        Element is Present at index  : 4

        """
        low = 0
        high = len(self.array) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if self.array[mid] < self.key:
                low = mid + 1

            elif self.array[mid] > self.key:
                high = mid - 1

            else:
                return print("Key is present at index : ", mid)
        return "Not Found"

    @staticmethod
    def get_code():
        """
        :return: source code        """
        return inspect.getsource(BinarySearch)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """
        return " Best Case : O(1), "\
               " Worst Case: O(Logn), "\
               " Average Case: O(Logn) "


class FibonacciSearch(object):
    """
    Fibonacci Search Implementation

    Fibonacci search is an efficient search algorithm based on divide and conquer principle that
    can find an element in the given sorted array with the help of fibonacci series in O(Logn) time complexity.

    On Avg , fibonacci search require 4% more comparisons than binary search

    :return: index of key if its found in the sorted list else returns false

    """

    def __init__(self, array=None, key=None):
        """
        :param array: array of elements
        :param key: key to be search in the given array

        """
        self.array = array
        self.key = key

    def fibonacci_search(self):

        m = 0
        # Imported fibonacci function from recursion.py
        while fibonacci(m) < len(self.array):
            m = m+1

        offset = -1  # Main

        while (fibonacci(m) > 1):
            i = min(offset + fibonacci(m-2), len(self.array)-1)

            if self.key > self.array[i]:
                m = m-1
                offset = i

            elif self.key < self.array[i]:
                m = m-2

            else:

                return i

        # if m =2 then this case will be executed
        if (fibonacci(m - 1) and self.array[offset + 1] == self.key):
            return offset + 1
        return -1

    @staticmethod
    def get_code():
        """
        :return: source code       
        """
        return inspect.getsource(FibonacciSearch)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity      
        """
        return " Best Case  : O(1) , "\
               " Worst Case: O(Logn), "\
               " Average Case: O(Logn) "


class InterpolationSearch(object):
    """
    Interpolation Search Implementation

    Interpoaltion search algorithm is a search algorithm that has been inspired by the way humans search 
    through a telephone book for a particular name,the key value by which book's entries are ordered.

    It is an improvement above binary search, in binary search ,we always move to the middle element 
    whereas interpolation search moves to a different element in order to reduce the search space further.

    for example : if the value of the key is closer to the last element ,interpolation search is likely to 
    start towards the end side.

    :return: index of key if its found in the sorted list else returns false

    """

    def __init__(self, array=None, key=None):
        """
        :param array: array of elements
        :param length: length of array
        :param key: key to be search in the given array

        """
        self.array = array
        self.length = len(array)
        self.key = key

    def interpolation_search(self):

        l = 0
        h = self.length-1

        while l <= h and self.key >= self.array[l] and self.key <= self.array[h]:
            if l == h:
                if self.array[l] == self.key:
                    return l
                return -1

            # To find the position to be searched, it uses following formula
            pos = l + \
                int((
                    (float(h-l)/(self.array[h]-self.array[l]))*(self.key-self.array[l])))

            if self.array[pos] == self.key:
                return print("Key Found At Index : ", pos)

            if self.array[pos] < self.key:
                l = pos+1

            else:
                h = pos-1

        return print("Not Found")

    @staticmethod
    def get_code():
        """
        :return: source code        
        """
        return inspect.getsource(InterpolationSearch)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity        
        """
        return " Best Case  : O(1) , "\
               " Worst Case: O(n), "\
               " Average Case: O(Log Logn) "


class JumpSearch(object):
    """
    Jump Search Implementation

    Like binary search, Jump search is a searching algorithm for sorted array.

    The basic idea is to check fewer elements by jumping ahead by fixed steps or skipping
    some elements in the place of searching all elements

    For example : 
    suppose we have an array[] of size n and block (to be jumped ) size m . then we search
    at the indexes array[0],array[m],array[2m],.....array[km]and so on.

    Once we find the interval (array[km] < X < array[(k+1)m]),we perform a linear search 
    operation from the index km to find the element x.

    :return: index of key if its found in the sorted list else returns false

    Example : 
    let array : [0,2,6,8,10,21,34,66,89,120,124,300,350,500,549,600]

    len(array)  = 16 

    key  = 66

    Assume block size = 4

    1 . Jump from index 0 to index 4 
    2 . jump from index 4 ot index 8
    3 . since element at index 8 (89) is greater than the key element (66) so we will jump back to index 4
    4 . now from here we will perform linear search from index 4 to index 8 to get our key element 66


    """

    def __init__(self, array=None, key=None):
        """
        :param array: array of elements
        :param key: key to be search in the given array

        """
        self.array = array
        self.key = key

    def jump_search(self):
        low = 0
        jump = int(math.sqrt(len(self.array)))
        for i in range(0, len(self.array), jump):
            if self.array[i] < self.key:
                low = i
            elif self.array[i] == self.key:
                return i
            else:
                break
        c = low
        for j in self.array[low:]:
            if j == self.key:
                return print("Key Found At The Index : ", c)
            c += 1
        return print("Not Found")

    @staticmethod
    def get_code():
        """
        :return: source code        
        """
        return inspect.getsource(JumpSearch)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity      
        """
        return " Best Case  : O(1) , "\
               " Worst Case: O(√n), "\
               " Average Case: O(√n)"


class LinearSearch(object):
    """
    Linear Search Implementation

    Linear Search knows as sequential search is an algoerithm for finding a target key value within a list.
    it sequentially checks each element of the list for the target value until a match is found or until all
    the elements have seen searched.

    This is one of the most basic search algorithm

    :return: index of key if its found in the list else returns false



    """

    def __init__(self, array=None, key=None):
        """
        :param array: array of elements
        :param key: key to be search in the given array

        """
        self.array = array
        self.key = key

    def linear_search(self):
        i = 0
        while i < len(self.array):
            if self.key == self.array[i]:
                return print("Key found at index : ", i)
            i += 1

        return print("Not Found")

    @staticmethod
    def get_code():
        """
        :return: source code        
        """
        return inspect.getsource(LinearSearch)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity        
        """
        return " Best Case  : O(1) , "\
               " Worst Case: O(N), "\
               " Average Case: O(N)"
