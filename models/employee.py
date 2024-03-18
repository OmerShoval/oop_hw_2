class Employee:

    def __init__(self, name, age, role, year_joined):
        self.__name = name
        self.__age = age
        self.__role = role
        self.__year_joined = year_joined

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role


    @property
    def year_joined(self):
        return self.__year_joined

    @year_joined.setter
    def year_joined(self, year_joined):
        self.__year_joined = year_joined

    def __calculate_bonus(self):
        return self.__role.monthly_salary_factor * self.__role.monthly_salary

    def get_bonus(self):
        bonus = self.__calculate_bonus()
        print(f"{self.__name}, you got {bonus} as the annual bonus.")

    def print_employee(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Position: {self.__role.name}")
        print(f"Salary: {self.__role.monthly_salary}")
        print(f"Bonus Factor: {self.__role.monthly_salary_factor}")
        print(f"Hire Date: {self.__year_joined}")

    def promote(self, role):
        self.__role = role
        self.print_employee()
