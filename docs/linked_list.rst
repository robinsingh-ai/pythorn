Linked List
===========

:Info: Linked List Docs
:Author: Robin Singh <robin25tech@gmail.com>
:Date: 2020-12-19  (Fri, 19 Dec 2020) 
:Description: Added Linked list documentaion with time complexity


Quick Start Guide
------------------

``Linked List`` :- Arrays had certain disadvantages as data storage structures. In an unordered array, searching is slow, whereas in an ordered array, insertion is slow. In both kinds of arrays, deletion is slow. Also, the size of an array can’t be changed after it’s created.


We’ll look at a data storage structure that solves some of these problems: the linked list. Linked lists are probably the second most commonly used general-purpose storage structures after arrays.


In a linked list, each data item is embedded in a link. A link is an object of a class called something like Link. Each Link object contains a reference (usually called next) to the next link in the list.


The LinkList class contains only one data item: a reference to the first link on the list. This reference is called first or``HEAD``. It’s the only permanent information the list maintains about the location of any of the links. It finds the other links by following the chain of references from first, using each link’s next field.


A linked list data structure includes a series of connected nodes. Here, each node store the data and the address of the next node.You have to start somewhere, so we give the address of the first node a special name called ``HEAD``.Also, the last node in the linked list can be identified because its next portion points to ``NULL``.


You might have played the game Treasure Hunt, where each clue includes the information about the next clue. That is how the linked list operates.




+------------------------+-----------------------------+
|   Linked List          |       Time Complexity       |
|                        |                             |
+========================+==============+==============+
|  Cases                 | Worst        | Average      |
+------------------------+--------------+--------------+
| Search                 | O(n)         | O(n)         |
+------------------------+--------------+--------------+
| Insert                 | O(1)         | O(1)         |
+------------------------+--------------+--------------+
| Deletion               | O(1)         | O(1)         |
+------------------------+--------------+--------------+



- Linked List Applications
   + Dynamic memory allocation
   + Implemented in stack and queue
   + In undo functionality of softwares
   + Hash tables, Graphs




### Basic Operations On Linked List

- Two important points to remember:

   + head points to the first node of the linked list
   + next pointer of the last node is NULL, so if the next current node is NULL, we have reached the end of the linked list.



In all of the examples, we will assume that the linked list has three nodes 1 --->2 --->3 with node structure as below:


- How to Traverse a Linked List
   + Displaying the contents of a linked list is very simple. We keep moving the temp node to the next one and display its contents.

   + When temp is ``NULL``, we know that we have reached the end of the linked list so we get out of the while loop.

   + The output of this program will be:
      ``1 --->2 --->3 --->``



- How to Add Elements to a Linked List

You can add elements to either the beginning, middle or end of the linked list.
   * Add to the beginning
      - Allocate memory for new node
      - Store data
      - Change next of new node to point to head
      - Change head to point to recently created node
      
   * Add to the End
      - Allocate memory for new node
      - Store data
      - Traverse to last node
      - Change next of last node to recently created node

   * Add to the Middle
      - Allocate memory and store data for new node
      - Traverse to node just before the required position of new node
      - Change next pointers to include new node in between

   
- How to Delete from a Linked List

You can delete either from the beginning, end or from a particular position.
   * Delete from beginning
      - Point head to the second node : ``head = head->next``

   * Delete from end
      - Traverse to second last element
      - Change its next pointer to null

   * Delete from middle
      - Traverse to element before the element to be deleted
      - Change next pointers to exclude the node from the chain



### Types of Linked List
- There are three common types of Linked List.

   * Singly Linked List
   - A singly linked list is a type of linked list that is unidirectional, that is, it can be traversed in only one direction from head to the last node (tail).

   - Each element in a linked list is called a node. A single node contains data and a pointer to the next node which helps in maintaining the structure of the list.

   * Doubly Linked List
      - Let’s examine another variation on the linked list: the doubly linked list (not to be confused with the double-ended list). What’s the advantage of a doubly linked list? A potential problem with ordinary linked lists is that it’s difficult to traverse backward along the list. A statement like current=current.next steps conveniently to the next link, but there’s no corresponding way to go to the previous link.

      - The doubly linked list provides this capability. It allows you to traverse backward as well as forward through the list. The secret is that each link has two references to other links instead of one. The first is to the next link, as in ordinary lists. The second is to the previous link.

   * Circular Linked List
      - A circular linked list is a variation of a linked list in which the last element is linked to the first element. This forms a circular loop.
      
      - A circular linked list can be either singly linked or doubly linked.

         * for singly linked list, next pointer of last item points to the first item
         * In the doubly linked list, ``prev`` pointer of the first item points to the last item as well.


Below is the sample example code of linked list using this package


.. code-block:: python

    # import the required data structure
    >>> from pythorn.data_structures.linked_list import SinglyList

    # creating linked list
    >>> a = SinglyList()

    # inserting element
    >>> a.insert(5)
    >>> a.insert(8)
    >>> a.insert(16)

    # displaying elements
    >>> a.display_list()
    16 8 5 

    # delete element
    >>> a.delete()
    16

    # size of the linked list
    >>> a.size()
    2
    >>> a.display_list()
    8 5 



Linked List Programs
--------------------

.. automodule:: pythorn.data_structures.linked_list

    Singly Linked List
    -----

    .. autoclass:: SinglyList
       :members:


    Doubly Linked List
    ----------


    .. autoclass:: DoublyList
       :members:




    CircularList
    -------


    .. autoclass:: CircularList
       :members:


    Stack Using Linked List
    ----------------


    .. autoclass:: Stack_LinkedList
       :members:


    Queue Using Linked List
    -------


    .. autoclass:: Queue_LinkedList
       :members:


    
