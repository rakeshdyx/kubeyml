"""

a = (x for x in range(10))

e = (x1 for x1 in a if x1%2 == 0)

for i in e:
 print(i)


"""
a = (x for x in range(10))
odd = list(x for x in a if x%2==1)
print(odd)

for i in a:
    print(i)