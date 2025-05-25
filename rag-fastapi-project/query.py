import sqlite3

conn = sqlite3.connect('rag_app.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM document_store")
print(cursor.fetchone())
# Output: (0,)
results = cursor.fetchall()

for row in results:
    print(row)
conn.close()