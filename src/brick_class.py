import sqlite3 as sq

class bricksDB:

    def __init__(self):
        self.conn = sq.connect("../database/brick_database.db")
        self.stat = self.conn.cursor()

    def create_db(self):

        create_inventory = "CREATE TABLE IF NOT EXISTS Inventory (id_shelf INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE," \
                           " shelf_number int);"

        create_bricks = "CREATE TABLE IF NOT EXISTS Bricks (id_brick INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE," \
                        " brick_number int, qty int);"

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
        add = f"INSERT INTO Bricks (brick_number, qty) VALUES ({brickNum}, {qty});"
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
        select = f"SELECT Bricks.qty, Inventory.shelf_number " \
                 f"FROM Bricks " \
                 f"WHERE brick_number = {brick} " \
                 f"INNER JOIN Assignments ON Bricks.id_brick=Assignments.id_brick " \
                 f"INNER JOIN Inventory ON Assignments."
        self.stat.execute(select)
        brickData = self.stat.fetchall()


if __name__ == "__main__":
    db = bricksDB()
    db.create_db()
    db.add_brick(3, 1234)
    db.add_brick(4, 5678)
    db.add_shelf(100)
    db.add_shelf(200)
    db.assign_brick(200, 1234)
    db.remove_brick(1234, 100)
    db.remove_brick(5678)