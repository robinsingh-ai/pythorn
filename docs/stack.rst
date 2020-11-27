Stack
=====

Quick Start Guide
------------------
|br| `Stack`_ :- Stack is linear data structure which follows a particular order in which the operations are pewformed.The order maybe LIFO or FILO which Stands for "Last in First out" or "First in Last out" respectively.
|br| `Operations of Stack:-
|br| `Push`_ :- Inserts an element in the stack. Stack is said to be in Overflow condition if its full. 
|br| `Pop`_ :- Removes an item from the stack. The items are removed in opposite order they are inserted i.e item on the top is popped first and item on bottom is popped last. Stack is said to be in Underflow condition if its empty.
|br| `top`_ :- Returns top element of stack. 
|br| `isEmpty`_ :- Returns true if stack is empty, else returns false. 
|br| `Infix expression`_ :- The expression of the form a op(operator) b.When an operator is in between every pair of operands.
|br| `postfix expression`_ :- The expression of the form a b op. When an operator is follwed for every pair of operands. 

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



Example Code for Infix To Postfix
            .. code-block:: python

                # importing Stack and Infix_Postfix
                >>> from pythorn.data_structures.stack import Stack 
                from pythorn.data_structures.stack import Infix_Postfix

                # creating a stack
                my_stack = Stack()

                # My Expression
                my_exp = "a+c-*/dsefj-+//jk"

                # passing stack and expression to the Infix_Postfix class
                infixpostfix = Infix_Postfix(my_exp,my_stack)
                infixpostfix.infixToPostfix()
                'a c + * d s e f j / - - / j k / +'
                
                
Example Code for Integer To Binary
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
            


Stack Programs
--------------
.. automodule:: pythorn.data_structures.stack

    Stack
    -----

    .. autoclass:: Stack
       :members:


    Infix To Postfix
    ----------------
    
    .. autoclass:: Infix_Postfix
       :members:
    
    
        
            
    Integer To Binary
    -----------------
    
    .. autoclass:: Integer_Binary
       :members:
    

    

    




    








