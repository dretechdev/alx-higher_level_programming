#!/usr/bin/python3
if __name__ == "__main__":
    from add_0.py import add

    i, j = 1, 2
    print("{:d} + {:d} = {:d}".format(i, j, add(i, j)))
