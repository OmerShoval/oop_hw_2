class Company:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(self.employees)

    def annual_expense(self):
        bonus = self.employees[0].get_bonus()
        salary = self.employees[0].monthly_salary
        annual_expenses = bonus + salary
        print(f"the employee anuall expeneses are {annual_expenses}")


