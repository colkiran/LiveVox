import psycopg2
from prettytable import from_db_cursor

conn = psycopg2.connect(database="Livevox", user="postgres", host="localhost",
                        password="admin", port=5432)

cur = conn.cursor()

query = "select * from players;"

cur.execute(query)

prtyTbl = from_db_cursor(cur)

cur.close()
conn.close()

prtyTbl.align["playername"] = "l"
prtyTbl.align['sport'] = "r"

print(prtyTbl)
