# import math
# from config import *


# def customsort(t, fun):
#     u, v = [], []
#     for x in t:
#         u.append({'x': x, 'y': fun(x)})
#     u.sort(key=lambda a: a['y'])
#     for xy in u:
#         v.append(xy['x'])
#     return v

# class ROW:
#     k = 1

#     def __init__(self, t):
#         self.cells = t

#     def d2h(self, data):
#         d, n = 0, 0
#         for col in data.cols.y.values():
#             n += 1
#             d += (col.heaven - col.norm(self.cells[col.at])) ** 2
#         return math.sqrt(d) / math.sqrt(n)

#     def likes(self, datas):
#         n, nHypotheses = 0, 0
#         for k, data in datas.items():
#             n += len(data.rows)
#             nHypotheses += 1
#         most, out = None, None
#         for k, data in datas.items():
#             tmp = self.like(data, n, nHypotheses)
#             if most is None or tmp > most:
#                 most, out = tmp, k
#         return out

#     def like(self, data, n, nHypotheses):
#         prior = (len(data.rows) + self.k) / (n + self.k * nHypotheses)
#         out = math.log(prior)
#         for col in data.cols.x:
#             v = self.cells[col]
#             currentCOL = data.cols.all[col]
#             if v == "?":
#                 continue
#             inc = currentCOL.like(v, prior)
#             try:
#                 out += math.log(inc)
#             except ValueError:
#                 return 0.0
#         return math.exp(1) ** out

#     def dist(self, other, data):
#             d, n = 0, 0
#             p = the["p"]
#             for _, col in data.cols.x.items():
#                 n += 1
#                 d += (col.dist(self.cells[col.at], other.cells[col.at])) ** p
#             return (d / n) ** (1 / p)
        
#     def neighbors(self, data, rows=None):
#         if rows is None:
#             rows = data.rows
#         return customsort(rows, lambda row: self.dist(row, data))

import math
from config import *
class Row:
    def __init__(self, cells):
        self.cells = cells  # cells is expected to be a dictionary mapping column names/indices to values
#     def d2h(self, data):
#         d, n = 0, 0
#         for col in data.cols.y.values():
#             n += 1
#             d += (col.heaven - col.norm(self.cells[col.at])) ** 2
#         return math.sqrt(d) / math.sqrt(n)
    def d2h(self, data):
        """
        Calculate the 'distance to heaven' based on certain 'heavenly' values defined in the columns.
        """
        d, n = 0, 0
        for col in data.cols.y:  # Assuming 'y' cols are the target/dependent variables
            n += 1
            d += abs(col.heaven - col.norm(self.cells[col.index])) ** 2  # Assuming norm and heaven attributes exist
        return math.pow(d / n, 1 / 2) if n > 0 else float('inf')

# def d2h(self, data):
#         """
#         Function that returns the d2h (distance to heaven) value
#         :return: d2h
#         """
#         d, n = 0, 0
#         for col in data.cols.y:
#             n += 1
#             d += abs(col.heaven - col.norm(self.cells[col.at])) ** 2
#         return math.sqrt(d) / math.sqrt(n)

#     def dist(self, other, data):
#             d, n = 0, 0
#             p = the["p"]
#             for _, col in data.cols.x.items():
#                 n += 1
#                 d += (col.dist(self.cells[col.at], other.cells[col.at])) ** p
#             return (d / n) ** (1 / p)
 
    def dist(self, other, data, p=2):
        """
        Calculate the Minkowski distance between this row and another row.
        """
        d, n = 0, 0
        for col in data.cols.x:  # Assuming 'x' cols are the independent variables
            if col.index in self.cells and col.index in other.cells:
                n += 1
                d += math.pow(col.dist(self.cells[col.index], other.cells[col.index]), p)  # Assuming a dist method in col
        return math.pow(d / n, 1 / p) if n > 0 else float('inf')

    def neighbors(self, data, rows=None):
        """
        Find all neighbors in `rows`, sorted by distance to this row.
        """
        rows = rows or data.rows
        return sorted(rows, key=lambda row: self.dist(row, data))

# Assuming the `dist` method exists within the column definitions and that `norm` and `heaven` attributes are defined for relevant columns
