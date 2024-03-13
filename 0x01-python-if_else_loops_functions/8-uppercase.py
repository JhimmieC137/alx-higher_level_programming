#!/usr/bin/python3
def uppercase(str):
    word = ''
    for x in str:
        if ord(x) in range(97, 123):
            word = word + chr(ord(x) - 32)
        else:
            word = word + x
    print("{}".format(word))
