#!/usr/bin/python3
def print_last_digit(number):
    sign = 1
    if number < 0:
        sign = sign * -sign
    print("{}".format((number * sign) % 10), end='')
    return((number * sign) % 10)
