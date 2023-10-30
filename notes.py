# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

 ### it says that there is no module 
from curses.ascii import FF
from os import fchdir
from tkinter import N


class Dog:
    # functions that start w/ 2 underscores (__) are not intended to be called directly
    def __init__(self, n = "", fc = "", a = 0, ff = ""):
    ##Creates an instance of the dog class and sets atributes

       self.name = n 
       self.fur_color = fc 
       self.age = a 
       self.favorite_food = ff 
       self.fetch_count = 0 

    def __str__(self) -> str:
        # Returns a String representation of a dog
        s = "The dog's name is " + self.name + "\n"
        s += "and age is " + str(self.age) + "\n"
        s += "and fur color is " + self.fur_color + "\n"
        s += "and they have played fetch " + str(self.fetch_count) + " times\n"
        return s

    def play_fetch(self, num_times):
        self.fetch_count += num_times

    def paint_dog(self, color):
        self.fur_color = color


mydog = Dog("Logan", "black", 7, "salmon")
chrisdog = Dog("Luna", "black and white", 6, "tortillas")
print(mydog)
print(chrisdog)

mydog.play_fetch(20)
mydog.paint_dog("pink")
chrisdog.play_fetch(3)

print(mydog)
print(f"{chrisdog.name} has played fetch {chrisdog.fetch_count} times")
