#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    L = len(argv)
    print("{:d} {:s}{:s}".format(L - 1, "argument" if L <= 2 else "arguments",
                                 "." if L == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
