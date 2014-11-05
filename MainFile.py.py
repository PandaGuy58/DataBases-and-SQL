import sqlite3

def create_table("coffee_shop.db",table_name,sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you with to recreate it (y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table withh be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def delete_product(data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "delete from Product where Name=?"
        cursor.execute(sql,data)
        db.commit()

def insert_data(values):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name,Price) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

def select_all_products():
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute('select * from Product')
        products = cursor.fetchall()
        return products

def update_product(data):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        sql = "update Product set Name=?, Price=? where ProductID=?"
        cursor.execute(sql,data)
        db.commit()

def select_product(ProductID):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product where ProductID=?",(ProductID,))
        product = cursor.fetchone()
        return product

def addProduct("coffee_shop.db"):
    complete = False
    while not complete:
        print("Enter the name of the product or press enter to leave")
        productName = input("Name of the product: ")
        if len(productName) == 0:
            complete = True
            print("addProduct canceled")

        while not complete:
            print("Enter the price of the product or press enter to leave")
            productPrice = input("Product price: ")
            if len(productPrice) == 0:
                complete = True
            else:
                try:
                    productPrice = float(productPrice)
                except:
                    print("You must enter a float")
            while not complete:
                insert_data((productName,productPrice))
                complete = True
                print("Successful!")
                

def menu():
    print("Product Table Menu")
    print()
    print("1. (Re)Create Product Table")
    print("2. Add New Product")
    print("3. Edit Existing Product")
    print("4. Delete Existing Product")
    print("5. Search for Products")
    print("0. Exit")
    print()

if __name__ == "__main__":
    sql = """CREATE TABLE Product(
    ProductID integer,
    Name text,
    Price real,
    Primary Key(ProductID))"""

    boolean = False
    while not boolean:
        menu()

        choice = input("Enter one of the options above: ")
        choice = int(choice)
        if choice == '1':
            create_table("coffee_shop.db","Product",sql)
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '0':
            pass

        else:
            print("You must enter a number 0-5!")








            
            
    
