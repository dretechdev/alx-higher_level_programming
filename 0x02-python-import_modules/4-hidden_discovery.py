#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    # Print sorted name from directory

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
