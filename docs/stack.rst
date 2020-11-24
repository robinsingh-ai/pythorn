Stack
=====

Quick Start Guide
-----------------

.. code-block:: python


    # import the required data structure
    >>> from pythorn.data_structures.stack import Stack

    # creating a stack
    >>> a = Stack()

    # push elements
    >>> a.push(5)
    >>> a.push(20)
    >>> a.push(13)

    # displaying full stack
    >>> a.display()
    [5, 20, 13]

    # top element
    >>> a.tos()
    13

    # poping the element
    >>> a.pop()
    13
    >>> a.isEmpty()
    False



Stack Programs
--------------

.. automodule:: pythorn.data_structures.stack

    Stack
    -----

    .. autoclass:: Stack
       :members:


    Infix To Postfix
    ----------------

    Example :
        .. code-block:: python

            # importing Stack and Infix_Postfix
            >>> from pythorn.data_structures.stack import Stack 
            >>> from pythorn.data_structures.stack import Infix_Postfix

            # creating a stack
            >>> my_stack = Stack()

            # My Expression
            >>> my_exp = "a+c-*/dsefj-+//jk"

            # passing stack and expression to the Infix_Postfix class
            >>> infixpostfix = Infix_Postfix(my_exp,my_stack)
            >>> infixpostfix.infixToPostfix()
            'a c + * d s e f j / - - / j k / +'



    .. autoclass:: Infix_Postfix

       :members:


    Integer To Binary
    -----------------

    Example :
        .. code-block:: python

            # importing Stack and Integer_Binary
            >>> from pythorn.data_structures.stack import Stack 
            >>> from pythorn.data_structures.stack import Integer_Binary

            # creating a stack
            >>> my_stack = Stack()

            # My Number
            >>> my_num = 45

            # passing my_stack and my_num to the Integer_Binary class
            >>> integerbinary = Integer_Binary(my_num,my_stack)
            >>> integerbinary.IntegerBinary()
            '101101'
            

    .. autoclass:: Integer_Binary
        
       :members:




    








