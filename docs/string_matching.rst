String Matching
===============


Quick Start Guide
------------------








String Matching Algorithms
--------------------------


.. automodule:: pythorn.algorithms.string_matching

   Knuth Morris Pratt
   ------------------


   Example :
        .. code-block:: python

            # import required algorithm
            >>> from package.pygostructures.algorithms.string_matching import KnuthMorrisPratt

            # string to be searched
            >>> string1 = "csk"
            
            # main string from which string 1 has to be searched
            >>> string2 = "jadhgdajdkcsklsdhajhd"


            >>> a = KnuthMorrisPratt(string1,string2)

            >>> a.knuth_morris_pratt()
            Pattern Found At Index :10
         
   .. autoclass:: KnuthMorrisPratt
      :members:

      
   Naive Method
   -------------


   Example :
        .. code-block:: python

            # import required algorithm
            >>> from pythorn.algorithms.string_matching import NaiveMethod

            # string to be searched
            >>> string1 = "in"
            
            # main string from which string 1 has to be searched
            >>> string2 = "djhdjhdinqwert"


            >>> a = NaiveMethod(string1,string2)

            >>> a.naive_method()
            Pattern Found At Index :7
         
   .. autoclass:: NaiveMethod
      :members:


   Rabin Karp
   ----------


   Example :
        .. code-block:: python

            # import required algorithm
            >>> from pythorn.algorithms.string_matching import RabinKarp

            # string to be searched
            >>> string1 = "in"
            
            # main string from which string 1 has to be searched
            >>> string2 = "djhdjhdinqwert"


            >>> a = RabinKarp(string1,string2)

            >>> a.rabin_karp()
            Pattern Found At Index :7
         
   .. autoclass:: RabinKarp
      :members:
   