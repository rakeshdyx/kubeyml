def substring_match(string, sub_string):
    counter, sum = 0, 0
    for _ in range(0, len(string)):
        if matcher(string[counter:len(sub_string) + counter], sub_string):
            sum += 1
        counter += 1
    return sum


def matcher(str_slice, sub_string):
    return str_slice == sub_string


str_name = input()
sub_str = input()
count = substring_match(str_name, sub_str)
print(count)
