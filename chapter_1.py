a = 10


# Variable Scope


def my_func():
    global a
    print(a)
    a = a + 1


my_func()

# Type, value and identity
# (String type) sayHello (w/ sayHello identity) = "Hello World" (with this value)

# Slicing strings
greet = "Hello World"

# Slicing until 8th index
print(greet[0:8])
# Slicing until end w/ stepping of 2
print(greet[0::2])

# Lists
# Can contain nested structures
items = [["rice", 1.2, 8], ["flour", 1.9, 5], ["Korn", 4.7, 5]]

print(items[1][1])

# Creating a list through a list
# Called list comprehensions
numbers = [2, 4, 6, 8, 16]

new_l = [i ** 3 for i in numbers]
print(new_l)

# Functions as first class objects
# Both functions and classes are same like built-in data types
# Assigned as a variable or in a data structure
# Passed as an argument to a function
# Returned as the result of a function

# Higher Order Functions

# Functions that take other functions as arguments or that return functions are called higher order functions

for nums in map(lambda n: n * 2, numbers): print(nums)

words = str.split('The longest word in this sentence')

# Sorting words by length
print(sorted(words, key=len))

# Case-insentive sorting

sl = ['A', 'b', 'a', 'C', 'c']

sl.sort(key=str.lower)
print(sl)

sl.sort()
print(sl)

items.sort(key=lambda item: item[1])
print(items)


# Recursive Functions
# Recursion repeatedly calls a function
# for breaking out the infinite loop there's a need of test to terminete recursion

# Generators and co-routines
# No clue at first reading

# Classes and object programming
# Class defines set of attributes that are shared across instances of that class

class Employee(object):
    numEmployee = 0

    def __init__(self, name, rate):
        self.owed = 0
        self.name = name
        self.rate = rate
        Employee.numEmployee += 1

    def delete_emp(self):
        Employee.numEmployee -= 1

    def hours(self, numHours):
        self.owed += numHours * self.rate
        return ("%.2f hours worked" % numHours)

    def pay(self):
        self.owed = 0
        return ("payed %s" % self.name)


emp1=Employee("Jill",18.5)
print(emp1.hours(20))
print(emp1.owed)

# Special methods
# Things with __x__ generally called by Python interpreter

# Inheritance
# Inherit the functionality from other classes

# Data encapsulation and properties
# In python we use __methodName() to have private attributes


