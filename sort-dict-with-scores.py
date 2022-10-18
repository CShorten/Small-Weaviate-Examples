# lol, doing this so often needed to write it down somewhere.

ex = {
    1: 6,
    2: 10,
    3: 4,
    4: 18
}

sorted(ex.items(), key = lambda item: item[1], reverse=True)
