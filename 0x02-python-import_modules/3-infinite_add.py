#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = 0
    for x in range(1, len(sys.argv)):
        num = num + int(sys.argv[x])
    print(num)
