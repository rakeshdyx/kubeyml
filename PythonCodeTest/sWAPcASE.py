def swap_case(s):
    n = (''.join([i.upper() if i.islower() else i.lower() for i in s]))
    return n


result = swap_case(input())
print(result)
