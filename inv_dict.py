#!/usr/bin/python

def inv_dict(dic):
    keys = dic.keys()
    vals = dic.values()

    inv = {}

    for idx in range(len(vals)):
        key = vals[idx]

        if(key not in inv):
            inv[key] = []

        inv[key].append(keys[idx])

    return inv


if __name__ == "__main__":
    dict = {"hello":4, "world": 3, "gee":1, "kill":2, "mee":2}
    print inv_dict(dict)
