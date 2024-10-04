
import psycopg2

conn = psycopg2.connect(database="Livevox", user="postgres", host="localhost",
                        password="admin", port=5432)

cur = conn.cursor()

FL = open("players.txt", "r")

for line in FL.readlines():
    cur.execute(line)

conn.commit()
cur.close()
FL.close()
conn.close()