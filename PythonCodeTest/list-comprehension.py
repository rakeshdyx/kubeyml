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
"""
### Nested loop for list comprehension

