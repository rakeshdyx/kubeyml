A = "010101"
P = "101101"

list1 = list(A)
list2 = list(P)
count = 0
for i in list(range(6)):
    print(i)
    if list1[i] == list2[i]:
        count = count + 1
print(count)
