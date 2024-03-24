# from utils import *
# class NODE:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.C = None
#         self.cut = None
#         self.lefts = None
#         self.rights = None


#     def walk(self, fun, depth=0):
#         fun(self, depth, not (self.lefts or self.rights))
#         if self.lefts:
#             self.lefts.walk(fun, depth + 1)
#         if self.rights:
#             self.rights.walk(fun, depth + 1)

#     def show(self):
#         def d2h(data):
#             return rnd(data.mid().d2h(self.data))

#         maxDepth = 0

#         def _show(node, depth, leafp):
#             nonlocal maxDepth
#             post = leafp and (str(d2h(node.data)) + "\t" + str(modifyValues(node.data.mid().cells))) or ""
#             maxDepth = max(maxDepth, depth)
#             print(('|.. ' * depth) + post)

#         self.walk(_show)
#         print("")
#         print(("    " * maxDepth) + str(d2h(self.data)) , modifyValues(self.data.mid().cells))
#         print(("    " * maxDepth) + "_" + "\t" + modifyValues(self.data.cols.names))

from utils import *
class Node:
    def __init__(self, data, cols=None):
        self.here = data  # Data associated with this node
        self.cols = cols  # Assuming cols is a structure with names and potentially more data
        self.lefts = None  # Left child node
        self.rights = None  # Right child node

    def walk(self, func, depth=0):
        """
        Traverse the tree, applying 'func' to each node.
        """
        func(self, depth, not (self.lefts or self.rights))
        if self.lefts:
            self.lefts.walk(func, depth + 1)
        if self.rights:
            self.rights.walk(func, depth + 1)

    def show(self):
        max_depth = [0]  # Using a list to be mutable in nested function

        def d2h(data):
            # Assuming data has a mid() method that returns an object with a d2h method.
            return round(data.mid().d2h(self.here), ndigits=2)

        def _show(node, depth, leafp):
            # Only use d2h for leaf nodes
            post = f"{d2h(node.here)}" if leafp else ""
            max_depth[0] = max(max_depth[0], depth)
            print(('|.. ' * depth) + post)

        self.walk(_show)  # Walk the tree and print each node
        print("\n" + ("    " * max_depth[0]), end="")
        print(d2h(self.here))  # Print the d2h value for the root node
        if self.cols:  # If column names or additional data structure is provided
            print(("    " * max_depth[0]) + "_", self.cols)
