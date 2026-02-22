class Employee:
    def __init__(self, name, emp_id, department, basic_salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.basic_salary = basic_salary

    def calculate_salary(self):
        # Allowances
        da = 0.92 * self.basic_salary  # 92% DA
        hra = 0.58 * self.basic_salary  # 58% HRA
        ta = 0.30 * self.basic_salary  # 30% TA

        # Deduction
        lic = 500  # Fixed LIC deduction

        # Gross and Net Salary
        gross_salary = self.basic_salary + da + hra + ta
        net_salary = gross_salary - lic

        return da, hra, ta, gross_salary, net_salary

    def display_details(self):
        da, hra, ta, gross_salary, net_salary = self.calculate_salary()

        print("\n----- Employee Details -----")
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)
        print("Basic Salary: Rs.", self.basic_salary)
        print("DA (92%): Rs.", da)
        print("HRA (58%): Rs.", hra)
        print("TA (30%): Rs.", ta)
        print("LIC Deduction: Rs. 500")
        print("Gross Salary: Rs.", gross_salary)
        print("Net Salary: Rs.", net_salary)


# Taking input from user
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

# Create Employee object
emp = Employee(name, emp_id, department, basic_salary)

# Display details and salary
emp.display_details()