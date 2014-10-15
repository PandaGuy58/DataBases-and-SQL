import sqlite3

def insert_data(values):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name,Price) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

def create_table(db_name,table_name,sql):
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

def select_all_products():
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute('select * from Product')
        products = cursor.fetchall()
        return products

def select_product(id):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product where ProductID=/",(id,))
        product = cursor.fetchone()
        return product

def update_product(data):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        sql = "update Product set Name=?, Price=? where ProductID=?"
        cursor.execute(sql,data)
        db.commit()

def menu():
    print("Produc Table Menu")
    print()
    print("1. (Re)Crate Product Table")
    print("2. Add new product")
    print("3. Edit existing product")
    print("4. Delete Existing product")
    print("5. Search for products")
    print("0. Exit")
    print()

def main():
    complete = False
    while not complete:
        choice = input("Choose one of the options: ")
        if choice == '1':
            create_table(db_name,table_name,sql)
        elif choice == '2':
            insert_data(values)
        elif choice == '3':
            
            
    




