YOU = ['aaa', 'bbb', 'iii', 'uuu', 'ggg', 'ddd', 'eee']
ME = ['bbb', 'ccc', 'ddd', 'fff', 'ggg', 'aaa', 'eee', 'zzz']
print("Your friends are:", YOU)
print("My friends are:", ME)

common = []

for x in YOU:
    for y in ME:
        if(x == y):
            common.append(x)
            break
    print(common)
print("\n")
print("Common Friends are:", common)
input("\n Press Enter Key")

print("\n"*3)
print("-"*40)
RforM=[]
for i in YOU:
        if i not in common:
            RforM.append(i)
print("Friends Recomended for Me", RforM)

RforY=[]
for j in ME:
    if j not in common:
        RforY.append(j)
print("Friends Recomended for You", RforY)

