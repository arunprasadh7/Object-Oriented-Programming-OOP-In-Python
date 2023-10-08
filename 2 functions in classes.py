# 2 functions in classes

se1 = ['Software engineer', 'Arun', 25, 'Junior', 5000]
se2 = ['FrontEnd developer', 'Arc', 27, 'Senior', 7000]
se3 = ['FrontEnd developer', 'Arc', 27, 'Senior', 7000]


class SoftwareEngineer:

    # class attribute
    alias = 'Keyboard Magician'

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.level = level
        self.age = age
        self.salary = salary

    def code(self):
        print(f'{self.name} is writing code...')

    def code_in_lang(self, language):
        print(f'{self.name} is writing code in {language}!!!')

    # def information(self):
    # 	information = f'name = {self.name}, age = {self.age}, level = {self.level}. '
    # 	return information

    # dunder method
    def __str__(self):  # automatically executes if the output is string
        information = f'Name : {self.name}, Age : {self.age}, Level :{self.level}.'
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
     	if age < 25:
     		return 5000
     	if age < 30:
     		return 7000
     	return 9000


# instance
se1 = SoftwareEngineer('Arun', 26, 'Junior', 5000)
print(se1.name, se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)


se2 = SoftwareEngineer('Arc', 27, 'Senior', 7000)
print(se2.name, se2.level, se2.salary)
print(se2.alias)
print(SoftwareEngineer.alias)


se1.code()
se2.code()

se1.code_in_lang('Python')
se2.code_in_lang('Java')

# print(se1.information())
# print(se2.information())

print(se1)
print(se2)

se3 = SoftwareEngineer('Arc', 25, 'Senior', 7000)
print(se2 == se3)


print(se1.entry_salary(20))
print(se1.entry_salary(29))
print(se1.entry_salary(45))

print(SoftwareEngineer.entry_salary(20))
print(SoftwareEngineer.entry_salary(27))
print(SoftwareEngineer.entry_salary(40))