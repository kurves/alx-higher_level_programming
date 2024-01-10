#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        score = 0
        weight = 0
        for s, w in my_list:
            score += s * w
            weight += w
            if total_weight != 0:
                weighted_average = total_score / total_weight
                return weighted_average
            else:
                return 0
