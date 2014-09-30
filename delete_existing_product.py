import sqlite3

def delete_product(data):
    with sqlite3.connect("coffe_shop.db") as db:
        cursor = db.cursor()
        sql = "delete from Product where Name=?"
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    data = ("Latte",)
    delete_product(data)
