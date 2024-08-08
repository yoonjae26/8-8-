from kivy.app import App  # type: ignore
from kivy.uix.label import Label

class HelloWorldApp(App):
    def build(self):
        label = Label(text='Hello, World!')
        return label

if __name__ == '__main__':
    HelloWorldApp().run()

# Define a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the class
person = Person("John", 30)

# Call a method on the instance
person.greet()

# Define a function
def greet(name):
    print("Hello, " + name + "!")

# Call the function
greet("John")

# For loop
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

for x in range(5):
    print(x)

# If-else statement
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")

# Switch statement (not directly supported in Python, but can be implemented using dictionaries)
def switch_demo(x):
    switcher = {
        1: "This is case one!",
        2: "This is case two!",
        3: "This is case three!",
    }
    return switcher.get(x, "nothing")

print(switch_demo(1))

# Declare a variable
name = "John"

# Print the variable
print(name)

# Declare a list (similar to an NSArray in iOS)
fruits = ["Apple", "Banana", "Cherry"]

# Print the list
print(fruits)

# Declare a dictionary (similar to an NSDictionary in iOS)
person = {"name": "John", "age": 30}

# Print the dictionary
print(person)
