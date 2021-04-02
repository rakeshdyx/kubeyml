s = input()
if len(s) > 0 and len(s) < 1000:
    for i in ['isalnum', 'isalpha', 'isdigit', 'isupper', 'islower']:
        print(any(eval("c." + i + "()") for c in s))

