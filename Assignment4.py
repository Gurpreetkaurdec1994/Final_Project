#Gurpreet kaur

""" This program demonstrates the connectivity with the database
along with CRUD ( Create, Read, Update and Delete) operations usig GUI( Graphical User Interface) Tkinter
"""

from tkinter import *
from tkinter.ttk import Frame, Label, Entry
import sqlite3 as sql
import csv

class Assignment4(Frame):
    print("This program is written by Gurpreet Kaur")
    __author__ = "Gurpreet kaur"
    def _init_(self):
        super()._init_()

        """ calling other methods using self object"""

        self.GUI()
        self.load()
        self.listbox
        self.database()
        self.delete()

    """ GUI Method that takes self object and demonstrates the use of Frame, List and widgets buttons for CRUD operations and labels to display the columns names"""

    def GUI(self):
        __author__ = "Gurpreet kaur"
        self.master.title("Gurpreet Kaur #040893454")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        self.specieslabel = Label(frame1, text="Species", width=15)
        self.specieslabel.pack(side=LEFT, padx=5, pady=5)



        self.species = Entry(frame1)
        self.species.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        self.yearlabel = Label(frame2, text="year", width=15)
        self.yearlabel.pack(side=LEFT, padx=5, pady=5)

        self.year = Entry(frame2)
        self.year.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        self.daylabel = Label(frame3, text="Julain day of year", width=15)
        self.daylabel.pack(side=LEFT, padx=5, pady=5)

        self.day = Entry(frame3)
        self.day.pack(fill=X, padx=5, expand=True)

        frame4 = Frame(self)
        frame4.pack(fill=X)

        self.pidlabel = Label(frame4, text="Plant Identification", width=15)
        self.pidlabel.pack(side=LEFT, padx=5, pady=5)

        self.pid = Entry(frame4)
        self.pid.pack(fill=X, padx=5, expand=True)

        frame5 = Frame(self)
        frame5.pack(fill=X)


        self.budlabel = Label(frame5, text="Number of Buds", width=15)
        self.budlabel.pack(side=LEFT, padx=5, pady=5)

        self.bud = Entry(frame5)
        self.bud.pack(fill=X, padx=5, expand=True)

        frame6 = Frame(self)
        frame6.pack(fill=X)

        self.flowerlabel = Label(frame6, text="Number of Flowers", width=15)
        self.flowerlabel.pack(side=LEFT, padx=5, pady=5)

        self.flower = Entry(frame6)
        self.flower.pack(fill=X, padx=5, expand=True)

        frame7 = Frame(self)
        frame7.pack(fill=X)

        self.maturitylabel = Label(frame7, text="Maturity", width=15)
        self.maturitylabel.pack(side=LEFT, padx=5, pady=5)

        self.maturity = Entry(frame7)
        self.maturity.pack(fill=X, padx=5, expand=True)

        frame8 = Frame(self)
        frame8.pack(fill=X)

        self.inilabel = Label(frame8, text="Observer Initials", width=15)
        self.inilabel.pack(side=LEFT, padx=5, pady=5)


        self.initials = Entry(frame8)
        self.initials.pack(fill=X, padx=5, expand=True)

        frame9 = Frame(self)
        frame9.pack(fill=X)


        self.commentlabel = Label(frame9, text="Observer comments", width=15)
        self.commentlabel.pack(side=LEFT, padx=5, pady=5)

        self.comment = Entry(frame9)
        self.comment.pack(fill=X, padx=5, expand=True)

        frame10 = Frame(self)
        frame10.pack(fill=X)

        self.updatelabel = Label(frame10, text="Enter ID below and click update", width=30)
        self.updatelabel.pack(side=LEFT, padx=5, pady=5)

        self.submit = Button(frame10,text="Submit", width=10,command= lambda: Assignment4.insert(self))
        self.submit.pack(side=RIGHT, padx=5, pady=5)

        frame11 = Frame(self)
        frame11.pack(fill=X)

        __author__ = "Gurpreet Kaur"

        self.id_button = Button(frame11, text="Update", width=15,command= lambda: Assignment4.update(self))
        self.id_button.pack(side=RIGHT, padx=5, pady=5)

        self.searchid = Entry(frame11)
        self.searchid.pack(fill=X, padx=5)

        frame12 = Frame(self)
        frame12.pack(fill=X)

        self.del_button = Button(frame12, text="Delete", width=15,command= lambda: Assignment4.delete(self))
        self.del_button.pack(side=RIGHT, padx=5, pady=5)

        self.del_entry = Entry(frame12)
        self.del_entry.pack(fill=X, padx=5)

        frame13 = Frame(self)
        frame13.pack(fill=X)

        self.show = Button(frame13, text="Load Data", width=15,command= lambda: Assignment4.load(self))
        self.show.pack(side=LEFT, padx=5, pady=5)


        frame14 = Frame(self)
        frame14.pack(side=RIGHT, fill=Y)

        self.listbox = Listbox(frame14, width=100)
        self.listbox.pack(side="right", fill=Y)

        return "gui"

    """ database method to create table named species with different column names and primary key but before 
        create a new table named species it checks if any table exist with the same name or not 
        if exist, then it deletes that table first and the create a new table"""

    def  database(self):
        connection = sql.connect("Finalproject.db")
        __author__ = "Gurpreet kaur"

        with connection:
            dbCursur = connection.cursor()

            dbCursur.execute("drop table if exists species;")

            dbCursur.execute(
                'create table species (id INTEGER PRIMARY KEY AUTOINCREMENT,species VARCHAR(10),year INTEGER ,day INTEGER,plantID INTEGER,buds INTEGER,flowers VARCHAR(10),maturity INTEGER ,initial VARCHAR(10),comment VARCHAR(30))')
        return "database"

    """ load method to load data from file into database table with the help of for loop"""

    def load(self):

        __author__ = "Gurpreet Kaur"
        """" Try block to check the existence of the file"""
        try:
            with open('Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv') as file:
                var = csv.reader(file)
                next(var)
                next(var)
                csvData = []
                i = 0
                for d in var:
                    if(i<10):
                        csvData.append(d)
                    i = i + 1

                self.listbox.delete(0,END)
                connection = sql.connect("Finalproject.db")
                with connection:
                    dbCursur = connection.cursor()

                    for row in csvData:
                        print(row)
                        dbCursur.execute('INSERT INTO species (species,year,day,plantID,buds,flowers,maturity,initial,comment) values (?,?,?,?,?,?,?,?,?)',(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
                    get = dbCursur.execute('SELECT * FROM species')
                    for row in get:
                        self.listbox.insert(END,row)

        except:
            print("Error: file is missing or not available")
        return "dataread"

    """ insert method to get input from user and insert data into species table using sql statement"""

    def insert(self):

        __author__ = "Gurpreet Kaur"
        self.listbox.delete(0, END)

        connection = sql.connect("Finalproject.db")
        with connection:
            dbCursur = connection.cursor()

            dbCursur.execute(
                'INSERT INTO species (species,year,day,plantID,buds,flowers,maturity,initial,comment) values (?,?,?,?,?,?,?,?,?)',
                ([(self.species.get()), (self.year.get()),(self.day.get()),(self.pid.get()),(self.bud.get()),(self.flower.get()),(self.maturity.get()),(self.initials.get()),(self.comment.get())]))
            get = dbCursur.execute('SELECT * FROM species')
            for row in get:
                self.listbox.insert(END, row)
            self.species.delete(0,END)
            self.year.delete(0,END)
            self.day.delete(0,END)
            self.pid.delete(0,END)
            self.bud.delete(0,END)
            self.flower.delete(0,END)
            self.maturity.delete(0,END)
            self.initials.delete(0,END)
            self.comment.delete(0,END)

        return "insert"

    """update method to modify the records into database"""

    def update(self):

        __author__ = "Gurpreet Kaur"
        self.listbox.delete(0, END)

        connection = sql.connect("Finalproject.db")
        with connection:
            dbCursur = connection.cursor()

            dbCursur.execute(
                "UPDATE species SET species=?,year=?,day=?,plantID=?,buds=?,flowers=?,maturity=?,initial=?,comment=? where id=?",
                (self.species.get(),
                 self.year.get(),
                 self.day.get(),
                 self.pid.get(),
                 self.bud.get(),
                 self.flower.get(),
                 self.maturity.get(),
                 self.initials.get(),
                 self.comment.get(),
                 self.searchid.get()))
            get = dbCursur.execute('SELECT * FROM species')
            for row in get:
                self.listbox.insert(END, row)
        app.listbox.insert(END, "data updated")
        self.species.delete(0, END)
        self.year.delete(0, END)
        self.day.delete(0, END)
        self.pid.delete(0, END)
        self.bud.delete(0, END)
        self.flower.delete(0, END)
        self.maturity.delete(0, END)
        self.initials.delete(0, END)
        self.comment.delete(0, END)
        return "update"

    """method to delete a specific record from database"""

    def delete(self):


        __author__ = "Gurpreet Kaur"
        self.listbox.delete(0, END)

        connection = sql.connect("Finalproject.db")
        with connection:
            dbCursur = connection.cursor()
            id = self.del_entry.get()
            print("select id "+id)

            dbCursur.execute("DELETE FROM species where id=?",id)
            get = dbCursur.execute('SELECT * FROM species')
            for row in get:
                self.listbox.insert(END, row)

        app.listbox.insert(END, "data deleted")

        return "delete"

    """Search method to search a particular record from the list"""

    def search(self):

        app.listbox.insert(END,"DATA SEARCHED")

        return "serach"

app = Assignment4()

""" main methods that invokes the other methods with the help of object"""

def main():
    root = Tk()
    app.GUI()
    app.database()
    root.mainloop()

""" main starting point of the program execution """

if __name__ == '__main__':
    main()