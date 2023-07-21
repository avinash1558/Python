class Employee:
    pro='code'
    no=12
    def __init__(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id
    @classmethod
    def alternative(cls,str):
    #     slice_str= str.split(' ')
    # #           def __init__(self,name,salary,id):
    #     return cls(slice_str[0],slice_str[1],slice_str[2])
        return cls(*str.split(" "))
    @staticmethod
    def printer():
        print("the name of employee  and salary  ,id")

avinash=Employee('avinash', 150000, 12321)
avinash.printer()
Employee.printer()

