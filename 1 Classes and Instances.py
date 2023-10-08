# position, name ,age ,level, salary

se1 = ['Software engineer', 'Arun', 25, 'Junior', 5000]
se2 = ['FrontEnd developer', 'Arc', 27, 'Senior', 7000]


class SoftwareEngineer:

    # class attribute
    alias = 'Keyboard Magician'

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.level = level
        self.age = age
        self.salary = salary

# instance
se1 = SoftwareEngineer('Arun', 26, 'Junior', 5000)
print(se1.name, se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)


se2 = SoftwareEngineer('Arc', 27, 'Senior', 7000)
print(se2.name, se2.level, se2.salary)
print(se2.alias)
print(SoftwareEngineer.alias)