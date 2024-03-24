# import math
# from config import *

# class NUM:
#     def __init__(self, s=None, n=None):
#         self.txt = s or " "
#         self.at = n or 0
#         self.n = 0
#         self.mu = 0
#         self.m2 = 0
#         self.hi = -1E30
#         self.lo = 1E30
#         self.heaven = 0 if (s or "").find("-$") else 1

#     def add(self, x):
#         if x != "?":
#             self.n += 1
#             d = x - self.mu
#             self.mu += d / self.n
#             self.m2 += d * (x - self.mu)
#             self.lo = min(x, self.lo)
#             self.hi = max(x, self.hi)

#     def mid(self):
#         return self.mu

#     def div(self):
#         return 0 if self.n < 2 else math.sqrt(self.m2 / (self.n - 1))

#     def small(self):
#         return the.cohen * self.div()

#     def norm(self, x):
#         return x if x == "?" else (x - self.lo) / (self.hi - self.lo + 1E-30)

#     def dist(self, x, y):
#         if x == "?" and y == "?":
#             return 1

#         x, y = self.norm(x), self.norm(y)

#         if x == "?":
#             x = 1 if y < 0.5 else 0

#         if y == "?":
#             y = 1 if x < 0.5 else 0

#         return abs(x - y)

#     def bin(self, x):
#         tmp = (self.hi - self.lo) / (the.bins - 1)
#         return 1 if self.hi == self.lo else math.floor(x / tmp + 0.5) * tmp

#     def dist(self, x, y):
#         if x == "?" and y == "?":
#             return 1
#         x, y = self.norm(x), self.norm(y)
        
#         if x == "?":
#             x = 1 if y < 0.5 else 0
#         if y == "?":
#             y = 1 if x < 0.5 else 0
        
#         return abs(x - y)

import math
from config import *
class Num:
    def __init__(self, name, index):
        self.name = name  # Name of the column or the numeric feature
        self.index = index  # Position of the column in the dataset
        self.n = 0  # Number of items added
        self.mu = 0  # Mean of the added items
        self.m2 = 0  # Sum of squares of differences from the current mean
        self.lo = float('inf')  # Minimum value seen
        self.hi = float('-inf')  # Maximum value seen
        self.bins = 16  # Default number of bins, replace with `the.bins` if it's defined elsewhere
        # self.heaven = 0 if (name or "").find("-$") else 1
        self.heaven = 0 if name.endswith("-") else 1

    def add(self, x):
        """ Update the statistics for the column based on the new value x. """
        self.n += 1
        delta = x - self.mu
        self.mu += delta / self.n
        delta2 = x - self.mu
        self.m2 += delta * delta2
        self.lo = min(x, self.lo)
        self.hi = max(x, self.hi)

    def mid(self):
        """ Return the mean (midpoint) of the values seen so far. """
        return self.mu

    def div(self):
        """ Return the standard deviation of the values seen so far. """
        return (self.m2 / (self.n - 1)) ** 0.5 if self.n > 1 else 0

    def bin(self, x):
        """ Calculate the bin for a given value x. """
        width = (self.hi - self.lo) / (self.bins - 1) if self.hi != self.lo else 1
        return self.hi if self.hi == self.lo else int((x - self.lo) / width + 0.5) * width + self.lo
