"""
Author : Robin Singh

Programs List : 
1 . Factorial
2 . Fibonacci
3 . Tower Of Hanoi
4 . Binary Search (Recursive)

"""
import inspect


def factorial(number):
    """
    Factorial Using Recursion

    Example : 
    5!
    Factorial is denoted by ! 
    Factorial(5)  : 5 X 4 X 3 X 2 X 1 = 120 

    """
    if number == 0:
        return 1
    else:
        print(f"{number}*", end=" ")
        return number * factorial(number-1)


def fibonacci(number):
    """
    Fibonacci Implementaion

    The Febonacci numbers are the numbers in the following sequence
    0,1,1,2,3,5,8,13,21,34,55,89,144,............

    In Mathematical terms,the sequence Fn of the fibonacci numbers is defined by the recurrence relation

    F(n) = F(n-1) + F(n-1)

    with seed values
    F(0) = 0 and F(1) = 1

    Example : 
    Fibonacci(5) = 5
    Fibonacci(10) = 55
    Fibonacci(1) = 1
    Fibonacci(2) = 2
    Fibonacci(12) = 144



    """

    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)


def tower_of_hanoi(disk, source, destination, auxiliary):
    """
    Tower Of Hanoi Implementation Using Recursion

    Tower of hanoi is a mathematical puzzle.It consists of three poles and a number of disks of different sizes which can slide onto any poles.

    The puzzle starts with a disk in a neat stack u ascending order of size in one pole, the smallest at the top making it a conical shape.

    The objective of the puzzle is to move all the disks from one pole (Source Pole) to another pole (Destination pole) with the help of the third pole (auxiliary pole)

    The puzzle has two rules :
    1 . You Can't place a larger disk onto smaller disk or vice-versa
    2 . Only one disk can be moved at a time

    Moves Reqd to Solve This puzzle is given by : 2^(n)-1

    Example :
    Number Of Dics : 3
    Source Pole : A
    Destination Pole : C
    Auxiliary Pole : D

    Solution :
    Tower_of_hanoi(3,"A","B","C")
    Move Disk From Source  A To Destination B
    Move Disk From Source  A To Destination C
    Move Disk From Source  B To Destination C
    Move Disk From Source  A To Destination B
    Move Disk From Source  C To Destination A
    Move Disk From Source  C To Destination B
    Move Disk From Source  A To Destination B

    """

    if disk == 1:
        print("Move Disk From Source ", source, "To Destination", destination)
    else:
        tower_of_hanoi(disk-1, source, auxiliary, destination)
        tower_of_hanoi(1, source, destination, auxiliary)
        tower_of_hanoi(disk-1, auxiliary, destination, source)


def binary_search(A, key, low, high):
    """
    Implementation of Binary Search Recursive Method

    Below function perform sa binary search on a sorted list
    and returns the index of the item if it;s present else returns false

    :param list: a sorted list 
    :param key: key to search from given sorted list
    :return: index of key if its found in the sorted list else returns false 

    Example : 
    A = [5  9   10  45  65  78  98  102 1045]
    Key  = 11

    Binary_Search(A,11,0,len(A))

    Solution :
    Not Present

   ==============================================


    A = [5  9   10  45  65  78  98  102 1045]
    Key  = 65

    Binary_Search(A,65,0,len(A))

    Solution : 

    Element is Present at index  : 4 

    """

    if low > high:
        print("Not Present")
    else:
        m = (low+high)//2
        if key == A[m]:
            print("Element is Present at index ", m)
        elif key < A[m]:
            return binary_search(A, key, low, m-1)
        else:
            return binary_search(A, key, m+1, high)


def time_complexity(name):
    """
    :return: time complexity
    """
    if name == "factorial":
        return " Time Complexity : O(n) "
    elif name == "fibonacci":
        return " Time Complexity : O(2^n) "
    elif name == "tower_of_hanoi":
        return " Time Complexity : O(2^n) or O(a^n) "
    elif name == "binary_search":
        return " Best Case : O(1), "\
               " Worst Case: O(Logn), "\
               " Average Case: O(Logn) "
    else:
        return " No Information or (Enter function name correctly)"


def get_code(name):
    """

    :return: source code
    """
    return inspect.getsource(name)
