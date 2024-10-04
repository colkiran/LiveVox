import psycopg2

conn = psycopg2.connect(database="Livevox", user="postgres", host="localhost",
                        password="admin", port=5432)

cur = conn.cursor()

query = """
create table players (
playerid varchar(7) PRIMARY KEY,
playername varchar(50) NOT NULL,
sport varchar(30) NOT NULL,
achievements varchar(50) NOT NULL
);
"""

cur.execute(query)
conn.commit()
cur.close()
conn.close()

