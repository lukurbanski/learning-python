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

print("-----------")

#quick lambda for fun
wysokienumerki = filter(lambda x: x > 3, numerki)
# print(list(wysokienumerki))

class myRange:
    def __init__(self, start, end) -> None:
        self.value = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

m = myRange(1,10)

print(next(m))
print(next(m))
print(next(m))

print("-----------")

#generators automatically have __iter__ and __next__, we don't have to create it manually
#example of generators

def my_range(start,end):
    current = start
    while current < end:
        yield current
        current += 1

myr = my_range(0,5)
for n in myr:
    print(n)

#definietely generator takes memory than looping over the list, it takes one at a time
#fact that something is iterable does not mean it is iterable (it has to have "next" dunder method)
#iterator remember where it's at. 