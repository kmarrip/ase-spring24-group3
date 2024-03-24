# import math

# class RANGE:
#     def __init__(self, at, txt, lo, hi=None):
#         self.at = at
#         self.txt = txt
#         self.scored = 0
#         self.x = {'lo': lo, 'hi': hi or lo}
#         self.y = {}

#     def add(self, x, y):
#         self.x['lo'] = min(self.x['lo'], x)
#         self.x['hi'] = max(self.x['hi'], x)
#         self.y[y] = self.y.get(y, 0) + 1

#     def show(self):
#         lo, hi, s = self.x['lo'], self.x['hi'], self.txt
#         if lo == -math.inf:
#             return f"{s} < {hi}"
#         if hi == math.inf:
#             return f"{s} >= {lo}"
#         if lo == hi:
#             return f"{s} == {lo}"
#         return f"{lo} <= {s} < {hi}"

#     def score(self, goal, LIKE, HATE):
#         return l.score(self.y, goal, LIKE, HATE)

#     def merge(self, other):
#         both = RANGE(self.at, self.txt, self.x['lo'])
#         both.x['lo'] = min(self.x['lo'], other.x['lo'])
#         both.x['hi'] = max(self.x['hi'], other.x['hi'])
#         for t in [self.y, other.y]:
#             for k, v in t.items():
#                 both.y[k] = both.y.get(k, 0) + v
#         return both

#     def merged(self, other, tooFew):
#         both = self.merge(other)
#         e1, n1 = l.entropy(self.y)
#         e2, n2 = l.entropy(other.y)
#         if n1 <= tooFew or n2 <= tooFew:
#             return both
#         if l.entropy(both.y) <= (n1 * e1 + n2 * e2) / (n1 + n2):
#             return both


# def _ranges(cols, rowss):
#     t = []
#     for col in cols:
#         for range_ in _ranges1(col, rowss):
#             t.append(range_)
#     return t


# def _ranges1(col, rowss):
#     out, nrows = [], 0
#     for y, rows in rowss.items():
#         nrows += len(rows)
#         for row in rows:
#             x = row['cells'][col.at]
#             if x != "?":
#                 bin_ = col.bin(x)
#                 out.append(RANGE(col.at, col.txt, x))
#                 out[bin_ - 1].add(x, y)
#     out.sort(key=lambda a: a.x['lo'])
#     return out if col.has else _mergeds(out, nrows / the.bins)


# def _mergeds(ranges, tooFew):
#     i, t = 1, []
#     while i <= len(ranges):
#         a = ranges[i - 1]
#         if i < len(ranges):
#             both = a.merged(ranges[i], tooFew)
#             if both:
#                 a = both
#                 i += 1
#         t.append(a)
#         i += 1
#     if len(t) < len(ranges):
#         return _mergeds(t, tooFew)
#     for i in range(1, len(t)):
#         t[i].x['lo'] = t[i - 1].x['hi']
#     t[0].x['lo'] = -math.inf
#     t[-1].x['hi'] = math.inf
#     return t

import math

class Range:
    def __init__(self, at, txt, lo, hi=None):
        self.at = at
        self.txt = txt
        self.lo = lo if lo is not None else float('-inf')
        self.hi = hi if hi is not None else float('inf')
        self.scored = 0
        self.y = {}

    def add(self, x, y):
        self.x['lo'] = min(self.x['lo'], x)
        self.x['hi'] = max(self.x['hi'], x)
        self.y[y] = self.y.get(y, 0) + 1

    def show(self):
        if self.lo == float('-inf'):
            return f"{self.txt} < {self.hi}"
        elif self.hi == float('inf'):
            return f"{self.txt} >= {self.lo}"
        elif self.lo == self.hi:
            return f"{self.txt} == {self.lo}"
        else:
            return f"{self.lo} <= {self.txt} < {self.hi}"

    def score(self, goal, LIKE, HATE):
        like = self.y.get(goal, 0)
        hate = sum(self.y.values()) - like
        return like * like / (like + hate + 1e-31)

    def merge(self, other):
        new_range = Range(self.at, self.txt, min(self.lo, other.lo), max(self.hi, other.hi))
        new_range.y = {k: self.y.get(k, 0) + other.y.get(k, 0) for k in set(self.y) | set(other.y)}
        return new_range

    def merged(self, other, tooFew):
        combined = self.merge(other)
        e1 = self.entropy()
        e2 = other.entropy()
        n1 = sum(self.y.values())
        n2 = sum(other.y.values())
        if n1 <= tooFew or n2 <= tooFew:
            return combined
        if combined.entropy() <= (n1 * e1 + n2 * e2) / (n1 + n2):
            return combined
        return None

    def entropy(self):
        total = sum(self.y.values())
        return -sum(count / total * math.log(count / total) for count in self.y.values() if count != 0)

def _mergeds(ranges, too_few):
    i = 0
    t = []
    while i < len(ranges):
        a = ranges[i]
        if i < len(ranges) - 1:
            both = a.merged(ranges[i + 1], too_few)
            if both:
                a = both
                i += 1
        t.append(a)
        i += 1

    if len(t) < len(ranges):
        return _mergeds(t, too_few)

    for i in range(1, len(t)):
        t[i].lo = t[i - 1].hi
    t[0].lo = float('-inf')
    t[-1].hi = float('inf')

    return t

def ranges(cols, rowss):
    t = []
    for col in cols:
        ranges = _ranges1(col, rowss)
        t.extend(ranges)
    return t

def _ranges1(col, rowss):
    out = {}
    nrows = 0
    for y, rows in rowss.items():
        nrows += len(rows)
        for row in rows:
            x = row.cells[col.at]
            if x != "?":
                bin = col.bin(x)
                if bin not in out:
                    out[bin] = Range(col.at, col.txt, x)
                out[bin].add(x, y)

    out_list = list(out.values())
    out_list.sort(key=lambda range: range.lo)
    return out_list if col.has else _mergeds(out_list, nrows / settings['bins'])

# Assuming 'the.bins' is defined in the settings
settings = {'bins': 16}
