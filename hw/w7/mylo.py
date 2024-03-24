# import DATA
# def eg_branch():
#     d = DATA.new("../data/auto93.csv")

#     result = branch(d)
#     best, rest, evals = result.best, result.rest, result.evals

#     print(l_o(best['mid'].cells), l_o(rest['mid'].cells))
#     print(evals)

from DATA import Data
from SYM import Sym
from NUM import Num

import copy
import sys
import random
import math
# Where to store examples
eg = {}

# Utility functions
def fmt(string, *args):
    return string.format(*args)

# Example function implementations
def eg_oo():
    return {"a": 1, "b": 2, "c": 3, "d": {"e": 3, "f": 4}}

def eg_the(settings):
    # Assuming 'the' is similar to a settings dictionary in Python
    print(settings)
    return settings.get("help") is not None and settings.get("seed") is not None

def eg_help(settings):
    print("\n" + settings.get("_help", ""))

def eg_copy():
    t = {"a": 1, "b": {"c": [2, 3, [4, 5, 6]]}}
    u = copy.deepcopy(t)
    u["b"]["c"][0] = 4000
    return t["b"]["c"][0] != u["b"]["c"][0]

# Registering the examples
eg["oo"] = eg_oo
eg["the"] = eg_the
eg["help"] = eg_help
eg["copy"] = eg_copy

# Function to run a single example
def run(k, settings):
    if k not in eg:
        print(f"-- ERROR: unknown start up action [{k}]")
        return True

    oops = False
    try:
        result = eg[k](settings) if k in ["the", "help"] else eg[k]()
        if not result:
            oops = True
    except Exception as e:
        print(f"Exception during {k}: {e}", file=sys.stderr)
        oops = True

    print(fmt("# {} {}\n", "❌ FAIL" if oops else "✅ PASS", k))
    return oops

# Function to run all examples
def eg_all(settings):
    bad = 0
    for k in eg.keys():
        if k != "all":
            if run(k, settings):
                bad += 1
    print(fmt("# {} {} fail(s)\n", "❌ FAIL" if bad > 0 else "✅ PASS", bad))
    sys.exit(bad)

# Function to list all example names
def eg_egs():
    for k in eg.keys():
        print(fmt("python script.py -t {}", k))

def eg_sym():
    s = Sym()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        s.add(x)
    mode, e = s.mid(), s.div()
    print(mode, e)
    return 1.37 < e < 1.38 and mode == 1

def norm(mu=0, sd=1):
    R = random.random
    return mu + sd * math.sqrt(-2 * math.log(R())) * math.cos(2 * math.pi * R())

def eg_num():
    e = Num()
    for _ in range(1000):
        e.add(norm(10, 2))
    mu, sd = e.mid(), e.div()
    print(round(mu, 3), round(sd, 3))
    return 10 < mu < 10.1 and 2 < sd < 2.05

def eg_data(filename):
    n = 0
    d = Data(filename)
    for i, row in enumerate(d.rows, start=1):
        if i % 100 == 0:
            n += len(row)
            print(i, row)
    print(d.stats())
    return n == 63

def eg_stats(filename):
    d = Data(filename)
    stats = d.stats()
    print(stats)
    return stats == {"N": 398} 

def eg_sorted(data):
    data.sort_by_d2h()
    print(data.cols.names)  # Assuming a names attribute in cols
    for i, row in enumerate(data.rows):
        if i < 5 or i > len(data.rows) - 5:
            print(i + 1, row)  # Lua indexing starts at 1


def eg_dist(data):
    r1 = data.rows[0]
    rows = data.neighbors(r1)
    for i, row in enumerate(rows):
        if i % 30 == 0:
            print(i + 1, row.cells, round(row.dist(r1, data), 2))


def eg_far(data):
    a, b, C = data.farapart()
    print(a, b, C)


def eg_half(data):
    lefts, rights, left, right, C, cut = data.half()
    print(len(lefts), len(rights), left.cells, right.cells, C, cut)


def eg_tree(data):
    t, evals = data.tree()
    t.show()
    print(evals)

def eg_branch():
    d = Data("data/auto93.csv")
    best, rest, evals = d.branch()
    print(d.mid_cells(best), d.mid_cells(rest))
    print(evals)


def eg_doubletap():
    d = Data("data/auto93.csv")
    best1, rest, evals1 = d.branch(32)
    best2, _, evals2 = best1.branch(4)
    print(d.mid_cells(best2), d.mid_cells(rest))
    print(evals1 + evals2)


# def eg_bins():
#     d = Data("../data/auto93.csv")
#     best, rest = d.branch()
#     LIKE = best
#     HATE = slice_data(shuffle(rest), 0, 3 * len(LIKE))
#     t = []

#     # Assuming 'cols.x' and '_ranges1' are defined elsewhere in your Data class
#     for col in d.cols.x:
#         for range_item in d._ranges1(col, {"LIKE": LIKE, "HATE": HATE}):
#             print()
#             t.append(range_item)
#     t.sort(key=lambda item: d.score_range(item, LIKE, HATE), reverse=True)
#     max_score = d.score_range(t[0], LIKE, HATE)

#     print("\n#scores:\n")
#     for v in t[:10]:  # Assuming 'the.Beam' is equivalent to 10 here
#         if d.score_range(v, LIKE, HATE) > max_score * 0.1:
#             print(d.score_range(v, LIKE, HATE), v)


# Example settings
settings = {
    'seed': 31210,
    '_help': 'Example help text...'
}

# Set up
random.seed(settings['seed'])

# d = Data('data/auto93.csv')
# # Example usage
# if __name__ == '__main__':

#     eg_all(settings)
#     print(eg_sym())
#     print(eg_num())
#     print(eg_data("data/auto93.csv"))
#     print(eg_stats("data/auto93.csv"))
#     eg_sorted(d)
#     eg_dist(d)
#     eg_far(d)
#     eg_half(d)
#     eg_tree(d)
#     print("OUTPUT 1:\n")
#     eg_branch()
#     print("OUTPUT 2:\n")
#     eg_doubletap()
#     # eg_bins()


def run_examples():
    d = Data("data/auto93.csv")
    print("OUTPUT 1:\n")
    eg_branch()
    print("\n\nOUTPUT 2:\n")
    eg_doubletap()


# Execute the example functions
if __name__ == "__main__":
    run_examples()