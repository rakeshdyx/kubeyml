"""
record = []
for _ in range(int(input())):
    inner_list = []
    name = input()
    score = float(input())
    inner_list.append(name)
    inner_list.append(score)
    record.append(inner_list)


z = min(record)
while min(record) == z:
    record.remove(min(record))
x = min(record)
while min(record) == x:
    print(min(record))

record = []
for _ in range(int(input())):
    record.append([input(), float(input())])

second_higest = sorted(list(set([marks for name, marks in record])))
print(second_higest)


"""
n = int(input())
record = [[input(), float(input())] for _ in range(n)]
shorted_value = sorted(set([z for y, z in record]))[1]
print('\n' .join([a for a, b in sorted(record) if b == shorted_value]))