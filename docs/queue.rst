Queue
=====


Quick Start Guide
------------------


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


    
