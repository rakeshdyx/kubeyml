f=open("emp.txt", "r")

"""
f.seek(15)
print(f.tell())
print(f.read(10))


print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())


L = f.readlines()
print(L)
print(type(L))

"""

# Calculate sum of all salaries from emp.txt file

s=f.read()
f.seek(0)
f.readline()
for l in f.readlines():
    s=l.strip('\n')
    print(s)
