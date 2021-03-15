"""
a = [x for x in range(10)]
print(a)

##from a string
h_letter = [letter for letter in 'human']
print(h_letter)

##if condition
d = [x for x in range(10) if x%2==1]
print(d)


##with if-else
obj = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print(obj)

### Nested if for list comprehension
print([y for y in range(100) if y % 2 == 0 if y % 5 == 0])

### Nested loop for list comprehension with Transpose of Matrix using Nested Loops

##Transpose of Matrix using Nested Loops

transposed = []
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

##Using nested list comprehension
matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed_matrix)

"""
##using multiple parallal for loops

x, y, z, n = [int(input()) for _ in range(4)]
#print(x, y, z, n)
#print all possible coordinates in i,k,j format with constriant 0<=i<= x, 0<=j<= y, 0<=k<= z and remove the cordinate if i+j+k=n
cordinates_list = [[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a + b +c != n]
print(cordinates_list)


