# sales_tax=.095
# item_list={"water": 1.00, "milk": 1.50, "apple": .75}
# def calc_tax(price):
#     return price*sales_tax
#
# def calculate_final_price(item_value):
#     return calc_tax(item_value)+item_value
#
# def calculate_final_price_by_name(item_name):
#     return calculate_final_price(item_list[item_name])
#
# print ("Please insert item name")
# user_input=raw_input()#will return what the user has typed
#
# if (user_input in item_list)==False:
#     print "Not in dictionary"
# else:
#     print calculate_final_price_by_name(user_input)

class Ninja(object):

    def __init__(self, name, level):
        self.name = name
        self.level = level


    def fight(self, other):
        if self.level>other.level:
            print "I win"
        elif self.level==other.level:
            print "draw"
        else:
            print "I lose"

ninja1 = Ninja("Tyson", 1)

#ninja1.fight(ninja1)
#
# class Sensei(Ninja):

class Monster(object): #3 properties and two methods; ne method include a way to interact, then have a monster an a ninja interact.
#have some properties in ninja and monsters?

    def __init__(self, name, color, size):
        self.color = color
        self.size = size
        self.name = name

    def scare(self):
        print "I'M BEING SCARY"

    def roarAt(self, other):
        print "I'M ROARING AT "+ other.name.upper()

    def describeSelf(self):
        print "My name is " + self.name + ". I am " + self.color.lower() + " and I am " + self.size.lower() + ". "


Mike=Monster("Mike", "Green", "Small")
Sully=Monster("Sully", "Blue and Purple", "Huge")
Sully.roarAt(Mike)
Sully.roarAt(ninja1)
Mike.describeSelf()
Sully.scare

def collatz(n):
    while n>1: yield n; n=(n/2 if n%2==0 else 3*n+1)
print max(sum(1 for _ in collatz(n)) for n in xrange(1, 1000001))
