class Employee1:
    pro='code'
    no=12
    def __init__(self,name,sname,log):
        self.name=name
        self.sname=sname
        self.log=log
    @property
    def printer(self):
        print("the name of employee  and salary  ,id")

    def fun(self):
        return f'{self.name}.{self.sname}@{self.log}'
    
    def fun(self,lname):
        self.name=lname.split('.')[0]
        self.sname=(lname.split('@')[0]).split('.')[1]
        self.log=lname.split('@')[1]
        return f'{self.name}.{self.sname}@{self.log}'
# function.setter
# function()
# function.deleter
# function()
# deleter
    # def fun(self):
    #     self.name=none
    #     self.sname=none
    #     self.log=none 
    
avinash=Employee1('avinash',"sharma","gmail.com")
print(avinash.fun('avinash.sharma@gmail.com'))
print(avinash.fun())
# del fun