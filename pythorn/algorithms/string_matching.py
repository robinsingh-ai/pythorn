"""
Author : Robin Singh

Programs List : 

1 . Knuth Morris Pratt String Matching Algorithm
2 . Naive Method 
3 . Rabin Karp String Matching Algorithm

"""

import inspect


class KnuthMorrisPratt(object):
    """
    Implementation Of KMP string Matching Algorithm
    """

    def __init__(self, string1, string2):
        """
        :parma string1: String which has to be matched
        :param string2: Main String from which string1 has to be matched
        """

        self.string1 = string1
        self.string2 = string2

    @staticmethod
    def prefix_generator(pattern, m, n):
        """
        utility function for generating prefix
        """
        prefix = [0] * len(pattern)
        while m != len(pattern):
            if pattern[m] == pattern[n]:
                n += 1
                prefix[m] = n
                m += 1
            elif n != 0:
                n = prefix[n - 1]
            else:
                prefix[m] = 0
                m += 1
        return prefix

    def knuth_morris_pratt(self):
        """
        
        :prints: prints the index if string is matched 
        """
        index = []
        m = 0
        n = 0
        prefix = KnuthMorrisPratt.prefix_generator(self.string1, m+1, n)
        while m != len(self.string2):
            if self.string2[m] == self.string1[n]:
                m += 1
                n += 1
            else:
                n = prefix[n - 1]
            if n == len(self.string1):
                index.append(m - n)
                n = prefix[n - 1]
            elif n == 0:
                m += 1
        for i in index:
            print(f"Pattern Found At Index :{i}")

    @staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return "Time Complexity : O(N)"

    @staticmethod
    def get_code():
        """
        
        :return: source code
        """
        return inspect.getsource(KnuthMorrisPratt)


class NaiveMethod(object):
    """
    Implementation Of Naive method string Matching Algorithm

    """

    def __init__(self, string1, string2):
        """
        :parma string1: String which has to be matched
        :param string2: Main String from which string1 has to be matched
        """

        self.string1 = string1
        self.string2 = string2

    def naive_method(self):
        """
        :prints: prints index if string is matched 
        """
        index = []
        for i in range(len(self.string2)):
            j = 0
            while (j < len(self.string1)):
                if (self.string2[i + j] != self.string1[j]):
                    break
                j += 1

            if (j == len(self.string1)):
                index.append(i)

        for i in range(len(index)):
            print(f"Found At Index : {index[i]}")

    @ staticmethod
    def time_complexity():
        """
        
        :return: time complexity
        """
        return "Time Complexity : O(NxM)"

    @ staticmethod
    def get_code():
        """


        :return: source code
        """
        return inspect.getsource(NaiveMethod)


class RabinKarp(object):
    """
    Implementation Of Rabin Karp method string Matching Algorithm
    """

    def __init__(self, string1, string2):
        """
        :parma string1: String which has to be matched
        :param string2: Main String from which string1 has to be matched
        """

        self.string1 = string2
        self.string2 = string1
        self.base = 10  # Here We have taken base = 10
        # choose a prime number (here 7) in such a way that we can perform all the calculations with single-precision arithmetic
        self.primeNumber = 7

    def rabin_karp(self):
        """
        :prints: prints index if string exists 
        """
        h = pow(self.base, len(self.string2)-1) % self.primeNumber
        p = 0
        t = 0
        index = []
        for i in range(len(self.string2)):
            p = (self.base*p+ord(self.string2[i])) % self.primeNumber
            t = (self.base*t+ord(self.string1[i])) % self.primeNumber
        for s in range(len(self.string1)-len(self.string2)):
            if p == t:
                found = True
                for i in range(len(self.string2)):
                    if self.string2[i] != self.string1[s+i]:
                        found = False
                        break
                if found:
                    index = index + [s]
            # calculate hash value for next pattern
            if s < len(self.string1)-len(self.string2):
                # will remove first alphabet value
                t = (t-h*ord(self.string1[s])) % self.primeNumber
                # will add next alphabet
                t = (t*self.base +
                     ord(self.string1[s+len(self.string2)])) % self.primeNumber
                t = (t+self.primeNumber) % self.primeNumber

        if len(index) != 0:
            for i in range(len(index)):
                print(f"Found At Index : {index[i]}")
        else:
            print("patterns Not exists")

    @ staticmethod
    def time_complexity():
        """
        :return: time complexity
        """
        return "Time Complexity : Average Case = Best Case = O(length(Patter)+(length(String))) , "\
            "Worst Case = O(length(Patter)*length(String))"

    @ staticmethod
    def get_code():
        """


        :return:source code
        """
        return inspect.getsource(RabinKarp)
