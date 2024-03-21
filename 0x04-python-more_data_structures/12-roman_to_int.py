#!/usr/bin/python3
def roman_to_int(roman_string):
    num_dict = {"M": 1000, "D": 500, "C": 100,"L": 50, "X": 10, "V": 5, "I": 1}
    result = 0
    if roman_string and type(roman_string) == str:
        for x in range(0, len(roman_string)):
            print(x)
            print(roman_string[x])
            if roman_string[x] == "C":
                if (x + 1) <= (len(roman_string) - 1) and roman_string[x + 1] == "D":
                    result += 400
                    x += 1
                else:
                    result += num_dict[roman_string[x]]
            elif roman_string[x] == "X":
                if (x + 1) <= (len(roman_string) - 1) and roman_string[x + 1] == "L":
                    result += 40
                    x += 1
                else:
                    result += num_dict[roman_string[x]]
            elif roman_string[x] == "I":
                if (x + 1) <= (len(roman_string) - 1) and roman_string[x + 1] == "X":
                    result += 9
                    x += 1                 
                elif (x + 1) <= (len(roman_string) - 1) and roman_string[x + 1] == "V":
                    result += 4
                    x += 1 
                else:
                    result += num_dict[roman_string[x]]
            else:               
                result += num_dict[roman_string[x]]
            
        return result
    else:
        return 0
