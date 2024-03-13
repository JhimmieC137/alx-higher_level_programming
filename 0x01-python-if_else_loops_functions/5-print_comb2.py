#!/usr/bin/python3
for x in range(0, 100):
    if x == 99:
        print("{}".format("%02d" % x), end='\n')
    else:
        print("{}".format("%02d" % x), end=', ')
