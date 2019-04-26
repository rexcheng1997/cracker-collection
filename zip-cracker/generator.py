"""
    python 3 - Generator Module
"""

__author__ = "rexcheng1997"


from functools import reduce

def generator(_plen, _characters):
    '''
        Generate all permutations of passwords of length = _plen, using the characters in _characters.

        Attributes:

            - _plen: length of the passwords
            - _characters: list of characters included in the passwords
    '''
    arr = []
    perm = []
    for i in range(_plen):
        perm.append(0)
    walk = range(1, len(perm))
    walk.reverse()
    while perm[0] < len(_characters):
        pwd = reduce(lambda x, y: x + y,
            map(lambda x: _characters[x], perm)
        )
        arr.append(pwd)
        perm[-1] += 1
        for i in walk:
            if perm[i] == len(_characters):
                perm[i - 1] += 1
                perm[i] = 0
    return arr
