class avinash:
    # constractor
    no=12
    def __init__(self,n,s):
        self.name=n
        self.sharname=s
    def func(self,n):
        self.so=n
    @classmethod
    def func1(cls,n):
        cls.no=n
    pass
avi=avinash('avinash', 'sharma')
avi.func(100)
print(avi.so,avi.no)
avi.func1(10)
print(avi.name,avi.sharname)
print(avi.so,avi.no)