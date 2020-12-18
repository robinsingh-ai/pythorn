Queue
=====


:Info: Queue Docs
:Author: Robin Singh <robin25tech@gmail.com>
:Date: 2020-12-18  (Fri, 18 Dec 2020) 
:Description: Added queue docs with full descriptions



Quick Start Guide
------------------

``Queue`` :- A queue is a data structure that is some- what like a stack, except that in a queue the first item inserted is the first to be removed (First-In-First-Out, `FIFO`), while in a stack, as we’ve seen, the last item inserted is the first to be removed (`LIFO`).


too can be implemented with a linked list or an array.
  - Queues are a **first in, first out** (FIFO) data structure.
  - Made with a doubly linked list that only removes from head and adds to tail.  


In programming terms, putting an item in the queue is called an "enqueue" and removing an item from the queue is called "dequeue".


We can implement the queue in any programming language like C, C++, Java, Python or C#, but the specification is pretty much the same.

### Basic Operations of Queue


A queue is an object or more specifically an abstract data structure(ADT) that allows the following operations:

   - Enqueue: Add an element to the end of the queue
   - Dequeue: Remove an element from the front of the queue
   - IsEmpty: Check if the queue is empty
   - IsFull: Check if the queue is full
   - Peek: Get the value of the front of the queue without removing it



### Working of Queue
Queue operations work as follows:

   - two pointers ``FRONT`` and ``REAR``
   - ``FRONT`` track the first element of the queue
   - ``REAR`` track the last elements of the queue
   - initially, set value of ``FRONT`` and ``REAR`` to -1

#### Enqueue Operation
   - check if the queue is full
   - for the first element, set value of ``FRONT`` to 0
   - increase the ``REAR`` index by 1
   - add the new element in the position pointed to by ``REAR``

#### Dequeue Operation
   - check if the queue is empty
   - return the value pointed by ``FRONT``
   - increase the ``FRONT`` index by 1
   - for the last element, reset the values of ``FRONT`` and ``REAR`` to -1

#### Limitation of Queue
   - As you can see in the image below, after a bit of enqueuing and dequeuing, the size of the queue has been reduced.
   - The indexes 0 and 1 can only be used after the queue is reset when all the elements have been dequeued.
   - After REAR reaches the last index, if we can store extra elements in the empty spaces (0 and 1), we can make use of the empty spaces. This is implemented by a modified queue called the Circular queue


#### Applications of Queue Data Structure
   - CPU scheduling, Disk Scheduling
   - When data is transferred asynchronously between two processes.The queue is used for synchronization. eg: IO - Buffers, pipes, file IO, etc
   - Handling of interrupts in real-time systems.
   - Call Center phone systems use Queues to hold people calling them in an order



### Types of queue
``Simple Queue`` :- In a simple queue, insertion takes place at the rear and removal occurs at the front. It strictly follows FIFO rule.


``Circular Queue`` :- In a circular queue, the last element points to the first element making a circular link.The main advantage of a circular queue over a simple queue is better memory utilization. If the last position is full and the first position is empty then, an element can be inserted in the first position. This action is not possible in a simple queue.


#### How Circular Queue Works
   - Circular Queue works by the process of circular increment i.e. when we try to increment the pointer and we reach the end of the queue, we start from the beginning of the queue.

#### Circular Queue Operations
The circular queue work as follows:

   - two pointers ``FRONT`` and ``REAR``
   - ``FRONT`` track the first element of the queue
   - ``REAR`` track the last elements of the queue
   - initially, set value of ``FRONT`` and ``REAR`` to -1


#### Enqueue Operation
   - check if the queue is full
   - for the first element, set value of ``FRONT`` to 0
   - circularly increase the ``REAR index by 1 (i.e. if the rear reaches the end, next it would be at the start of the queue)
   - add the new element in the position pointed to by ``REAR``


