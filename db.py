import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM parts")  # Read all
        rows = self.cur.fetchall()
        return rows

    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)",  # Protection against SQL injection
                         (part, customer, retailer, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?",
                         (id,))  # Trailing comma for tuple
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",
                         (part, customer, retailer, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# # Initialising DB
# db = Database('store.db')  # database name 'store.db'

# # Inserting data in DB:
# db.insert("8GB DDR4 RAM", "I.P Freely", "Argos", "130")
# db.insert("NVDIA 3080 GPU", "Maya Normousbutt", "Currys", "700")
# db.insert("INTEL I7-4790K CPU", "Ben Dover", "PC World", "250")
# db.insert("24 Inch 120Hz ASUS Monitor", "Oliver Klozoff", "eBay", "500")
# db.insert("Gaming Mouse ROG ASUS", "Mike Rotch", "Amazon", "85")
# db.insert("Sony Playstation 5 Pro 2TB", "M. Ray Chakmac", "Amazon", "485")
