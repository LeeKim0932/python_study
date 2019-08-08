
# number1 mathod override
"""
class Person():
    def __init__(self, name):
        self.name = name


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor" + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + " , Esquire"

person = Person('fudd')
doctor = MDPerson('fudd')
layer = JDPerson('fudd')

print(person.name)
print(doctor.name)
print(layer.name)
"""

# number2 super()
"""
class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@apple.co.kr')
print(bob.name)
print(bob.email)
"""

# number3 getter / setter
'''
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('indide the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

fowl = Duck('howard')
print(fowl.name)
print(Duck.name)
'''

# number4 Decorator / property 
"""
class Duck():
    def __init__ (self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

fowl = Duck('howard')
print(fowl.name)
fowl.name = 'donald'
print(fowl.name )
"""

# number5 Decorator  / property
"""
class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

cir = Circle(5)
print(cir.diameter)
print(cir.radius)
"""

# number6 private 
"""
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property #getter
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter #getter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

fowl = Duck('howard')
print(fowl.name)
"""

# number7 magic method 
"""
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return "Word('" + self.text + "')"

first = Word('ha')
first
print(first)
"""

# number8 composition
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a', self.bill.description, 'bill and a', self.tail.length, 'tail')

tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()

