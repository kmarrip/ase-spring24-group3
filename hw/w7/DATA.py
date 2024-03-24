from COLS import Cols
from ROW import Row
from utils import *
from config import *
from operator import itemgetter
from node_module import Node
import config

# class DATA:

#     def __init__(self, src, fun=None):
#         self.rows, self.cols = [], None
#         if isinstance(src, str):
#             csv(src, self.add)
#         else:
#             self.add(src, fun)

#     def add(self, r, fun=None):
#         row = r if isinstance(r, ROW) and r.cells else ROW(r)
#         if self.cols:
#             if fun:
#                 fun(self, row)
#             self.rows.append(self.cols.add(row))
#         else:
#             self.cols = COLS(row)

#     def mid(self, cols=None):
#         u = [col.mid() for col in (cols or self.cols.all)]
#         return ROW(u)

#     def div(self, cols=None):
#         u = [col.div() for col in (cols or self.cols.all)]
#         return ROW(u)

#     def small(self):
#         u = [col.small() for col in self.cols.all]
#         return ROW(u)

#     def stats(self, cols=None, fun=None, ndivs=None):
#         u = {".N": len(self.rows)}
#         for col in self.cols.y if cols is None else [self.cols.names[c] for c in cols]:
#             current_col = self.cols.all[col]
#             u[current_col.txt] = (
#                 round(getattr(current_col, fun or "mid")(), ndivs)
#                 if ndivs
#                 else getattr(current_col, fun or "mid")()
#             )
#         return u
   
#     def dist(self, row1, row2, cols = None):
#         n,d = 0,0
#         for index in cols or self.cols.x:
#             n = n + 1
#             d = d + cols[index].dist(row1.cells[index], row2.cells[index])**the['p']
#         return (d/n)**(1/the['p'])

#     def clone(self, init = {}):
#         data = DATA([self.cols.names])
#         _ = list(map(data.add, init))
#         return data


#     def farapart(self, data, a=None, sortp=False):
#             if isinstance(data,list):
#                 rows = data
#             else:
#                 rows = data.rows or self.rows
#             far = int(len(rows) * the.get("Far", 0.95))
#             evals = 1 if a else 2
#             a = a or any(rows).neighbors(self, rows)[far]
#             b = a.neighbors(self, rows)[far]
#             if sortp and b.d2h(self) < a.d2h(self):
#                 a,b=b,a
#             return a, b, a.dist(b,self),evals

#     def cluster(self, rows = None , min = None, cols = None, above = None):
#         rows = rows or self.rows
#         min  = min or len(rows)**the['min']
#         cols = cols or self.cols.x
#         node = { 'data' : self.clone(rows) }
#         if len(rows) >= 2*min:
#             left, right, node['A'], node['B'], node['mid'], _ = self.half(rows,cols,above)
#             node['left']  = self.cluster(left,  min, cols, node['A'])
#             node['right'] = self.cluster(right, min, cols, node['B'])
#         return node
    
#     def half(self, rows, sortp = False, before = None, evals = None):
#         evals = evals or 0
#         some = many(rows, min(the['Half'], len(rows)))
#         a, b, C, evals = self.farapart(some, before, sortp)

#         def d(row1, row2):
#             return row1.dist(row2, self)

#         def project(r):
#             return (d(r, a)**2 + C**2 - d(r, b)**2) / (2 * C)

#         sorted_rows = sorted(rows, key=project)
        
#         mid_index = len(sorted_rows) // 2
#         as_ = sorted_rows[:mid_index]
#         bs = sorted_rows[mid_index:]

#         return as_, bs, a, b, C, d(a, bs[0]), evals
    
#     def tree(self, sortp = False):
#         evals = 0
#         def _tree(data, above=None, lefts=None, rights=None, node=None):
#             nonlocal evals
#             node = NODE(data)

#             if len(data.rows) > 2 * (len(self.rows) ** 0.5):
#                 lefts, rights, node.left, node.right, node.C, node.cut, evals1 = self.half(data.rows, sortp, above)
#                 evals += evals1
#                 node.lefts = _tree(self.clone(lefts), node.left)
#                 node.rights = _tree(self.clone(rights), node.right)

#             return node

#         return _tree(self), evals
    
#     def branch(self, stop=None):
#         evals, rest = 1, []
#         stop = stop or (2 * (len(self.rows) ** 0.5))

#         def _branch(data, above=None, left=None, lefts=None, rights=None):
#             nonlocal evals, rest
#             if len(data.rows) > stop:
#                 lefts, rights, left, _, _, _, _ = self.half(data.rows, True, above)
#                 evals += 1
#                 rest.extend(rights)
#                 return _branch(self.clone(lefts), left)
#             else:
#                 return self.clone(data.rows), self.clone(rest), evals

#         return _branch(self)
class Data:
    def __init__(self, src):
        self.rows = []
        self.cols = None  # Will be set up upon the first call to `add`

        # Load data from a source which could be a file path (string) or a list of rows
        if isinstance(src, str):
            csv(src, self.add)
        else:
            for row in src:
                self.add(row)
    # class Data:
    # def __init__(self, src, func=None):
    #     """
    #     Initialization function for the data class
    #     Sets up rows and columns and calls to read in required values
    #     :param src: Either the csv filename or a list of rows
    #     :param func: An anonymous function, likely the function learn as of right now
    #     """
    #     self.rows = []
    #     self.cols = None
    #     if isinstance(src, str):
    #         # checks if src is a string
    #         self.process_file(src, func)
    #     ## else the scenario where source is a table already
    #     else:
    #         for x in src:
    #             self.add(x, func)
