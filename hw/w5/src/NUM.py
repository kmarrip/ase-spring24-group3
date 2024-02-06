import math

class NUM:
    def __init__(self, s=None, n=None):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.hi = -1E30
        self.lo = 1E30
        self.heaven = 0 if (s or "").find("-$") else 1

    def add(self, x):
        if x != "?":
            self.n += 1
            d = x - self.mu
            self.mu += d / self.n
            self.m2 += d * (x - self.mu)
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)

    def mid(self):
        return self.mu

    def div(self):
        return 0 if self.n < 2 else math.sqrt(self.m2 / (self.n - 1))

    def small(self):
        return the.cohen * self.div()

    def norm(self, x):
        return x if x == "?" else (x - self.lo) / (self.hi - self.lo + 1E-30)

    def dist(self, x, y):
        if x == "?" and y == "?":
            return 1

        x, y = self.norm(x), self.norm(y)

        if x == "?":
            x = 1 if y < 0.5 else 0

        if y == "?":
            y = 1 if x < 0.5 else 0

        return abs(x - y)

    def bin(self, x):
        tmp = (self.hi - self.lo) / (the.bins - 1)
        return 1 if self.hi == self.lo else math.floor(x / tmp + 0.5) * tmp
