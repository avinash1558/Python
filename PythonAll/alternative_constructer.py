class Employee:
    pro='code'
    no=12
    def __init__(self,name1,salary1,id1):
        self.name=name1
        self.salary=salary1
        self.id=id1
    def printer(self):
        print(f"the name of employee is '{self.name}' and salary '{self.salary}' ,id'{self.id}'")

    @classmethod
    def alternative(cls,str):
    #     slice_str= str.split(' ')
    # #           def __init__(self,name,salary,id):
    #     return cls(slice_str[0],slice_str[1],slice_str[2])

        return cls(*str.split(" "))

# avinash=Employee('avinash', 150000, 12321)
# avinash.printer()
avinash=Employee.alternative('avinash 150000 12321')
avinash.printer()
# print(Employee.alternative('avinasj sharma sis '))
