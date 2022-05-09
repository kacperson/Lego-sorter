from src.brick_class import bricksDB
import os

db = bricksDB()
db.create_db()
i = 1
_, labels, _ = os.walk("../CNN/Data/test").__next__()
for label in labels:
    print(label)
    db.add_brick(0, label)
    db.add_shelf(i * 10)
    db.assign_brick(i * 10, label)
    i += 1
