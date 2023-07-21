class Employee1:
    pro='code'
    no=12
    def __init__(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id
    @staticmethod
    def printer():
        print("1st base class")
class Employee2(Employee1):
    pro='23'
    # overloading function
    def __init__(self,name,salary,id,value):
        self.name=name
        self.salary=salary
        self.id=id
        self.program=value
    def pri(self):
        print(self.name)
    @staticmethod
    def printer():
        print("2nd base class")

# class multiple(Employee1,Employee2):
class Employee3(Employee2):
    @staticmethod
    def printer():
        print("3nd base class")

avinash=Employee3('avinash', 123000, 10232,"python")
avinash.printer()
sharma=Employee2('sharma', 16300,233,"python")
print(avinash.name)
print(avinash.salary)
print(avinash.id)
print(avinash.program)
print(avinash.pro)
print(sharma.name)
print(sharma.salary)
print(sharma.id)
print(sharma.program)
print(sharma.pro)
avinash.pri()