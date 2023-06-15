

import psycopg2 as pg


if __name__ == "__main__":

    con = pg.connect(
        host="localhost",
        database="demodb",
        user="demodb",
        password="demodb"
    )

    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS persons (name VARCHAR(100) PRIMARY KEY);
    """)
    cur.execute("INSERT INTO persons VALUES ('david');")

    cur.execute("SELECT * FROM persons;")

    res = cur.fetchall()

    for i in res:
        print(i)
