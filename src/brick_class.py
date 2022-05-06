import sqlite3 as sq

class bricksDB:

    def __init__(self):
        self.conn = sq.connect("../database/brick_database.db")
        self.stat = self.conn.cursor()

    def create_db(self):

        create_inventory = "CREATE TABLE IF NOT EXISTS Inventory (id_shelf INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE," \
                           " shelf_number int);"

        create_bricks = "CREATE TABLE IF NOT EXISTS Bricks (id_brick INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE," \
                        " brick_number text UNIQUE , qty int);"

        create_assignments = "CREATE TABLE IF NOT EXISTS Assignments (id_assignment INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE," \
                             " id_brick int," \
                             " id_shelf int," \
                             " FOREIGN KEY (id_brick) REFERENCES Bricks (id_brick)," \
                             " FOREIGN KEY (id_shelf) REFERENCES Inventory (id_shelf));"

        create_images = "CREATE TABLE IF NOT EXISTS Images (id_image INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE," \
                        " id_brick int ," \
                        " img_path string," \
                        " FOREIGN KEY (id_brick) REFERENCES Bricks(id_brick));"

        self.stat.execute(create_inventory)
        self.stat.execute(create_bricks)
        self.stat.execute(create_assignments)
        self.stat.execute(create_images)
        self.conn.commit()
        return

    def add_brick(self, qty, brickNum):
        add = f"INSERT INTO Bricks(brick_number, qty) VALUES({brickNum},{qty})" \
              f"ON CONFLICT(brick_number) DO UPDATE SET qty=qty+{qty};"

        self.stat.execute(add)
        self.conn.commit()
        return

    def add_shelf(self, shelfNum):
        add = f"INSERT INTO Inventory (shelf_number) VALUES ({shelfNum});"
        self.stat.execute(add)
        self.conn.commit()
        return

    def assign_brick(self, shelfNum, brickNum):
        select_bi = f"SELECT id_brick FROM Bricks WHERE brick_number={brickNum};"
        select_si = f"SELECT id_shelf FROM Inventory WHERE shelf_number={shelfNum};"
        brId = self.stat.execute(select_bi).fetchall()[0][0]
        shId = self.stat.execute(select_si).fetchall()[0][0]
        assign = f"INSERT INTO Assignments (id_brick, id_shelf) VALUES ({brId}, {shId});"
        self.stat.execute(assign)
        self.conn.commit()
        return

    def remove_brick(self, brick, qty=-1):

        if qty == -1:
            delete_bn = f"UPDATE Bricks SET qty=0 WHERE brick_number={brick};"
        else:
            delete_bn = f"UPDATE Bricks SET qty=qty-{qty} WHERE brick_number={brick} AND qty-{qty} >= 0;"

        self.stat.execute(delete_bn)
        self.conn.commit()
        return

    def find_brick(self, brick):
        select = f"SELECT qty, shelf_number FROM Bricks " \
                 f"INNER JOIN Assignments A on Bricks.id_brick = A.id_brick " \
                 f"INNER JOIN Inventory I on I.id_shelf = A.id_shelf " \
                 f"WHERE brick_number = {brick};"

        self.stat.execute(select)
        brickData = self.stat.fetchone()
        self.stat.close()
        self.stat = self.conn.cursor()
        return brickData


if __name__ == "__main__":
    db = bricksDB()
    db.create_db()
    db.add_brick(100, 1111)
    db.add_brick(200, 2222)
    db.add_brick(100, 1111)
    db.add_shelf(12)
    db.add_shelf(13)
    db.assign_brick(12, 1111)
    print(db.find_brick(1111))
    db.add_shelf(14)
    db.conn.close()
