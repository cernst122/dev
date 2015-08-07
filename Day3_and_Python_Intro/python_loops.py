# words=["Mary", "had", "a", "little", "lamb"]
#
# i=0
# for word in words:
#     word=word[::-1]
#     words[i]=word
#     i=i+1
# words.reverse(); #reverse order of words
# print words
# def first_letters(words): #this doesn't need to have the same name as the words array. coincidence
#     letters=[]
#     for name in words: #this names each element in words "name"
#         letters.append(name[0]) #add the first element of the first element to the empty list "letters"
#     return letters
#
#
# words=["Zach", "Arely", "Manuel","Yulissa"]
# print first_letters(words)
# print first_letters(["a", "little", "lamb"])

# def print_dwarves(names):
#     i=1
#     for name in names:
#         print str(i)+". "+name
#         i=i+1
#
# dwarves=["Doc", "Grumpy", "Sleepy", "Happy"]
# print_dwarves(dwarves)
#
# def summon_captain_planet(calls):
#     for element in calls:
#         print element.capitalize()+"!"
#
#
# calls=["earth", "wind", "fire", "water", "heart"]
# summon_captain_planet(calls)
#
# def long_planeteer_calls(calls):
#     for element in calls:
#         if len(element) > 4 :
#             print "true"
#             return True
#         else:
#             return False
#
# words=["cow", "cow", "cow"]
# longer_words=["ubiquitous, slug, umbrella"]
# long_planeteer_calls(words)
# long_planeteer_calls(longer_words)
#
# Happy Parrot - This parrot is so happy. It accepts a 'thing' as its argument and then returns a string where it says how happy it is about the thing!
def happy_parrot(thing):
  print "I am so happy about " + thing +"!"

string="crackers"
happy_parrot(string)

# Boring Parrot - Write a method for a boring parrot that just returns whatever string you give him as an argument.

def boring_parrot(topic):
    print topic

conversation="boring"
boring_parrot(conversation)

# Math Parrot - Create a method that accepts two numbers as arguments and adds them together!

def math_parrot(num1, num2):
    print num1+num2

num1=3
num2=5
math_parrot(num1, num2)

# Friendly Parrot - This parrot greets people by returning their name and age

def friendly_parrot(name, age):
    print "Your name is " + name + " and your age is " + str(age)

name="Christina"
age=18
friendly_parrot(name, age)

# Favorites Parrot - Tell this parrot about your three favorite things and he will return "I love <that thing> too!"
def favorites_parrot(thing1, thing2, thing3):
    string="I love " + thing1+ ", "+thing2+", and "+thing3+" , too!"
    string=string.upper()
    print string[::-1]
    print string[::-1][::-1]

thing1="Harry Potter"
thing2="tacos"
thing3="chipotle"
favorites_parrot(thing1, thing2, thing3)









percy_invitation = "The family of Percy Weasley proudly invite you to their graduation commencement on Saturday the 22nd of May 1993. Festivities will be held at The Burrow. See you then!"
ron_invitation=percy_invitation.replace("Percy", "Ron").replace("Saturday", "Sunday").replace("22nd", "18th").replace("1993", "1997")
print ron_invitation


ginny_template = "The family of {name} Weasley proudly invite you to their graduation commencement on {calendar_day} the {date} of May {year}. Festivities will be held at The Burrow. See you then!"
print ginny_template.format(name="Ginny", calendar_day="Sunday", date="17th", year="1998")
