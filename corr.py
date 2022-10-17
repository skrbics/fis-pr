import numpy as np
import scipy as sp


def cov(xs, ys):
    mx = np.mean(xs)
    my = np.mean(ys)
    c = np.dot(xs-mx, ys-my) / len(xs)
    return c


data1 = np.array([3, 7, 12, 10])
data2 = np.array([5, 4, 12, 3])

print("Mean 1: ", data1.mean())
print("Mean 2: ", data2.mean())
print("Var 1: ", data1.var())
print("Var 2: ", data2.var())

print("Covariance: ", cov(data1, data2))

std1 = data1.std();
std2 = data2.std();
print("Std 1: ", data1.std())
print("Std 2: ", data2.std())

pcc, _ = sp.stats.pearsonr(data1, data2)
print("Pearson: ", pcc)
scc, _ = sp.stats.spearmanr(data1, data2)
print("Spearman: ", scc)

x = np.array([1, 2, 4, 3])
y = np.array([3, 2, 4, 1])
pcc, _ = sp.stats.pearsonr(x, y)
print("Spearman using Pearson: ", pcc)