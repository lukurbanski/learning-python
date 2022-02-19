

class Osoba():
    iloscpalcow = 5
    def __init__(self, name, surname):
        
        self.name = name
        self.surname = surname
        self.palce = Osoba.iloscpalcow * 2
    
    @classmethod
    def ilosc_palcow(cls):
        return cls.iloscpalcow

    @staticmethod #useful mostly for organization
    def dosomething():
        return 5

class Chalupa():
    def __init__(self, miejsca):
        self.miejsca = miejsca
        self.osoby = []

    def add_person(self, osoba):
        if len(self.osoby) < self.miejsca:
             self.osoby.append(osoba)
             return True
        return False
    

o1 = Osoba("Tomek", "Kalisz")
o2 = Osoba("Wojtek", "Mrona")
o3 = Osoba("Zbyszek", "Syfon")
o4 = Osoba("Marcin", "Troszczynski")    

print()

chata = Chalupa(3)

chata.add_person(o1)
chata.add_person(o2)
chata.add_person(o3)

# for o in chata.osoby:
#     print(o.name, o.surname)

Osoba.iloscpalcow = 7
o5 = Osoba("Luk", "Tola")
print(o5.palce)

print(Osoba.ilosc_palcow())

print(Osoba.dosomething())