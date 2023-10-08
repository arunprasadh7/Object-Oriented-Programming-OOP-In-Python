# 3 Inheritance- one class takes the properties of other class
# main: parent class  ,lower: child class

# inherits, extends, overide

# base/ parent class
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f'{self.name} is working....')

# child class


class SoftwareEngineer(Employee):

    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f'{self.name} is coding...')

    def debug(self):
        print(f'{self.name} is debugging...')

# child class


class Designer(Employee):

    def draw(self):
        print(f'{self.name} is drawing....')


se = SoftwareEngineer('Arc', 27, 5000, 'Junior')
print(se.name, se.age)
se.work()
print(se.level)
se.debug()

print()

de = Designer('Invoker', 20, 7000)
print(de.name, de.age)
de.work()
de.draw()

print()

# Polymorphism - many faces

employees = [SoftwareEngineer('Arc', 27, 5000, 'Junior'),
             SoftwareEngineer('Luna', 30, 9000, 'Senior'),
             Designer('Invoker', 20, 7000)]


def motivateEmployee(employees):
    for i in employees:
        i.work()


motivateEmployee(employees)