# Goldobina Svetlana
#
# display all permutations

from itertools import permutations
import re

print(*(map(lambda *x: re.sub(r'[(]|[)]|,|\s', '', str(x)), (permutations(range(1, int(input().strip()) + 1))))), end='', sep='\n')

