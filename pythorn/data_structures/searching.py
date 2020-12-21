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
from pythorn.data_structures.recursion import fibonacci
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





    """

    def __init__(self, array=None, key=None):
        """
        :param array: array of elements
        :param key: key to be search in the given array

        """
        self.array = array
        self.key = key

    def fibonacci_search(self):
        """
        :return: index of key if its found in the sorted list else returns false
        """

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
        """
        :return: index of key if its found in the sorted list else returns false
        """

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


    """

    def __init__(self, array=None, key=None):
        """
        :param array: array of elements
        :param key: key to be search in the given array

        """
        self.array = array
        self.key = key

    def jump_search(self):
        """
        :return: index of key if its found in the sorted list else returns false
        """
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



    """

    def __init__(self, array=None, key=None):
        """
        :param array: array of elements
        :param key: key to be search in the given array

        """
        self.array = array
        self.key = key

    def linear_search(self):
        """
        :return: index of key if its found in the list else returns false

        """
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
