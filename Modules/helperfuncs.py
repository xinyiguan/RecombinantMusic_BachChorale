import numpy as np

def F(f,X):
    return [f(x)for x in X]
def compose(f,g):
    return lambda x:f(g(x))
