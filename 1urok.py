'# class Studens:
#     print("Hello")
#     def __init__(self):
#       self.height = 158
#       print("I am Sasha!")
#
# first_student = Studens()
# print(first_student.height)

# class Studens:
#     amount_of_studens = 0
#     def __init__(self, height=160):
#         self.height = height
#         Studens.amount_of_studens += 1
#
# sasha = Studens()
# german = Studens(height = 158)
# print(german.height)
# print(sasha.height)
# print(german.amount_of_studens)

# class Studens:
#     def __init__(self, name = None):
#         self.name = name
#     def __str__(self):
#         return f"I Sasa. I is Sasa {self.name}."
#
#
# kate = Studens(name = "Kate")
# print(kate)
# print(kate.name)

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print(("Time to study"))
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print(("I will sleep"))
        self.gladness +=3
    def to_chill(self):
        print("Time to play")
        self.gladness -= 5
        self.progress -= 0.1
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.slive = False
        elif self.progress > 5:
            print("Passed externally")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cude = random.randint(1, 3)
        if live_cude == 1:
            self.to_study()
        elif live_cude == 2:
            self.to_sleep()
        elif live_cude == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive ()

nick = Student(name="Nick")
for day in range(365):
    if nick.is_alive == False:
        break
    nick.live(day)'