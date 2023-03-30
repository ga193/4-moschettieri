from Book import Book
from User import User


class Order:

    def __init__(self,user:User, book: Book):
        self.user = user
        self.__orderlist = []
        self.__orderlist.append(book)

    def add_Book(self, book: Book):
        self.__orderlist.append(book)

    def remove_Book(self, book: Book):
        self.__orderlist.remove(book)

    def get_Orderlist(self) -> list:
        return self.__orderlist
    
    def get_Orderprice(self) -> float:
        tot=0
        for book in self.__orderlist:
            tot+=book.get_Price
        return tot 



