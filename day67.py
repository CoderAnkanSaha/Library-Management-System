# Library management
class Library:
    
    def __init__(self):
        self.nbooks = 0
        self.books =[]
    
    def addbook(self, book):
        self.books.append(book)
        self.nbooks = len(self.books)
    
    def showinfo(self):
        print(f"The library has {self.nbooks} books. The books are ")
        for book in self.books:
            print(book)

l1 = Library()

while True:
    text =input("Enter book name ? : ")
    print("type Quit to stop adding or to escape")
    l1.addbook(text)
    if text == "Quit":
        break
print("To see the books present type 'Y' or else to quit press any other alphabet and enter key ")
show = input("See the books present? ")
if show =="Y":
    l1.showinfo()
else:
    print("Thanks")

# l1.addbook("Harry Potter")
# l1.addbook("Jungle Book")
# l1.addbook("Julius Ceasar")
# l1.showinfo()
