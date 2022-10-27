# use mysillyobject instead of self as a reference to the current instance of the class and abc also
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name + " and I am " + str(abc.age) + " years old.")

p1 = Person("John", 36)
p1.myfunc()


