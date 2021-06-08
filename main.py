class Employee:
    count = 0

    def profile(self, n, a, s, c):
        self._name = n
        self._age = a
        self._salary = s
        self._company = c

    def printData(self):
        print(f"Employee name is {self._name}")
        print(f"Employee age is {self._age}")
        print(f"Employee salary is {self._salary}")
        print(f"Employee company is {self._company}")

e1 = Employee()
e1.profile("Saarthak", 11, 21000, 'xyz')
Employee.count = 1
e1.printData()
print(f"The number of Employees working at xyz are {Employee.count}")