import tkinter as tk
class Restaurant:
    def __init__(self, restaurantName, cuisineType, rating):
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
        if int(int(rating >5) or int(rating < 0)):
            print("Рейтинг от 0 до 5, ИНАЧЕ НЕ ДОВЕРЯЙТЕ ЭТОМУ РЕЙТИНГУ")
        self.rating = int(rating)

    def describe_restaurant(self):
        print("Название:", self.restaurantName, "Кухня:", self.cuisineType)

    def is_open_restaurant(self):
        print("Ресторан:",self.restaurantName, "- открыт")

    def rating_of_restaurant(self):
        print("Рейтинг ресторана", self.restaurantName, "-", self.rating)

    def new_rating(self, rater):
        self.rating = rater

class IceCreamStand(Restaurant):
        standartflavors = ["chocolate", "strawberry"]
        def __init__(self, location, timeOfWork, restaurantName, rating):
            self.flavors = self.standartflavors
            self.location = location
            self.timeOfWork = timeOfWork
            self.restaurantName = restaurantName
            self.rating = rating
        def addFlavor(self, flavor):
            self.flavors.append(flavor)
        def showFlavors(self):
            print("Вкусы : ")
            for flavor in self.flavors:
                print(flavor)
        def removeFlavor(self, flavor):
            self.flavors.remove(flavor)
        def whenWhereWork(self):
            print("Работает в", self.location, " Работает ", self.timeOfWork, "часов")
        def pickyEating(self, flavor):
            if flavor in self.flavors:
                print(flavor, "Вкус в наличии")
            else:
                print(flavor, "Такого вкуса нет")

CoolCream = IceCreamStand("Park", 10, "CoolCream", 4)
CoolCream.addFlavor("OREO51")
CoolCream.showFlavors()
CoolCream.removeFlavor("OREO51")
CoolCream.showFlavors()
CoolCream.whenWhereWork()
CoolCream.pickyEating("chocolate11")

def clicked():
    windowFlavors = "Вкусы : "
    for flavor in CoolCream.flavors:
        windowFlavors = windowFlavors + flavor + ", "
    windowFlavors = windowFlavors[0:len(windowFlavors)-2]
    label1 = tk.Label(window, text= windowFlavors, font=("Arial Bold", 25))
    label1.grid(row=10, column=1)

window = tk.Tk()
tinker = CoolCream.restaurantName
window.title(tinker)
window.geometry("500x500")
button1 = tk.Button(window, text = "Вывод списка вкусов", font=("Arial", 20),command=clicked)
button1.grid(row = 1, column = 1)
window.mainloop()
