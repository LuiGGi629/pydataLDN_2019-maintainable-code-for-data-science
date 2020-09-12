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


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, comission) -> None:
        super().__init__(id, name, weekly_salary)
        self.comission = comission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.comission


class Manager(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} screams and yells for {hours} hours.")


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours doing office paperwork.")


class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f"{self.name} expends {hours} hours on the phone.")


class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f"{self.name} manufactures gadgets for {hours} hours.")


class TemporarySecretary(HourlyEmployee, Secretary):
    def __init__(id, name, hours_worked, hour_rate):
        super().__init__(id, name, hours_worked, hour_rate)
