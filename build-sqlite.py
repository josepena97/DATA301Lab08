import sqlite3
import os

conn = sqlite3.connect("tpch.db")

cursor = conn.cursor()

for filename in os.listdir("./db-data"):
    filepath = os.path.join("./db-data", filename)
    if os.path.isdir(filepath):
        continue
    with open(filepath, "r") as f:
        commands = f.read()
        for command in commands.split(";"):
            cursor.execute(command)
            conn.commit()
            
cursor.execute("VACUUM;")
conn.commit()
conn.close()