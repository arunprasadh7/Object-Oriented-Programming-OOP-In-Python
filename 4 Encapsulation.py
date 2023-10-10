# 4 Encapsulation -  hiding attribtues within class/ making them private
# _x is protected (one underscore)
# __x is private (double underscore)


class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None  # protected
        # self.__num_bugs_solved =0 	#private
        self._num_bugs_solved

    def code(self):
        self._num_bugs_solved

    # getter
    def get_salary(self):
        return self._salary

    # # setter
    # # check values, enforce constraints
    # def set_salary(self, value):
    # 	if value < 1000:
    # 		self._salary = 1000
    # 	if value > 20000:
    # 		self._salary = 20000
    # 	self._salary = value

    def set_salary(self, base_value):
        self.set_salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3


se = SoftwareEngineer('Arun', 26)
print(se.name, se.age)
# print(se._salary)	# protected attributes are accessible
# print(se.__num_bugs_solved)	#private attributes cannot be accessed outside class

se.set_salary(9000)
print(se.get_salary())



#code 2
class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_bugs_solved = 0

    def code(self):
        self._num_bugs_solved += 1

    # getter
    def get_salary(self):
        return self._salary

    # setter
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value*3


se = SoftwareEngineer('Arc', 25)
print(se.name, se.age)

se.set_salary(6000)
print(se.get_salary())


for i in range(70):
    se.code()

se.set_salary(6000)
print(se.get_salary())