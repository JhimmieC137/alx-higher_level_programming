#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(list(a_dictionary.keys())) > 0:
        scores = list(a_dictionary.values())
        scores.sort()
        for x in a_dictionary.keys():
            if a_dictionary[x] == scores[-1]:
                return x
    else:
        return None
