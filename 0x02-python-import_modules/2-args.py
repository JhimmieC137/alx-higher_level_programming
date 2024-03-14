#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("0 arguments.")
    else:
        if len(sys.argv) == 2:
            print(f"{len(sys.argv) - 1} argument:")
        else:
            print(f"{len(sys.argv) - 1} arguments:")
        for x in range(1, len(sys.argv)):
            print(f"{x}: {sys.argv[x]}")
