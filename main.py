from function import *
 
R = {(1, 1), (1, 3), (2, 2), (3, 3),(3, 1), (3, 4), (4, 4), (4, 3)}
a = set(sum([[*i] for i in R],[]))

print(check_reflexive(R))

print(check_symmetric(R))

print(check_transitive(R))

print(check_equivalnce(R))
