mylist = [ ]
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
    print(mylist)
print("outloop:",mylist)

#comp

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)