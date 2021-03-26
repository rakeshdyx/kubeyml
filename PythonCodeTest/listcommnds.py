n = int(input())
l = []
for _ in range(n):
    cmd, *args = input().split()
    if cmd != "print":
        cmd += "("+ ",".join(args) +")"
        eval("l ."+cmd)
    else:
        print(l)