#     def __init__(self, src, fun=None):
#         self.rows, self.cols = [], None
#         if isinstance(src, str):
#             csv(src, self.add)
#         else:
#             self.add(src, fun)

#     def add(self, r, fun=None):
#         row = r if isinstance(r, ROW) and r.cells else ROW(r)
#         if self.cols:
#             if fun:
#                 fun(self, row)
#             self.rows.append(self.cols.add(row))
#         else:
#             self.cols = COLS(row)

    def add(self, row):
        # Convert the row to a Row object if it isn't already one
        # Assuming Row class is defined to handle row operations
        row_obj = row if hasattr(row, 'cells') else Row(row)

        if self.cols is None:
            # First row defines the columns
            # Assuming Cols class is defined to handle column operations
            self.cols = Cols(row_obj)
        else:
            # Update columns with the new row and store the row
            if callable(row_obj):  # If a function is provided, use it
                row_obj(self, row_obj)
            # self.cols.add(row_obj)
            self.rows.append(row_obj)
    # def add(self, t, func=None):
    #     """
    #     Function that adds rows and columns from the read csv
    #     :param t: t is the row to be added and should be passed as an array
    #     :param func: The anonymous function to be ran on each row before being added to a col
    #     :return: None
    #     """
    #     row = t if hasattr(t, 'cells') else Row(t)
    #     if self.cols is None:
    #         self.cols = Cols(row)
    #         # the following is not included in his lua code, but I believe we need it
    #         #self.rows.append((self.cols))
    #     else:
    #         if func is not None:
    #             # if the lambda function was passed to data
    #             func(self, row)
    #         self.rows.append(self.cols.add(row))

    def mid(self):
        # Calculate the mid value for each column
        return [col.mid() for col in self.cols.all]

    def div(self):
        # Calculate the diversity for each column
        return [col.div() for col in self.cols.all]

    def small(self):
        # Calculate the 'small' value for each column (mainly applicable to NUM columns)
        return [col.small() for col in self.cols.all]

    def stats(self, fun='mid', ndivs=None):
        # Generate statistics based on the specified function (default is 'mid')
        stats = {".N": len(self.rows)}
        for col in self.cols.all:
            # Use a dynamic function call; by default, it uses 'mid'
            stats[col.name] = round(getattr(col, fun)(), ndivs) if ndivs else getattr(col, fun)()
        return stats

    def clone(self, rows=None):
        # Create a new Data instance with the same column structure but potentially different rows
        new_data = Data([])
        new_data.cols = self.cols  # Share the same columns structure
        new_data.rows = rows if rows else list(self.rows)  # Copy rows if provided, else duplicate current rows
        return new_data
    
    def farapart(self, rows, sortp, a=None, b=None):
        far = int(len(rows) * 0.95)  # the_far = 0.95 as pre-defined
        evals = 1 if a else 2
        if not a:
            a = random.choice(rows).neighbors(self, rows)[far]
            # neighbors = sorted(rows, key=lambda x: a.dist(x, self))  # Assuming Row class has dist method
            b = a.neighbors(self, rows)[far]
        if sortp and b.d2h(self) < a.d2h(self):  # Assuming Row class has d2h method
            a, b = b, a
        return a, b, a.dist(b, self), evals
    
    # def farapart(self, rows, sortp = None, a = None):
    #     far = int((len(rows) * the.Far ) // 1) 
    #     evals = a and 1 or 2
    #     a = a or random.choice(rows).neighbors(self, rows)[far]
    #     b = a.neighbors(self, rows)[far]
    #     if sortp and b.d2h(self) < a.d2h(self):
    #         a, b = b, a
    #     return (a, b, a.dist(b, self), evals)

    def half(self, rows, sortp, before=None):
        some = random.sample(rows, min(len(rows), 256))  # the_half = 256 as pre-defined
        a, b, C, evals = self.farapart(some, sortp, before)

        def project(row):
            return (a.dist(row, self) ** 2 + C ** 2 - b.dist(row, self) ** 2) / (2 * C)

        sorted_rows = sorted(rows, key=project)
        mid = len(rows) // 2
        return sorted_rows[:mid], sorted_rows[mid:], a, b, C, project(sorted_rows[0]), evals

    def tree(self, sortp):
        def _tree(data, above=None):
            if len(data.rows) > 2 * math.sqrt(len(self.rows)):
                lefts, rights, _, _, _, _, evals1 = self.half(data.rows, sortp, above)
                node = Node(data)  # Assuming Node class is defined
                node.lefts = _tree(Data(lefts), lefts[0])
                node.rights = _tree(Data(rights), rights[0])
                return node, evals1
            return Node(data), 0  # Base case: no further division

        root, total_evals = _tree(self)
        return root, total_evals

    def branch(self, stop=None):
        stop = stop or 2 * math.sqrt(len(self.rows))
        def _branch(data, above=None):
            if len(data.rows) > stop:
                lefts, rights, _, _, _, _, evals1 = self.half(data.rows, True, above)
                best_half, evals2 = _branch(Data(lefts), lefts[0])
                rest = Data(rights)
                return best_half, rest, evals1 + evals2
            return data, Data([]), 1

        best, rest, total_evals = _branch(self)
        return best, rest, total_evals