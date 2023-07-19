import os


class Index:
    def __init__(self):
        self.arr = []
        self.map = {}
        self.ID_1 = "21bce7985"
        self.ID_2 = "21bce7914"
        self.load_data()

    def load_data(self):
        try:
            with open("Test.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line:
                        self.arr.append(line)
        except Exception as e:
            print("Something went wrong....")

    def issue(self, book)->bool:
        if book in self.arr:
            print("Your book", book, "is issued")
            self.arr.remove(book)
            self.map[book] = self.count(book)
            self.update_file("Test.txt", book, "")
            return True
        else:
            print("The searched book is not available in the library. Sorry for the inconvenience!!")
            print("Please try again later")
            return False

    def return_book(self, book):
        try:
            with open("search.txt", "r") as file:
                lines = file.readlines()
                returned = False
                for line in lines:
                    line = line.strip()
                    if line == book:
                        self.addit(book, 1)
                        print("You have successfully returned your book")
                        returned = True
                        break
                if not returned:
                    print("This book doesn't belong to this library. You can't return it.")
            return returned
        except Exception as e:
            print("Something went wrong....")

    def search_book(self, book):
        if book in self.arr:
            count = self.count(book)
            return count,book
            # print("There are", count, book, "books in the library. You can take them.")
        else:
            # print("Your book is not available in the library. Sorry!!")
            return 0," "

    def addit(self, id, book, nob):
        try:
            print(id,book,nob)
            id = str(id)
            ID_1 = "21bce7985"
            ID_2 = "21bce7914"
            if id == ID_1 or id == ID_2:
                print("hello")
                for _ in range(nob):
                    self.arr.append(book)
                self.map[book] = self.count(book)
                self.update_file("Test.txt", "", book)
                if not self.search_database(book):
                    self.update_file("search.txt", "", book)
                return True
            else:
                return False
        except Exception as e:
            print("Something went wrong....")

    def count(self, book):
        return self.arr.count(book)

    def list_books(self):
        for book in self.arr:
            if book != "":
                self.map[book] = self.count(book)
        # print(self.map)
        return self.map

    def help(self):
        return """
        These are the functionalities you can use:
        1. Type 'issue' to get any book from the library.
        2. Type 'return' to give back the book to the library.
        3. Type 'search' to find any book in the library.
        4. Type 'add' to add any book to the shelf (for librarian).
        5. Type 'count' to know the count of a particular book.
        6. Type 'list' to see the list of available books in the library.
        """

    def exit(self):
        return False

    def ask(self):
        a = True
        print("If you want to do something else, please type 'Y' or type 'N' to exit.")
        hlp = input().lower()
        if hlp == "y":
            a = True
        elif hlp == "n":
            a = self.exit()
        else:
            print("Please type 'N' or 'Y' to proceed.")
            rtr1 = input().lower()
            if rtr1 == "y":
                a = True
            elif rtr1 == "n":
                a = self.exit()
        return a

    def search_database(self, book):
        searched = False
        try:
            with open("search.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line == book:
                        searched = True
                        break
                    else:
                        searched = False
        except Exception as e:
            print("Something went wrong....")
        return searched

    def update_file(self, filename, to_remove, to_add):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
            with open(filename, "w") as file:
                for line in lines:
                    line = line.strip()
                    if line != to_remove:
                        file.write(line + "\n")
                if to_add:
                    file.write(to_add + "\n")
        except Exception as e:
            print("Something went wrong....")


if __name__ == "__main__":
    index = Index()
    while True:
        print("This is the library management system please type help to get the information.")
        choice = input("Enter your choice: ")
        if choice=='help':
            print(index.help())
        elif choice == "issue":
            book = input("Enter the book name: ")
            index.issue(book)
        elif choice == "return":
            book = input("Enter the book name: ")
            index.return_book(book)
        elif choice == "search":
            book = input("Enter the book name: ")
            index.search_book(book)
        elif choice == "add":
            print("This option is only for authorized members.")
            id = input("Enter your ID: ")
            if id == index.ID_1 or id == index.ID_2:
                book_name = input("Enter the book name that you want to add: ")
                no_of_books = int(input("Please enter the number of books to be added: "))
                index.addit(id,book_name, no_of_books)
                print("Your", book_name, "book is added successfully.")
            else:
                print("You are not authorized to add books.")
            # index.addit(book, nob)
        elif choice == "count":
            book = input("Enter the book name: ")
            count = index.count(book)
            print("Count of", book, "is", count)
        elif choice == "list":
            index.list_books()
        else:
            print("Invalid choice")
        if not index.ask():
            break




#
# import mysql.connector
#
#
# class Index:
#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host="localhost",
#             user="your_username",
#             password="your_password",
#             database="library"
#         )
#         self.cursor = self.conn.cursor()
#         self.ID_1 = "21bce7985"
#         self.ID_2 = "21bce7914"
#         self.load_data()
#
#     def load_data(self):
#         query = "SELECT book_name FROM books"
#         self.cursor.execute(query)
#         self.arr = [row[0] for row in self.cursor.fetchall()]
#
#     def issue(self, book):
#         if book in self.arr:
#             print("Your book", book, "is issued")
#             self.arr.remove(book)
#             self.update_database(book, "", "issued")
#         else:
#             print("The searched book is not available in the library. Sorry for the inconvenience!!")
#             print("Please try again later")
#
#     def return_book(self, book):
#         query = "SELECT book_name FROM issued_books WHERE book_name = %s"
#         self.cursor.execute(query, (book,))
#         result = self.cursor.fetchone()
#         if result:
#             self.addit(book, 1)
#             print("You have successfully returned your book")
#         else:
#             print("This book doesn't belong to this library. You can't return it.")
#
#     def search_book(self, book):
#         query = "SELECT COUNT(*) FROM books WHERE book_name = %s"
#         self.cursor.execute(query, (book,))
#         count = self.cursor.fetchone()[0]
#         if count > 0:
#             print("There are", count, book, "books in the library. You can take them.")
#         else:
#             print("Your book is not available in the library. Sorry!!")
#
#     def addit(self, book, nob):
#         for _ in range(nob):
#             self.arr.append(book)
#         self.update_database(book, "issued", "")
#
#     def count(self, book):
#         return self.arr.count(book)
#
#     def list_books(self):
#         query = "SELECT book_name, COUNT(*) FROM books GROUP BY book_name"
#         self.cursor.execute(query)
#         self.map = {row[0]: row[1] for row in self.cursor.fetchall()}
#         print(self.map)
#
#     def help(self):
#         return """
#         These are the functionalities you can use:
#         1. Type 'issue' to get any book from the library.
#         2. Type 'return' to give back the book to the library.
#         3. Type 'search' to find any book in the library.
#         4. Type 'add' to add any book to the shelf (for librarian).
#         5. Type 'count' to know the count of a particular book.
#         6. Type 'list' to see the list of available books in the library.
#         """
#
#     def exit(self):
#         self.cursor.close()
#         self.conn.close()
#         return False
#
#     def ask(self):
#         a = True
#         print("If you want to do something else, please type 'Y' or type 'N' to exit.")
#         hlp = input().lower()
#         if hlp == "y":
#             a = True
#         elif hlp == "n":
#             a = self.exit()
#         else:
#             print("Please type 'N' or 'Y' to proceed.")
#             rtr1 = input().lower()
#             if rtr1 == "y":
#                 a = True
#             elif rtr1 == "n":
#                 a = self.exit()
#         return a
#
#     def update_database(self, book, from_status, to_status):
#         if from_status:
#             query = "DELETE FROM issued_books WHERE book_name = %s"
#             self.cursor.execute(query, (book,))
#         if to_status:
#             query = "INSERT INTO issued_books (book_name) VALUES (%s)"
#             self.cursor.execute(query, (book,))
#         self.conn.commit()
#
#
# if __name__ == "__main__":
#     index = Index()
#     while True:
#         print("This is the library management system please type help to get the information.")
#         choice = input("Enter your choice: ")
#         if choice == 'help':
#             print(index.help())
#         elif choice == "issue":
#             book = input("Enter the book name: ")
#             index.issue(book)
#         elif choice == "return":
#             book = input("Enter the book name: ")
#             index.return_book(book)
#         elif choice == "search":
#             book = input("Enter the book name: ")
#             index.search_book(book)
#         elif choice == "add":
#             print("This option is only for authorized members.")
#             id = input("Enter your ID: ")
#             if id == index.ID_1 or id == index.ID_2:
#                 book_name = input("Enter the book name that you want to add: ")
#                 no_of_books = int(input("Please enter the number of books to be added: "))
#                 index.addit(book_name, no_of_books)
#                 print("Your", book_name, "book is added successfully.")
#             else:
#                 print("You are not authorized to add books.")
#         elif choice == "count":
#             book = input("Enter the book name: ")
#             count = index.count(book)
#             print("Count of", book, "is", count)
#         elif choice == "list":
#             index.list_books()
#         else:
#             print("Invalid choice")
#         if not index.ask():
#             break
