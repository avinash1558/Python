class Library:
    def __init__(self,lists,name):
        self.bookList= lists
        self.userName= name
        self.lendDict={}

    def displayBook(self):
        print(f"we have following books inside of library : {self.userName}")
        for book in self.bookList:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender-book database has been updated")

    def addBook(self,book):
        self.bookList.append(book)
        print("book has been add")

    def returnBook(self,book):
        self.bookList.remove(book)

avinashLibrary=Library(['python','c++','c','java','javascript','php','flask'], 'avinashLibrary')
while(1):
    print(f"welcome to {avinashLibrary.userName} , enter the number for option :\n ")
    print("1. Display book")
    print("2. Lend book")
    print("3. Add book")
    print("4. Return book")
    user =int(input())
    if user==1:
        avinashLibrary.displayBook()
    elif user==2:
        book=input('Enter book name you want to lend : ')
        name=input("Enter your name : ")
        avinashLibrary.lendBook(name, book)
    elif user==3:
        book=input('Enter book name you want to add : ')
        avinashLibrary.addBook(book)
    elif user==4:
        book=input('Enter book name you want to return : ')
        avinashLibrary.returnBook(book)
    else :
        print('Not valid option')
    print('press enter q for quit and any key for continue')
    option=input()
    if option=='q':
        break
    else:
        continue
