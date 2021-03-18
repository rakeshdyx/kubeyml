"""
i = int(input())

if i >= 2 and i <= 10:
    l_score = list([int(input()) for _ in range(i)])

    z = max(l_score)
    while max(l_score) == z:
        l_score.remove(max(l_score))

    print(max(l_score))

n = int(input())
l_score = []
if n >= 2 and n <= 10:
    for i in range(n):
        l_score.append(input())
    z = max(l_score)
    while max(l_score) == z:
        l_score.remove(max(l_score))
    print(max(l_score))

"""

n = int(input())
arr = map(int, input().split())
l_score = list(arr)
z = max(l_score)
while max(l_score) == z:
    l_score.remove(max(l_score))
print(max(l_score))

