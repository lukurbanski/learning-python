#Python tips

#easier IF
import enum


condition = True

if condition:
    print("OK")
else:
    print("Not OK")

print("OK") if condition else print("Not OK")

#easier to read
num1 = 10_000_000
num2 = 1_000

print(f"{num1*num2:,}")


names = ['Mark', 'George', 'Lucas']
role = ["Developer", "PMO", "BA"]

#enumerate
for index, name in enumerate(names):
    print(index, name)

#zip
for name, rl in zip(names, role):
    print(f'{name} is a {rl}')


#tuples

x, _ = (4,7)
print(x)

a,b, *c = (1,2,3,4,5) #c will have list of 3
print(c)
a,b, *_ = (1,2,3,4,5) #last three are ignored

#class setting attribute tip
class Person():
    pass

person = Person()

person.email = "myemail@email.com"
print(person.email)

personinfo = {'firstname': "Tomas", 'surname': 'Dendelion'}

for key,value in personinfo.items():
    setattr(person,key,value)
#to get attribute use getattr()
print(person.firstname, person.surname)

#security
#best to keep secret values in environment variables
from getpass import getpass
username = input('Username: ')
password = getpass('Password: ')

print(username, 'is logged in.')

#if we use -m we can run scripts which are not in current directory, and we do not have to add ending .py, it runs a module

#run help(nameofthemodule) - to get more info about module and parameters used
#run dir(nameofthemodule) to see all attribute and methods available
