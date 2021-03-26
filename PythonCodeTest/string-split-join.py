def split_and_join(line):
    sj = ("-".join(line.split(" ")))
    return sj
result = split_and_join(input())
print(result)
