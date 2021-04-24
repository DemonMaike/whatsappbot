import psycopg2
import secret 
con = psycopg2.connect(
    database="dbr0eanbod0c9q",
    user="tvoflxtnevefnc",
    password=secret.password,
    host=secret.host,
    port="5432",
)

print("Database opened successfully")

