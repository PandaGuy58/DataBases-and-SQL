import sqlite3

def insert_data(values):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name,Price) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    product = ("Espresso",1.5)
    insert_data(product)
