#list is iterable, but it's not an interator
numerki = [1,2,4,5]
tuplki = (1,4,5,6)
dziwne = [tuplki, 4]

#classic for loop
for i in dziwne:
    if isinstance(i,tuple):
        print(i)
    else:
        pass

print('__iter__' in dir(dziwne))

#iter_num = numerki.__iter__() #not too clean
iter_num = iter(numerki) #cleaner
print(type(iter_num))
#print(dir(iter_num))
print(next(iter_num)) 
print(next(iter_num))
print(next(iter_num)) #it remembers where it is so new values every time
#it cannot go backwards or repeat

#quick lambda for fun
wysokienumerki = filter(lambda x: x > 3, numerki)
# print(list(wysokienumerki))

