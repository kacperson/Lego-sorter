import sqlite3 as sq

conn = sq.connect("../database/brick_database.db")
stat = conn.cursor()


def create_db():
    create_inventory = "CREATE TABLE IF NOT EXISTS Inventory (id_shelf int NOT NULL PRIMARY KEY," \
                       " shelf_number int);"
    create_bricks = "CREATE TABLE IF NOT EXISTS Bricks (id_brick int NOT NULL PRIMARY KEY," \
                    " brick_number int );"
    create_assignments = "CREATE TABLE IF NOT EXISTS Assignments (id_assignment int NOT NULL PRIMARY KEY," \
                         " id_brick int," \
                         " id_shelf int," \
                         " FOREIGN KEY (id_brick) REFERENCES Bricks (id_brick)," \
                         " FOREIGN KEY (id_shelf) REFERENCES Inventory (id_shelf));"
    create_images = "CREATE TABLE IF NOT EXISTS Images (id_image int NOT NULL PRIMARY KEY," \
                    " id_brick int ," \
                    " img_path string," \
                    " FOREIGN KEY (id_brick) REFERENCES Bricks(id_brick));"

    stat.execute(create_inventory)
    stat.execute(create_bricks)
    stat.execute(create_assignments)
    stat.execute(create_images)


def update(id_brick, id_shelf, number_of_bricks):
    pass
