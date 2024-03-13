#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
rem = number
sign = 1
if rem < 0:
    rem = rem * -1
    sign = -1
rem = rem  % 10
if rem > 5:
    print(f'Last digit of {number} is {sign * rem} and is greater than 5')
elif rem == 0:
    print(f'Last digit of {number} is {sign * rem} and is 0')
else:
    print(f'Last digit of {number} is {sign * rem} and is less than 6 and not 0')
