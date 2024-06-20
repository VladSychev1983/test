import math
from decorator_ import logger

@logger
def foo(num_rows):
    return [[math.comb(i, j) for j in range(i + 1)] for i in range(num_rows)]
print(foo(10))