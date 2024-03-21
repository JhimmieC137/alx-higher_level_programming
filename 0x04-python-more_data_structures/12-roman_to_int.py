#!/usr/bin/python3
def roman_to_int(roman_string):
    num_dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    s_len = len(roman_string)
    result = 0
    x = 0
    if roman_string and type(roman_string) == str:
        while x < len(roman_string):
            if roman_string[x] == "C":
                if (x + 1) <= (s_len - 1) and roman_string[x + 1] == "D":
                    result += 400
                    x += 1
                else:
                    result += num_dict[roman_string[x]]
            elif roman_string[x] == "X":
                if (x + 1) <= (s_len - 1) and roman_string[x + 1] == "L":
                    result += 40
                    x += 1
                else:
                    result += num_dict[roman_string[x]]
            elif roman_string[x] == "I":
                if (x + 1) <= (s_len - 1) and roman_string[x + 1] == "X":
                    result += 9
                    x += 1
                elif (x + 1) <= (s_len - 1) and roman_string[x + 1] == "V":
                    result += 4
                    x += 1
                else:
                    result += num_dict[roman_string[x]]
            else:
                result += num_dict[roman_string[x]]
            x += 1
        return result
    else:
        return 0
