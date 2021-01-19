def Solv( N,A ):
    list1 = list(N)
    count = len(list1)
    for i in list(range(count)):
        M = list1[i] / 2
        if A == M:
            pass
            print("Yes")
        else:
            print("No")

    T = int(input())
    for _ in range(T):
        N = input()
        A = map(int, input().split())
        out_ = Solv(N, A)
        print(out_)
