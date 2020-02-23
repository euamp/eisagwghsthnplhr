import itertools
def combinations(list_of_six,list_of_four):
    list_of_combos = []
    combos = itertools.combinations(list_of_six, 4)
    for combo in combos:
        if combo in list_of_four:
            list_of_combos.append(combo)
    return list_of_combos


'''
#Example
print(combinations([1,2,3,4,5,6],[(1,2,3,4),(10,11,23,34)]))
'''