#### Dequeue Operation
   - check if the queue is empty
   - return the value pointed by ``FRONT``
   - circularly increase the ``FRONT`` index by 1
   - for the last element, reset the values of ``FRONT`` and ``REAR`` to -1
   - However, the check for full queue has a new additional case:
   - Case 1: ``FRONT`` = 0 && ``REAR`` == SIZE - 1
   - Case 2: ``FRONT`` = ``REAR`` + 1
   - The second case happens when REAR starts from 0 due to circular increment and when its value is just 1 - less than ``FRONT``, the queue is full.


#### Applications of Circular Queue
   - CPU scheduling
   - Memory management
   - Traffic Management





``Deque (Double Ended Queue)`` :- Double Ended Queue is a type of queue in which insertion and removal of elements can be performed from either from the front or rear. Thus, it does not follow FIFO rule (First In First Out).



### Types of Deque
   - Input Restricted Deque
   - In this deque, input is restricted at a single end but allows deletion at both the ends.
   - Output Restricted Deque
   - In this deque, output is restricted at a single end but allows insertion at both the ends.


### Operations on a Deque
   - Below is the circular array implementation of deque. In a circular array, if the array is full, we start from the beginning.
   - But in a linear array implementation, if the array is full, no more elements can be inserted. In each of the operations below, if the array is full, "overflow message" is thrown.
   - Before performing the following operations, these steps are followed.
   - Take an array (deque) of size n.
   - Set two pointers at the first position and set front = -1 and rear = 0.


#### Insert at the Front
This operation adds an element at the front.

   - Check the position of front.
   - If ``front < 1``, reinitialize ``front = n-1`` (last index)
   - Else, decrease ``front`` by 1
   - Add the new key ``5`` into ``array[front]``


#### Insert at the Rear
This operation adds an element to the rear.

   - Check if the array is full
   - If the deque is full, reinitialize ``rear = 0``
   - Else, increase ``rear`` by 1.
   - Add the new key ``5`` into ``array[rear]``

#### Delete from the Front
The operation deletes an element from the front.

   - Check if the deque is empty
   - If the deque is empty (i.e. ``front = -1``), deletion cannot be performed (underflow condition).
   - If the deque has only one element (i.e. front = rear), set front = -1 and rear = -1.
   - Else if front is at the end (i.e. ``front = n - 1``), set go to the front ``front = 0``.
   - Else, ``front = front + 1``


#### Delete from the Rear
This operation deletes an element from the rear.

   - Check if the deque is empty
   - If the deque is empty (i.e. ``front = -1``), deletion cannot be performed (underflow condition).
   - If the deque has only one element (i.e. ``front = rear``), set ``front = -1`` and ``rear = -1``, else follow the steps below.
   - If rear is at the front (i.e. ``rear = 0``), set go to the ``front rear = n - 1``
   - Else, ``rear = rear - 1``



#### Check Empty
   - This operation checks if the deque is empty. If ``front = -1``, the deque is empty.


#### Check Full
   - This operation checks if the deque is full. If ``front = 0`` and ``rear = n - 1`` OR ``front = rear + 1``, the deque is full.


#### Applications of Deque Data Structure
   - In undo operations on software.
   - To store history in browsers.
   - For implementing both stacks and queues.

 


### Time Complexity
The time complexity of all the above methods and operations is constant i.e. O(1). 




Below is the simple example for how to use queue using this package.



.. code-block:: python

    # import the required data structure
    >>> from pythorn.data_structures.queue import Queue

    # creating a stack
    >>> a = Queue()

    # enqueue elements
    >>> a.enqueue(5)
    >>> a.enqueue(13)
    >>> a.enqueue(27)

    # display elements
    >>> a.display()
    [5, 13, 27]

    # dequeue elements
    >>> a.dequeue()
    5
    >>> a.dequeue()
    13
    >>> a.display()
    [27]





Queue Programs
--------------

.. automodule:: pythorn.data_structures.queue

    Queue
    -----

    .. autoclass:: Queue
       :members:


    Circular Queue
    --------------


    .. autoclass:: CircularQueue
       :members:




    Dequeue
    --------------


    .. autoclass:: Deque
       :members:


    
