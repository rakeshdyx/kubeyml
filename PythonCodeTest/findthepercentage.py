n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
name_avg = student_marks[query_name]
print("{0:.2f}".format(sum(name_avg)/(len(name_avg))))