#whileloop
"""i = 0
while i <= 10:
    i+=1
    print(i)
print("Main Ends here")
print(i)"""

##whileloop, with break and continue

i = 1
while i:
    print("{}th time of i".format(i))
    i+=1
    c = 10
    print(c)
    if i == 6:
        break
    else:
        print("Before else\n  continue")
        continue
        print("after else\n  continue")
print("Main Ends here")
print(i)


