from models.employee import *
from models.role import *
from models.company import *


if __name__ == '__main__':

    product_manager = Role("Product manager", 445, 10000, 2.0)
    software_developer = Role("software_developer", 554, 20000, 0.5)

    employee_1 = Employee("Amir", 40, product_manager,  2000)
    employee_2 = Employee("Avi", 40, software_developer, 1999)

    company_instance = Company()
    company_instance.add_employee(employee_2)


