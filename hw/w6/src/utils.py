from os.path import exists
import sys
import re
from pathlib import Path
from config import *
import math
import random

def coerce(s):
    if s.isdigit():
        return int(s)
    elif '.' in s and s.replace('.', '').isdigit():
        return float(s)
    elif s.lower() == 'true':
        return True
    elif s.lower() == 'false':
        return False
    elif s.lower() == 'nil':
        return None
    else:
        return s.strip()

def settings(s):
    t = {}
    pat = r"[-][-]([\S]+)[^\n]+= ([\S]+)"
    return dict(re.findall(pat, s))


def cli(options):
    args = sys.argv[1:]
    for k, v in options.items():
        for n, x in enumerate(args):
            if x == '-' + k[0] or x == '--' + k:
                v = 'true' if v == 'false' else 'false' if v == 'true' else args[n + 1]
        options[k] = coerce(v)
    return options


def eg(key, str, fun):
    egs[key] = fun
    global help
    help = help + '  -g '+ key + '\t' + str + '\n'
    

def csv(sFilename, fun):
    sFilename = Path(sFilename)
    t = []
    with open(sFilename.absolute(), 'r', encoding='utf-8') as file:
        for line in file:
            row = list(map(coerce, line.strip().split(',')))
            t.append(row)
            fun(row)

def keysort(t, fun):
    u, v = [], []
    for x in t:
        u.append({'x': x, 'y': fun(x)})
    u.sort(key=lambda a: a['y'])
    for xy in u:
        v.append(xy['x'])
    return v

def o(t, n=None, u=None):
    if isinstance(t, (int, float)):
        return str(rnd(t, n))
    if not isinstance(t, dict):
        return str(t)
    if u is None:
        u = []
    for k in t.keys():
        if str(k)[0] != "_":
            if len(t) > 0:
                u.append(o(t[k], n))
            else:
                u.append(f"{o(k, n)}: {o(t[k], n)}")
    return "{" + ", ".join(u) + "}"

def rnd(n, ndecs=None):
    if not isinstance(n, (int, float)):
        return n
    if math.floor(n) == n:
        return n
    mult = 10**(ndecs or 2)
    return math.floor(n * mult + 0.5) / mult

def any(t):
    return t[random.randint(0, len(t) - 1)]

def cosine(a,b,c):
    den = 1 if c == 0 else 2*c
    x1 = (a**2 + c**2 - b**2) / den
    return x1

def many(t,n):
    u=[]
    for _ in range(1,n+1):
        u.append(any(t))
    return u

def shuffle(t):
    u = list(t)
    for i in range(len(u) -1, 1, -1):
        j=random.randint(0, i)
        u[i], u[j] = u[j], u[i]
    return u
