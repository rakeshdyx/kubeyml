"""
#Retraive using get
x = {"UK":500045, "India":500023, "USA":500024}
print(x.get('UK'))
print(x.get('Japan'))


#Using in Operator
d = {"Apple":20, "Orange":15, "Peach":10}
k = "Peach"
print(k in d)
print("Orange" in d)
print(d.keys())
print(d.values())
print(type(d.values()))


#converting list of tuple to dictionary

x = [('Apple', 30), ('Orange', 55), ('Banana', 30)]
d= dict(x)
print(d)

#concatinate 2 strings
d1 = {"US": 1234, "UK": 1235, "UAE": 12346}
d2={"Tony": 23, "John": 52, "Scott": 60}

d1.update(d2)
print(d1)
print(d2)



words=["Apple", "Orange","Apple", "Banana", "Peach", "Banana", "Apple","Peach" ]

d={}

for w in words:
    if w not in d:
        d[w] = 1
    else:
        d[w] += 1
print("Words and Counts: ", d)

words=["Apple", "Orange","Apple", "Banana", "Peach", "Banana", "Apple","Peach" ]

for w in words:
    print((w, ' -> ', words.count(w)))
"""

words=["Apple", "Orange","Apple", "Banana", "Peach", "Banana", "Apple","Peach" ]

for w in set(words):
    print((w, ' -> ', words.count(w)))