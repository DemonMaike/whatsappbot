import psycopg2
import secret 
import datetime

# connect to our database
con = psycopg2.connect(
    database="dbr0eanbod0c9q",
    user="tvoflxtnevefnc",
    password=secret.password,
    host=secret.host,
    port="5432",
)

# print for complite connect
print("Database opened successfully")

# creating mimi-function for search in database on date today
def name(date_today):
    names = ''
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE to_char(date, 'YYYY-MM-DD') LIKE '%{date_today}' ")
    rows = cur.fetchall()
    for row in rows:
        names += row[2]
        names += ','
    return names 


print(name('04-24'))



