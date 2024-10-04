
import psycopg2

conn = psycopg2.connect(database="Livevox", user="postgres", host="localhost",
                        password="admin", port=5432)

cur = conn.cursor()

query = "update players set playername = 'Pusarla Venkata Sindhu' where playerid = 'PLY501'"

cur.execute(query)

conn.commit()
cur.close()
conn.close()

