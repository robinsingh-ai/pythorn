"""
Author : Robin Singh

Programs List : 

1 . Bubble Sort
2 . Counting Sort
3 . Insertion Sort
4 . Merge Sort
5 . Quick Sort
6 . Selection Sort
7 . Shell Sort
8 . Heap Sort

"""
import inspect


class BubbleSort(object):
    """
    Bubble Sort Implementation


    """

    def __init__(self, array=None):
        """
        :param array: array to be sorted
        :param length: length of the array
        """
        self.array = array
        self.length = len(array)

    def bubblesort(self):
        """
        :return: sorted values
        """
        for i in range(0, self.length-1):

            flag = 0

            for j in range(0, self.length-1-i):
                if self.array[j] > self.array[j+1]:
                    t = self.array[j]
                    self.array[j] = self.array[j+1]
                    self.array[j+1] = t
                    flag = 1

            if flag == 0:
                return print("Sorted Array : ", self.array)

    @staticmethod
    def get_code():
        """
        returns source code of the current class

        :return: source code
        """
        return inspect.getsource(BubbleSort)

    @staticmethod
    def time_complexity():
        """
        returns time complexity of the functions

        :return: string
        """
        return " Best Case : O(N), "\
               " Worst Case: O(n^2), "\
               " Average Case: O(n^2) "


class CountingSort(object):
    """
    Counting Sort Implementation

    """

    def __init__(self, array=None):
        """
        :param array: array to be sorted
        :param length: length of the array
        :param max: maximum value from the given array
        :param auxiliary: null array of length len(array)
        """

        self.array = array
        self.length = len(array)
        self.max = max(array)
        self.auxiliary = [0]*self.length

    def counting_sort(self):
        """
        :return: sorted values
        """

        c = [0]*(self.max+1)
        for i in range(0, self.max):
            c[i] = 0

        for j in range(0, self.length):
            c[self.array[j]] += 1

        for i in range(1, self.max+1):
            c[i] += c[i-1]

        for j in range(self.length-1, -1, -1):
            self.auxiliary[c[self.array[j]]-1] = self.array[j]
            c[self.array[j]] -= 1

        return self.auxiliary

    @staticmethod
    def get_code():
        """
        
        :return: source code
        """
        return inspect.getsource(CountingSort)

    @staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return " Best Case : O(N+K), "\
               " Worst Case: O(N+K), "\
               " Average Case: O(N+K) "


class InsertionSort(object):
    """
    Insertion Sort Implementation

    """

    def __init__(self, array=None):
        """
        :param array: array to be sorted
        :param length: length of the array

        """
        self.array = array
        self.length = len(array)

    def insertion_sort(self):
        """
        :return: sorted values
        """
        for i in range(1, self.length):
            t = self.array[i]
            j = i-1

            while j >= 0 and self.array[j] > t:
                self.array[j+1] = self.array[j]
                j -= 1

            self.array[j + 1] = t
        return self.array

    @staticmethod
    def get_code():
        """
        
        :return: source code
        """
        return inspect.getsource(InsertionSort)

    @staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return " Best Case : O(N), "\
               " Worst Case: O(N^2), "\
               " Average Case: O(N^2) "


class MergeSort(object):
    """
    Merge Sort Implementation


    """

    def __init__(self, array):
        """
        :param array: array to be sorted

        """

        self.array = array

    def merge_sort(self):
        """
        function to sort an array using merge sort algorithm

        :return: sorted values
        """
        if len(self.array) > 1:
            m = len(self.array) // 2
            left = self.array[:m]
            right = self.array[m:]

            leftsort = MergeSort(left)
            leftsort.merge_sort()

           
            rightsort = MergeSort(right)
            rightsort.merge_sort()
            

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:

                    self.array[k] = left[i]

                    i += 1
                else:
                    self.array[k] = right[j]
                    j += 1

                k += 1

            while i < len(left):
                self.array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                self.array[k] = right[j]
                j += 1
                k += 1

        return self.array

    @staticmethod
    def get_code():
        """
    
        :return: source code
        """
        return inspect.getsource(MergeSort)

    @staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return " Best Case : O(nLogn), "\
               " Worst Case: O(nLogn), "\
               " Average Case: O(nLogn) "


