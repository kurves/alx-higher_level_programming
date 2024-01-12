#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = 0
    weight = 0
    for s, w in my_list:
        score += s * w
        weight += w
        if weight == 0:
            return 0
        weighted_average = score / weight
        return weighted_average
