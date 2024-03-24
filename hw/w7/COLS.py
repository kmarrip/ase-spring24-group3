# from SYM import SYM
# from NUM import NUM


# class COLS:
#     def __init__(self, row):
#         self.x, self.y, self.all = {}, {}, []
#         self.klass, col = None, None
#         if len(row.cells) == 1:
#             row.cells = row.cells[0]
#         for at, txt in enumerate(row.cells):
#             col = (NUM if txt[0].isupper() else SYM)(
#                 txt, at
#             )  # Instantiate NUM or SYM directly
#             self.all.append(col)
#             # this is guard statement for the txt ending with X
#             if txt.endswith("X"):
#                 continue

#             # if txt ends with !, it should be the final class of the row
#             if txt.endswith("!"):
#                 self.klass = col
#             # if txt ends with these, it will be y class
#             if txt.endswith(("!", "+", "-")):
#                 self.y[at] = col
#             else:
#                 self.x[at] = col
#         self.names = row.cells

#     def add(self, row):
#         # add new data to cols
#         for cols in [self.x.values(), self.y.values()]:
#             for col in cols:
#                 col.add(row.cells[col.at])
#         return row

# class Cols:
#     def __init__(self, row):
#         """
#         Initialization function for the cols class
#         Sets up columns
#         :param row: the column names in a the form of a array
#         """
#         self.x = []
#         self.y = []
#         self.all = []
#         self.klass = None
#         self.names = row.cells
#         for idx, cell in enumerate(row.cells):
#             col = Num(cell,idx) if re.match("^[A-Z]",cell) else Sym(cell,idx)
#             self.all.append(col)
#             if not cell.endswith("X"):
#                 if cell.endswith("!"):
#                     self.klass = col
#                 if cell.endswith("!") or cell.endswith("+") or cell.endswith("-"):
#                     self.y.append(col)
#                 else:
#                     self.x.append(col)
    
#     def add(self, row):
#         """
#         Function that adds rows 
#         :param row: row is the row to be added and should be passed as an Row object
#         :return: None
#         """
#         for _, cols in enumerate([self.x, self.y]):
#             for col in cols:
#                 col.add(row.cells[col.at])
        
#         return row

from SYM import Sym
from NUM import Num
class Cols:
    def __init__(self, row):
        self.x = []  # Independent variables
        self.y = []  # Dependent variables
        self.all = []  # All columns
        self.klass = None  # Class column
        self.names = row.cells  # Keeping the original names for reference

        for at, name in enumerate(row.cells):
            # Determine if the column is NUM or SYM based on the name's case
            col = Num(name, at) if name.isupper() else Sym(name, at)

            # Keep track of all columns
            self.all.append(col)
            if "X" not in name[-1]:  # Skip columns ending with 'X'
                if any(suffix in name[-1] for suffix in "!+-"):
                    self.y.append(col)  # Dependent variable
                    if "!" in name[-1]:
                        self.klass = col  # Class column
                else:
                    self.x.append(col)  # Independent variable

    def add(self, row):
        # Update each column with data from a new row
        for _, cols in enumerate([self.x, self.y]):
            for col in cols:
                value = row.cells[col.index]  # Get value from row corresponding to column's index
                col.add(value)
              
#     def add(self, row):
#         """
#         Function that adds rows 
#         :param row: row is the row to be added and should be passed as an Row object
#         :return: None
#         """
#         for _, cols in enumerate([self.x, self.y]):
#             for col in cols:
#                 col.add(row.cells[col.at])
        
#         return row
# class Cols:
#     def __init__(self, row):
#         """
#         Initialization function for the cols class
#         Sets up columns
#         :param row: the column names in a the form of a array
#         """
#         self.x = []
#         self.y = []
#         self.all = []
#         self.klass = None
#         self.names = row.cells
#         for idx, cell in enumerate(row.cells):
#             col = Num(cell,idx) if re.match("^[A-Z]",cell) else Sym(cell,idx)
#             self.all.append(col)
#             if not cell.endswith("X"):
#                 if cell.endswith("!"):
#                     self.klass = col
#                 if cell.endswith("!") or cell.endswith("+") or cell.endswith("-"):
#                     self.y.append(col)
#                 else:
#                     self.x.append(col)
    
#     def add(self, row):
#         """
#         Function that adds rows 
#         :param row: row is the row to be added and should be passed as an Row object
#         :return: None
#         """
#         for _, cols in enumerate([self.x, self.y]):
#             for col in cols:
#                 col.add(row.cells[col.at])
        
#         return row