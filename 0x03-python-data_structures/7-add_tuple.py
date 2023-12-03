#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    We can use the function ziplongest from itertools module
    for  this task as follow:
    from itertools import ziplongest
    result = [sum(pair) \
              for pair in \
              ziplongest(tuple_a,
                         tuple_b,
                         fillvalue=0)]
    return (tuple(result))
    """
    result = []
    # Find the maximum tuple size for iteration
    size = max(len(tuple_a), len(tuple_b))
    # We used on the first 2 element though.
    # We can change 2 to size later if need be.
    for i in range(2):
        try:
            a = tuple_a[i]
        except IndexError as e:
            a = 0
        try:
            b = tuple_b[i]
        except IndexError as e:
            b = 0
        result.append(a + b)
    return (tuple(result))
