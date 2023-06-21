import numpy as np
import math as mt
import itertools

class Permutation:
    def __init__(self,X):
        self.num = len(X)
        self.l = X
        self.rank = 0
        for i in range(self.num):
            cnt = 0
            for j in range(i+1,self.num):
                if X[i] > X[j]:
                    cnt += 1
            self.rank += mt.factorial(self.num - i - 1) * cnt

class Distribution:
    def __init__(self,n):
        self.n = n
        self.num = mt.factorial(n)
        self.l = [1] + [0] * (self.num - 1)
    def display(self):
        print(self.l)
    def Top_shuffle(self):
        _l = [0] * self.num
        for p in itertools.permutations([_ + 1 for _ in range(self.n)]):
            for i in range(self.n):
                B = list(p)
                P = Permutation(B[1:i+1] + [B[0]] + B[i+1:self.n])
                _l[P.rank] += self.l[Permutation(B).rank] / self.n
        self.l = _l
        self.display()
    def Riffle_shuffle(self):
        pass

X = Distribution(3)
for _ in range(10):
    X.Top_shuffle()