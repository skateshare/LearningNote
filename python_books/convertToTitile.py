
"""
A > 65

"""


def converter(n):
    res = ""
    while True:
        if n <= 26:
            res = chr(64+n) + res
            break

        mod_ = n % 26
        n = n // 26
        res = chr(64+mod_) + res

    return res



print(converter(700))
