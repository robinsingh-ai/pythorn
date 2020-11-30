Stack
=====


:Info: Stack docs
:Author: Gourav <gouravpatel11072@gmail.com>
:Date: 2020-11-30  (Mon, 30 Nov 2020) 
:Description: Added stack operations and infix to postfix.


Quick Start Guide
------------------
 
``stack`` :- Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).


A stack allows access to only one data item: the last item inserted. If you remove this item, you can access the next-to-last item inserted, and so on.


A stack is also a handy aid for algorithms applied to certain complex data structures. In "Binary Trees", we’ll see it used to help traverse the nodes of a tree.


Notice how the order of the data is reversed. Because the last item pushed is the first one popped.


commonly implemented with linked lists but can be made from arrays too.


operations of stack: pop(), push(), tos(), isEmpty(), display().
            

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


``Infix expression``:The expression of the form a op b. When an operator is in-between every pair of operands.


``Postfix expression``:The expression of the form a b op. When an operator is followed for every pair of operands.
            
            
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
            
    .. autoclass:: Integer_Binary
        :members:
    

    

    




    








