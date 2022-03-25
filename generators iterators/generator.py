#generators learning

my_list = [4,6,66,34,1]
#class
def pipi(values):
    lst = []
    for x in values:
        lst.append(x*3.17)
    return lst

print(pipi(my_list))
print('----------')
#vs
def pipi_cool(values):
    for x in values:
        yield x*3.17

mypi = pipi_cool(my_list)

for n in mypi:
    print(n)
print('----------')

#this is also generator

mypi1 = (x*3.17 for x in my_list)

# for n in mypi1:
#     print(n)

print(mypi1)
print(list(mypi1)) #easily converted to list, if we uncomment above for loop this list would be empty

print('----------')
#https://www.youtube.com/watch?v=bD05uGo_sVI