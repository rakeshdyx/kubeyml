### transpose of matrix

"""
transposed = []
matrix = [[2, 6, 7, 9, 4], [6, 5, 9, 3, 7]]

for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)


matrix = [[2, 6, 7, 9, 4], [6, 5, 9, 3, 7]]
print([[row[x] for row in matrix] for x in range(len(matrix[0]))])

"""

import string
alphabet = string.ascii_lowercase

L = []
for i in range(3):
    s = "-".join(alphabet[i:3])
    L.append((s[::-1]+s[1:]).center(4*3-3, "-"))
print('\n'.join((L[:0:-1])+L))





