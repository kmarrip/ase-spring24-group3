# import math
# from config import *

# class SYM:
#     m = 0
#     def __init__(self, s=None, n=None):
#         self.txt = s or " "
#         self.at = n or 0
#         self.n = 0
#         self.has = (
#             {}
#         )  # this is a dictionary to keep track of the frequencies of the symbols
#         self.mode = None  # this is the symbol which repeats the most
#         self.most = 0  # this is the frequency of the most repeating symbol

#     def add(self, x):
#         if x != "?":
#             self.n += 1
#             self.has[x] = 1 + self.has.get(x, 0)
#             if self.has[x] > self.most:
#                 self.most, self.mode = self.has[x], x

#     def mid(self):  # mid for symbols is mode itself
#         return self.mode

#     def div(self):
#         e = 0
#         for v in self.has.values():
#             e -= v / self.n * math.log(v / self.n, 2)
#         return e

#     def small(self):
#         return 0

#     def like(self, x, prior):
#         if self.n + the["m"] == 0:
#             return 0
#         return (self.has.get(x, 0) + the["m"] * prior) / (self.n + the["m"])

#     def dist(self, x, y):
#         return 1 if x == "?" and y == "?" else 0 if x == y else 1
    
import math
from config import *
class Sym:
    def __init__(self, name, index):
        self.name = name or " "
        self.index = index or 0
        self.n = 0  # Number of items added
        self.has = {}
        self.mode = None  # Most frequent symbol
        self.most = 0  # Frequency of the most frequent symbol

#def __init__(self, s=" ", n=0):
        # """
        # Initialization function for the Sym class
        # Sets up the column name, column index, number of rows and data aggregates
        # :param s: column name, n: column index
        # """
        # self.txt = s
        # self.at = n
        # self.n = 0 #  testing
        # self.has = {}
        # self.mode = None
        # self.most = 0      
        
    def add(self, x):
        """ Update the frequency table with a new value x. """
        if x != "?":
            self.n += 1
            self.has[x] = 1 + self.has.get(x, 0)
            if self.has[x] > self.most:
                self.most, self.mode = self.has[x], x
#     def add(self, x):
#         if x != "?":
#             self.n += 1
#             self.has[x] = 1 + self.has.get(x, 0)
#             if self.has[x] > self.most:
#                 self.most, self.mode = self.has[x], x

    def mid(self):
        """ Return the most frequent symbol (mode). """
        return self.mode

    def div(self):
        """ Calculate the entropy of the symbols seen so far. """
        total = sum(self.has.values())
        entropy = sum((-count / total) * math.log2(count / total) for count in self.has.values())
        return entropy

    def small(self):
        """ Placeholder method, as 'small' is not typically relevant for symbolic attributes. """
        return 0

    def dist(self, x, y):
        """ Calculate the distance between two symbols. """
        if x == "?" and y == "?":
            return 1
        return 0 if x == y else 1

    def bin(self, x):
        """ Return the symbol itself, as discretization does not apply to symbolic attributes. """
        return x