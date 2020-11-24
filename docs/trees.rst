Trees
======


Quick Start Guide
------------------



.. code-block:: python
    

    # import required algorithm
    >>> from package.pygostructures.data_structures.trees import BinarySearchTree

    # creating BST
    >>> bst = BinarySearchTree()

    # insert value to be inserted
    >>> bst.insert(5)
    >>> bst.insert(7)
    >>> bst.insert(3)
    >>> bst.insert(6)
    >>> bst.insert(20)
    >>> bst.insert(19)
    >>> bst.insert(0)
    >>> bst.insert(1)
    >>> bst.insert(100)
    >>> bst.insert(111)

    # check if give argument is present in the bst
    >>> bst.search(19)
    True
    >>> bst.search(50)
    False

    # performs inorder traversal
    >>> bst.inorder(bst.root)
    0-->1-->3-->5-->6-->7-->19-->20-->100-->111

    # performs preorder traversal
    >>> bst.preorder(bst.root)
    5-->3-->0-->1-->7-->6-->20-->19-->100-->111

    # performs postorder
    >>> bst.postorder(bst.root)
    1-->0-->3-->6-->19-->111-->100-->20-->7-->5



Trees Programs
--------------


.. automodule:: pythorn.data_structures.trees

    Binary Search Tree
    ------------------

    .. autoclass:: BinarySearchTree
       :members:
