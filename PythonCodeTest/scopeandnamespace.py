def outer_fun():
    global a
    a = 20

    def inner_fun():
        global a
        a = 30
        print('a =', a)
    inner_fun()
    print("Inner fun value")
    print('a =', a)
a = 10
outer_fun()
print("Print global one")
print('a =', a)