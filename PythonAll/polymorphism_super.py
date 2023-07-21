class Employee1:
    pro1='code'
    no=12
    def __init__(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id
    @staticmethod
    def printer():
        print("the name of employee  and salary  ,id")

class Employee2(Employee1):
    pro='23'
    # overloading function
    def __init__(self,name,salary,id,value):
        # self.name=name
        # self.salary=salary
        # self.id=id
        super().__init__(name, salary, id)
        self.program=value

avinash=Employee2('avinash', 150000, 12321,'c++')
avinash.printer()
print(avinash.name)
print(avinash.salary)
print(avinash.id)
print(avinash.program)
print(avinash.pro)
print(avinash.pro1)