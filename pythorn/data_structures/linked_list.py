"""
Author : Robin Singh

Programs List:

1.Singly Linked List
2.Doubly Linked List
3.Circular Linked List
4.Stack Using Linked List
5.Queue Using Linked List
"""
import inspect


class Node(object):
    """
    For Creating a Node.
    """

    def __init__(self, element, next=None):
        """
        :param element: value of the node

        """
        self.data = element
        self.next = next


class SinglyList(object):
    """
    Singly Linked List Implementation 
    """

    def __init__(self):
        """
        :param start: Head of the node
        """
        self.start = None

    def insert(self, ele):
        """
        inserts an element at the start of the linked list
        """
        node = Node(ele)  # Initialising a empty node from Node Class
        if self.start == None:
            self.start = node
        else:
            node.next = self.start
            self.start = node

    def delete(self):
        """
        deletes an element from the start
        """
        if self.start == None:
            return print("Empty list")
        else:
            temp = self.start
            self.start = self.start.next
            return temp.data

    def display_list(self):
        """
        displays current linked list
        """
        if self.start == None:
            return True
        else:
            temp = self.start
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

    def size(self):
        """
        returns size of the linked list
        """
        curr = self.start
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    @staticmethod
    def get_code():
        """
        :return: source code
        """
        return inspect.getsource(SinglyList)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """
        return "Insertion : O(1) ,"\
               "Deletion  : O(1)"


class DoublyList(object):
    """
    Doubly Linked List Implementation 
    """

    def __init__(self):
        """
        :param start: Head of the node
        """
        self.start = None

    def insert_start(self, ele):
        """
        inserts an element at the start of the linked list
        """
        node = Node(ele)  # Initialising a empty node from Node Class
        if self.start == None:
            self.start = node
        else:
            node.next = self.start
            self.start = node

    def insert_end(self, ele):
        """
        inserts an element at the end of the linked list 
        """
        node = Node(ele)  # Initialising a empty node from Node Class
        if self.start == None:
            self.start = node
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def delete_start(self):
        """
        deletes an element from the start
        """
        if self.start == None:
            return print("Empty list")
        else:
            temp = self.start
            self.start = self.start.next
            return temp.data

    def delete_end(self):
        """
        deletes an element from the end
        """
        if self.start == None:
            return
            print("empty list")
        n = self.start
        while n.next.next != None:
            n = n.next
        print("deleted ele", n.next.data)
        n.next = None

    def display_list(self):
        """
        displays current linked list
        """
        if self.start == None:
            return True
        else:
            temp = self.start
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

    def size(self):
        """
        returns size of the linked list
        """
        curr = self.start
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    @staticmethod
    def get_code():
        """
        :return: source code
        """
        return inspect.getsource(DoublyList)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """
        return "Insertion : O(1) ,"\
               "Deletion  : O(1)"


