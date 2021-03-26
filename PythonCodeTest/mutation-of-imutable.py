def mutate_string(string_value, position, value_char):
    l = list(string_value)
    l[position] = value_char
    string_value = '' .join(l)
    return string_value

S = input()
i, c = input().split()
x = mutate_string(S, int(i), c)
print(x)