class QuickSort(object):
    """
    Quick Sort Implementation

    """

    def __init__(self, array=None, lower=None, upper=None):
        """
        :param array: array to be sorted

        """

        self.array = array
        self.lowerbound = lower
        self.upperbound = upper

    @staticmethod
    def partition(a, lb, ub):
        """
        function for partition

        """
        pivot = a[lb]
        start = lb
        end = ub

        while start < end:
            while a[start] <= pivot:
                start += 1
            while a[end] > pivot:
                end -= 1
            if start < end:
                t = a[start]
                a[start] = a[end]
                a[end] = t

        a[lb] = a[end]
        a[end] = pivot

        return end

    def quick_sort(self):
        """
        
        :return: sorted values of the given array
        """
        if self.lowerbound < self.upperbound:
            p = QuickSort.partition(
                self.array, self.lowerbound, self.upperbound)

            quick1 = QuickSort(self.array, self.lowerbound, p-1)
            quick1.quick_sort()

            quick2 = QuickSort(self.array, p+1, self.upperbound)
            quick2.quick_sort()
        return self.array

    @staticmethod
    def get_code():
        """
        
        :return: source code
        """
        return inspect.getsource(QuickSort)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """
        return " Best Case : O(nLogn), "\
               " Worst Case: O(n^2), "\
               " Average Case: O(nLogn) "


class SelectionSort(object):
    """
    Selection Sort Implementation

    """

    def __init__(self, array=None):
        """
        :param array: array to be sorted
        :param lenght: array length

        """
        self.array = array
        self.length = len(array)

    def selection_sort(self):
        """
        :return: sorted values of array
        """
        for i in range(0, self.length-1):
            min = i
            for j in range(i+1, self.length):
                if self.array[j] < self.array[min]:
                    min = j
            if min != i:
                t = self.array[i]
                self.array[i] = self.array[min]
                self.array[min] = t

        return self.array

    @staticmethod
    def get_code():
        """
        
        :return: source code
        """
        return inspect.getsource(SelectionSort)

    @staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return " Best Case : O(n^2), "\
               " Worst Case: O(n^2), "\
               " Average Case: O(n^2) "


class ShellSort(object):
    """
    Shell Sort Implementation

    """

    def __init__(self, array=None):
        """
        :param array: array to be sorted
        :param lenght: array length

        """
        self.array = array
        self.length = len(array)

    def shell_sort(self):
        """
        :return: sorted values of array
        """
        g = self.length // 2
        while g > 0:
            for i in range(g, self.length):
                t = self.array[i]
                j = i
                while j >= g and self.array[j - g] > t:
                    self.array[j] = self.array[j - g]
                    j -= g

                self.array[j] = t
            g = g // 2
        return self.array

    @staticmethod
    def get_code():
        """
        
        :return: source code
        """
        return inspect.getsource(SelectionSort)

    @staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return " Best Case : O(n), "\
               " Worst Case: O((nLogn)^2), "\
               " Average Case: O((nLogn)^2) "


class HeapSort(object):
    """
    Heap Sort Implementation

    """

    def __init__(self, array=None):
        """
        :param array: array to be sorted
        :param lenght: array length

        """
        self.array = array
        self.length = len(array)

    @staticmethod
    def heapify(a, n, i):
        """
        funtion for converting a binary tree into a Heap data structure
        """
        largest = i
        l = 2 * i
        r = 2 * i + 1

        if l < n:
            if a[i] < a[l]:
                largest = l
        if r < n:
            if a[largest] < a[r]:
                largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            HeapSort.heapify(a, n, largest)

    def heapSort(self):
        """
        
        :return: sorted values of array
        """
        for i in range(self.length, -1, -1):
            HeapSort.heapify(self.array, self.length, i)

        for i in range(self.length-1, 0, -1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            HeapSort.heapify(self.array, i, 0)
        return self.array

    @staticmethod
    def get_code():
        """

        :return: source code
        """
        return inspect.getsource(HeapSort)

    @staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return " Best Case : O(nLogn), "\
               " Worst Case: O(nLogn), "\
               " Average Case: O(nLogn) "
