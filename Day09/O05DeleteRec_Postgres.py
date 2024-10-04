
import psycopg2

conn = psycopg2.connect(database="Livevox", user="postgres", host="localhost",
                        password="admin", port=5432)

cur = conn.cursor()

query = "delete from players where playerid = 'PLY444'"

cur.execute(query)

conn.commit()
cur.close()
conn.close()