class CircularList(object):
    """
    Circular Linked List Implementation
    """

    def __init__(self):
        """
        :param start: Head of the node
        :param end: Tail of the node
        :param size: Size of the list 
        """
        self.start = None
        self.end = None
        self.size = 0

    def __len__(self):
        """
        returns size of the list
        """
        return self.size

    def is_Empty(self):
        """
        checks whether list is empty or not
        """
        if self.size == 0:
            return True
        else:
            return False

    def insert_start(self, e):
        """
        inserts an element at the start
        """
        node = Node(e, None)
        if self.is_Empty():
            self.start = node
            self.end = node
            node.next = node

        else:
            self.end.next = node
            node.next = self.start
        self.start = node
        self.size += 1

    def insert_end(self, e):
        """
        inserts an element at the end
        """
        node = Node(e, None)
        if self.is_Empty():
            self.start = node
            self.end = node
            node.next = node

        else:
            node.next = self.end.next
            self.end.next = node

        self.end = node
        self.size += 1

    def insert_position(self, e, pos):
        """
        inserts an element at the given position
        """
        node = Node(e, None)
        temp = self.start
        i = 1
        while 1 < pos:
            temp = temp.next
            i += 1
        node.next = temp.next
        temp.next = node
        self.size += 1

    def delete(self):
        """
        deletion of an element from the start
        """
        if self.is_Empty():
            print("Empty List")
        head = self.end.next
        self.end.next = head.next
        self.start = head.next
        self.size -= 1

        if self.is_Empty():
            self.end = None
        return head.data

    def display_list(self):
        """
        displays current linked list
        """
        temp = self.start
        i = 0
        while i < len(self):
            print(temp.data, end=" ")
            temp = temp.next
            i += 1

    @staticmethod
    def get_code():
        """
        :return: source code
        """
        return inspect.getsource(CircularList)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """

        return "Insertion at Start : O(1) ,"\
            "Insertion at End   : O(1) ,"\
            "Insertion at Position : O(n) ,"\
            " Deletion of node : O(1)"


class Stack_LinkedList(object):
    """
    Stack Using Linked List
    """

    def __init__(self):
        """
        :param start: Head of the node
        """
        self.start = None

    def push(self, ele):
        """
        for pushing the element into the stack
        """
        node = Node(ele)
        if self.start == None:
            self.start = node
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def pop(self):
        """
        for poping out the element
        """
        if self.isEmpty():
            return print("Empty Stack")

        n = self.start
        while n.next.next is not None:
            n = n.next
        print("deleted ele", n.next.data)
        n.next = None

    def isEmpty(self):
        """
        checks whether stack is empty or not
        """
        if self.start == None:
            return True
        else:
            return False

    def tos(self):
        """
        tos = top of stack ,
        to find the value of the top most element in the stack
        """
        if self.isEmpty():
            print("Empty Stack")

        else:
            n = self.start
            while n.next.next != None:
                n = n.next
            print("Top Element ", n.next.data)

    def display_stack(self):
        """
        displays full stack
        """
        if self.isEmpty():
            print("Empty Stack")
        else:
            temp = self.start
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

    def size(self):
        """
        returns size of the stack
        """
        curr = self.start
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    @staticmethod
    def get_code():
        """
        :return: source code
        
        """
        return inspect.getsource(Stack_LinkedList)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """

        return " Insertion : O(1) ,"\
               " Deletion of node : O(1)"


class Queue_LinkedList(object):
    """
    Implementation of queue uisng linked list
    """

    def __init__(self):
        """
        :param start: Head of the node
        """
        self.start = None

    def enqueue(self, ele):
        """
        for pushing the element into the queue
        """
        node = Node(ele)
        if self.start == None:
            self.start = node
        else:
            node.next = self.start
            self.start = node

    def dequeue(self):
        """
        for poping out the element
        """
        if self.start == None:
            print("list has no elements")
            return
        n = self.start
        while n.next.next != None:
            n = n.next
        print("deleted ele", n.next.data)
        n.next = None

    def display_queue(self):
        """
        displays full queue
        """
        if self.start == None:
            print("Empty Queue,Entre Value")
            return True
        else:
            temp = self.start
            while temp:
                print(temp.data, end=" ")
                temp = temp.next

    def isEmpty(self):
        """
        checks whether queue is empty or not
        """
        if self.start == None:
            return True
        else:
            return False

    def last_element(self):
        """
        to find the value of the last most element in the queue
        """
        if self.isEmpty():
            print("Empty Queue")
        else:
            n = self.start
            while n.next.next != None:
                n = n.next
            print("Last Element ", n.next.data)

    def size(self):
        """
        returns size of the queue
        """
        curr = self.start
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    @staticmethod
    def get_code():
        """
        :return: source code
        """
        return inspect.getsource(Queue_LinkedList)

    @staticmethod
    def time_complexity():
        """
        :return: time complexity
        """

        return " Insertion : O(1) ,"\
               " Deletion of node : O(1)"
