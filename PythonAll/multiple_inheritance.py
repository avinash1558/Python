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

class Employee2:
    pro='23'
    # overloading function
    def __init__(self,name,salary,id,value):
        self.name=name
        self.salary=salary
        self.id=id
        self.program=value
    @staticmethod
    def printer():
        print("2nd base class")

# class multiple(Employee1,Employee2):
class multiple(Employee2,Employee1):
    @staticmethod
    def printer():
        print("3nd base class")

avinash=multiple('avinash', 123000, 10232,"python")
avinash.printer()
