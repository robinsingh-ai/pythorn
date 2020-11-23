"""
Author : Robin Singh
"""

import inspect


class Node(object):
    """
    Node Class for creating a node for the tree 

    :param element: node value
    :param left: left child of node
    :param right: right child of node


    """

    def __init__(self, ele):
        self.element = ele
        self.left = None
        self.right = None


class BinarySearchTree(object):
    """
    Binary Search Tree Funtion

    :param root: root node
    """

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, ele):
        """
        inserts a node into the tree
        """

        temp_root = self.root
        temp2_root = None

        while temp_root:
            temp2_root = temp_root
            if ele < temp_root.element:
                temp_root = temp_root.left

            elif ele > temp_root.element:
                temp_root = temp_root.right
        # Creating a new node from Node class
        new_node = Node(ele)
        if self.root:
            if ele < temp2_root.element:
                temp2_root.left = new_node

            else:
                temp2_root.right = new_node
        else:
            self.root = new_node

    def search(self, k):
        """
        Function for searching an given element

        :return: true if element is present else return false
        """

        temp = self.root
        while temp:
            if k < temp.element:
                temp = temp.left

            elif k > temp.element:
                temp = temp.right

            else:

                return True

        return False

    def inorder(self, temp):
        """
        here we first traverse to the leftmost node and
        then print the data and then move to the rightmost child

        :param temp: root node
        """
        if temp:
            self.inorder(temp.left)
            print(temp.element, end="-->")
            self.inorder(temp.right)

    def preorder(self, temp):
        """
        here we first print the root node and then
        traverse towards leftmost node and then to the rightmost node

        :param temp: root node
        """
        if temp:
            print(temp.element, end="-->")
            self.preorder(temp.left)
            self.preorder(temp.right)

    def postorder(self, temp):
        """
        here we first traverse to the leftmost node
        and then to the rightmost node and then print the data

        :param temp: root node

        """
        if temp:

            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.element, end="-->")

    @staticmethod
    def get_code():
        """

        :return: source code
        """
        return inspect.getsource(BinarySearchTree)

    @staticmethod
    def time_complexity():
        """

        :return: time complexity
        """

        return "Time complexity of all BST Operations = O(h),  Here, h = Height of binary search tree"\
            "in worst case : The binary search tree is a skewed binary search tree, "\
            "Height of the binary search tree becomes n."\
            "So, Time complexity of BST Operations = O(n)"
