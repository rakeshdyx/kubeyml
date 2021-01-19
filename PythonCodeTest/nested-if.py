## if the number is even, square it.
## If the number is multiple of 5, cube it
##If the number is non-multiple of 5, multiply with 10

x = int(input("Enter a number"))

if x%2 == 0:
    print("squaring even number")
    print(x**2)
else:
    if x%5 == 0:
        print(" Qubenumber multiplied by 5")
        print(x**3)
    else:
        print("Non-multiple of 5, Multiply with 10")
        print(x * 10)
        if x < 100:
            print("{} Number is less then 100" .format(x))
        else:
            print("{} Number greater then 100" .format(x))

