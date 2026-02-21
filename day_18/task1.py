import sqlite3
import pandas as pd


conn = sqlite3.connect("internship.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
);
""")


cursor.execute("DELETE FROM interns")  # clear old data (optional)

intern_data = [
    ("Akash", "Data Science", 15000),
    ("Meena", "Web Dev", 12000),
    ("Rohan", "Cybersecurity", 14000),
    ("Priya", "Data Science", 16000),
    ("Kiran", "Web Dev", 13000)
]

cursor.executemany("INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)", intern_data)

# 4️⃣ Create mentors table
cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mentor_name TEXT NOT NULL,
    track TEXT NOT NULL
);
""")

# 5️⃣ Insert sample mentors
cursor.execute("DELETE FROM mentors")  # clear old data (optional)

mentor_data = [
    ("Ravi Kumar", "Data Science"),
    ("Sneha Reddy", "Web Dev"),
    ("Arjun Nair", "Cybersecurity")
]

cursor.executemany("INSERT INTO mentors (mentor_name, track) VALUES (?, ?)", mentor_data)

# 6️⃣ Commit changes
conn.commit()

# 7️⃣ INNER JOIN Query
query = """
SELECT interns.name AS intern_name,
       interns.track,
       interns.stipend,
       mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""

# 8️⃣ Load into Pandas DataFrame
df = pd.read_sql_query(query, conn)

# 9️⃣ Display result
print("Joined Internship Data:\n")
print(df)

# 🔟 Close connection
conn.close()