class Person:
    id = None
    full_name = None
    age = None
    ph_num = None
    emply_type = None

    def __init__(self):
        pass


# --------------------------------------------------------------------------------
class Client(Person):
    def __init__(self, id, name, age, id_no, ph_num):
        self.id = id
        self.full_name = name
        self.age = age
        self.id_no = id_no
        self.ph_num = ph_num


# ---------------------------------------------------------------------------------
class Librarian(Person):
    def __init__(self, id, name, age, id_no, emply_type):
        self.id = id
        self.full_name = name
        self.age = age
        self.id_no = id_no
        self.emply_type = emply_type


# --------------------------------------------------------------------------------
class Book:
    id = []
    title = []
    description = []
    author = []
    status = []

    def __init__(self, id, title, des, author, status):
        self.id.append(id)
        self.title.append(title)
        self.description.append(des)
        self.author.append(author)
        self.status.append(status)


# --------------------------------------------------------------------------------
class Borr_order:
    id = []
    date = []
    client_id = []
    book_id = []
    status = []

    def __init__(self, id, date, client_id, book_id, status):
        self.id.append(id)
        self.date.append(date)
        self.client_id.append(client_id)
        self.book_id.append(book_id)
        self.status.append(status)


# --------------------------------------------------------------------------------
class Main_file:
    clients = []
    librarians = []
    books = []
    borr_order = []
    total_borr_book = None
    total_avail_book = None
    total_borr_order = None

    def __init__(self, num):
        self.total_borr_book = num
        self.total_avail_book = len(self.books) - num
        self.total_borr_order = len(self.borr_order)


# --------------------------------------------------------------------------------
id1 = 0
id2 = 9  # counters
id3 = 99
id4 = 999
id5=0
# ---------------------------------------------------------------------

while True:
    m=0
    m2=0
    for i in Book.status:
        if i=="active":
            m+=1
        elif i=="inactive" :
            m2+=1
    print("Welcome to the Gaza Library ")
    print("total_borr_book "+str(m2))
    print("total_avail_book is " + str(m))
    print("total_borr_order " + str(len(Main_file.borr_order)))
    num = input("""input the number of process you need to do
           1- Create a new client
           2-Create a new librarian
           3-Create a new books
           4-Ask Librarian to borrow a book
           5-Return book""")
    # ---------------------------------------------------------------------------
    if int(num) == 1:
        print("Welcome to the Gaza Library ")
        id1 = id1 + 1
        name = input("enter your name")
        age = input("enter your age")
        id_no = input("enter your ID Number")
        ph_num = input("enter your phone number")
        client = Client(id1, name, age, id_no, ph_num)
        Main_file.clients.append(id1)
        print("Wonderful, you have become one of the members of the Gaza Library as a client ")
        stop = input("Enter (s) to pause or enter (r) to return to the main screen")
        if stop == "s":
            break
        elif stop == "r":
            continue
        else:
            print(" wrong input")
            break
    # ---------------------------------------------------------------------------------------
    if int(num) == 2:
        print("Welcome to the Gaza Library ")
        id2 = id2 + 1
        name = input("enter your name")
        age = input("enter your age")
        id_no = input("enter your ID Number")
        emply_type = input("enter your (full or part)")
        librarian = Librarian(id2, name, age, id_no, emply_type)
        Main_file.librarians.append(id2)
        print("Wonderful, you have become one of the members of the Gaza Library as a librarian")
        stop = input("Enter (s) to pause or enter (r) to return to the main screen")
        if stop == "s":
            break
        elif stop == "r":
            continue
        else:
            print(" wrong input")
            break
    # ---------------------------------------------------------------------------------------------------
    if int(num) == 3:
        print("Welcome to the Gaza Library ")
        id3 += 1
        title = input("enter the title of book")
        des = input("enter the description of book")
        author = input("enter the author name of book")
        status = input("enter the status of book(active-inactive)")
        book = Book(id3, title, des, author, status)
        Main_file.books.append(id3)
        stop = input("Enter (s) to pause or enter (r) to return to the main screen")
        if stop == "s":
            break
        elif stop == "r":
            continue
        else:
            print(" wrong input")
            break
    # -----------------------------------------------------------------------------------------------------
    if int(num) == 4:
        name_book = input("enter the name of the book you want to borrow.")
        if name_book in Book.title:
            for i in Book.title:
                if name_book == i:
                    ind = Book.title.index(i)
                    if Book.status[ind] == "active":
                        client_id = input("enter your id_no")
                        if client_id == client.id_no:
                            id4 += 1
                            id5+=1
                            Main_file.borr_order.append(id5)
                            date = input("enter the date of borrow process")
                            book_id = Book.id[ind]
                            status = input("enter status of borring (active - expired - cancelled)")
                            borr_order=Borr_order(id4,date,client_id,book_id,status)
                            Book.status[ind] = "inactive"
                            print("process of borrow book is don your id of prrowing is "+str(id4)+"keb it in your mind")
                            stop = input("Enter (s) to pause or enter (r) to return to the main screen")
                            if stop == "s":
                                break
                            elif stop == "r":
                                continue
                            else:
                                print(" wrong input")
                                break

                        else:
                            print("you are not member in the library ")
                            break
                    else:
                        print("sorry the book had been borrowed")
                        break
        else:
            print("the name of book you need dose not exist")
            break
# ------------------------------------------------------------------------------------------
    if int(num)==5:
        print("Welcome to the Gaza Library ")
        borr_id=input("enter the borr the id ")
        if int(borr_id)in Borr_order.id:
                 for i in Borr_order.id:
                          if int(borr_id)==i:
                               indx = Borr_order.id.index(i)
                               if Borr_order.status[indx]=="active" :
                                      Borr_order.status[indx]="cancelled"
                                      id5+=1
                                      Main_file.borr_order.append(id5)
                                      name=Borr_order.book_id[indx]
                                      i=Book.id.index(name)
                                      Book.status[i]="active"
                                      print("the process of cancelled is done thank you ")
                                      stop = input("Enter (s) to pause or enter (r) to return to the main screen")
                                      if stop == "no":
                                          break
                                      elif stop == "yes":
                                         continue
                                      else:
                                          print(" wrong input")
                                          break
                               else:
                                  print("the book is already available now")
                                  break
