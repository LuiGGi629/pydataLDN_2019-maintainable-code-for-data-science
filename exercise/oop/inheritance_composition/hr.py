class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating Payroll")
        print("===================")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            print("")


class Employee:
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary) -> None:
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate) -> None:
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class ComissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, comission) -> None:
        super().__init__(id, name, weekly_salary)
        self.comission = comission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.comission
