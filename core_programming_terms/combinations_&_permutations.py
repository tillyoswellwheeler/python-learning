# ------------------------------------------------
# Programming Terms -- Combinations & Permutations
# ------------------------------------------------

import itertools as it

my_list = [1, 2, 3, 4, 5, 6]

combinations = it.combinations(my_list, 3)
permutations = it.permutations(my_list, 3)

#--- Combination is important below
print([result for result in combinations if sum(result) == 10])

#--- Permutations is important below
word = 'sample'
my_letters = 'plmeas'

combinations = it.combinations(my_letters, 6)
permutations = it.permutations(my_letters, 6)

for p in permutations:
    print(p)
    if ''.join(p) == word:
        print("Match!")
        break
    else:
        print("No Match!")