#first step 1
from abc import ABC,abstractmethod
# create class
class all1(ABC):
    @abstractmethod
    def prints(self):
        return 0
# in inherate
class Employee1(all1):
    pro='code'
    no=12
    def __init__(self,name,salary,id):
        self.name=name
        self.salary=salary
        self.id=id
    def prints(self):
        print("the name of employee  and salary  ,id")

    @staticmethod
    def printer():
        print("the name of employee  and salary  ,id")

avinash=Employee1('avinash', 150000, 12321)
avinash.prints()
