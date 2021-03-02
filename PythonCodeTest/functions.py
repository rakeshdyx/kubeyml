"""
### calculate average and grade of university exam
##function for average

def averagevalue(marks):
    sub_count = len(marks)
    sum_of_marks = sum(marks)
    average_marks = sum_of_marks / sub_count
    return average_marks


##function for grade

def achived_grade(avgmark):
    if avgmark >= 80:
        print("Grade A", avgmark)
    elif avgmark >= 60 and avgmark < 80:
        print("GradeB", avgmark)
    elif avgmark >= 50 and avgmark < 60:
        print("Grade C", avgmark)
    else:
        print("Grade F", avgmark)


marks = [98,64,94,90,65]
avg_mark = averagevalue(marks)

achived_grade(avg_mark)


##function for add numbers
def number_sum(x, y):
    sum_nu = x + y
    return sum_nu

##function for multiply numbers

def number_multiply(x, y):
    mul_nu = x * y
    return mul_nu

a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))

print(number_sum(a, b))
print(number_multiply(a, b))



###Function Arguments
## Arbitary arguments

def greet(*names):
    for name in names:
        print("Hello ", name)

#name=["Jhon", "Scott", "Ruben", "Pieter", "Linda"]
greet("Jhon", "Scott", "Ruben", "Pieter", "Linda")

##default Arguments



#recursive function

def factorial(x):
    print(x)
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num=int(input("Enter a number"))
print("The factorial of ", num, "is", factorial(num))



##Lambda Function
#squaring a number

sq = lambda x,y: x**2 + y**2

print(sq(2,3))

#max of two numbers

maxim = lambda x, y: x if x > y else y

print(maxim(45,20))

##Quadratic Functions:
##f(x) = ax^2 + bx + c

def qf(a, b, c):
    return lambda x: a*x**2 + b*x + c

#y = qf(4,3,8)
#print(y(3))
print(qf(4,3,8)(3))


### MAP Function

##print square of numbers
#using tradinal method

def sq(lst1):
    lst2 = []
    for i in lst1:
        lst2.append(i**2)
    return lst2

lst1 = [3,4,7,2,9]
print(sq(lst1))


#using map function
lst1 = [3,4,7,2,9]

#x = map(lambda x: x**2, lst1)
print(list(map(lambda x: x**2, lst1)))
print(tuple(map(lambda x: x**2, lst1)))
print(set(map(lambda x: x**2, lst1)))
#for i in x:
#    print(i)



list1 = [1, 2, 4, 5, 6, 7, 10, 56, 34, 28, 54, 32, 21]

print(list(filter(lambda x: (x%2 == 0), list1)))



##Global and Local variables

c = 1

def add():
    global c
    c = c + 1
    print(c)

add()

print(c)




### If the syntax *expression appears in the function call, expression must evaluate to an iterable. Elements from these iterables are treated as if they were additional positional arguments. For the call f(x1, x2, *y, x3, x4), if y evaluates to a sequence y1, …, yM, this is equivalent to a call with M+4 positional arguments x1, x2, y1, …, yM, x3, x4.

### Same in the case of function call. To print a iterable we can call function wuth *. example below.

def _iterable():
    a = [1, 3, 4, 5, 6, 7]
    return a
print(_iterable())
print(*_iterable())

"""

def f(a, b):
    print(a, b)

f(b=1, *(2,))