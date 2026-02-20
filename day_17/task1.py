import sqlite3

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend REAL
)
""")

intern_data = [
    (1, "Hanith", "Data Science", 15000),
    (2, "Aisha", "Web Dev", 12000),
    (3, "Rohan", "Cybersecurity", 14000),
    (4, "Meera", "Data Science", 16000),
    (5, "Arjun", "Web Dev", 13000)
]

cursor.executemany("INSERT OR REPLACE INTO interns VALUES (?, ?, ?, ?)", intern_data)

conn.commit()

cursor.execute("SELECT name, track FROM interns")
rows = cursor.fetchall()

print("Interns and Their Tracks:")
for row in rows:
    print("Name:", row[0], "| Track:", row[1])

conn.close()