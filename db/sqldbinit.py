import sqlite3
from sqlite3 import Error

#set db default init
db = sqlite3.connect(':memory:')

conn = db.cursor()

def db_conn():
    try:
        con = sqlite3.connect(':memory:')
        return con
    except Error:
        print(Error)

class create_tables:
    #create user table (lookup)
    conn.execute("""CREATE TABLE userdb (
        user_id INT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
        )""")
    #create city table (lookup)
    conn.execute("""CREATE TABLE citydb
        (
            city_id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_name TEXT,
            city_desc TEXT,
            city_lon FLOAT,
            city_lat FLOAT
            CHECK (city_lon >= -180 AND city_lon < 181 AND city_lat >= -90 AND city_lat < 91)
            )""")

    #create user trip (transaction)
    conn.execute("""CREATE TABLE tripdb
        (
            fk_user_id INT NOT NULL,
            fk_city_id INT NOT NULL,
            fav_city TEXT,
            FOREIGN KEY (fk_user_id) REFERENCES userdb(user_id),
            FOREIGN KEY (fk_city_id) REFERENCES citydb(city_id)

        )""")

#get users data: return all
def get_city(con):
    city_table = {}
    curr = db.execute(" SELECT city_lon, city_lat FROM citydb")
    tabs = curr.fetchall()
    for rows in tabs:
        city_table = rows
    return city_table
    
class fill_tables_default:
    #fill tuples to user tables
    conn.execute("""INSERT INTO userdb(user_id,first_name,last_name) 
    VALUES
        (142342, 'John','Doe'),
        (192387, 'Mark','Ronson')
        """)
    #fill tuples to city tables
    conn.execute("""INSERT INTO citydb(city_name,city_desc,city_lon,city_lat)
        VALUES
            ("Stockholm","Visit Stockholm is your guide to Stockholm and the Stockholm Archipelago. Get tips on restaurants, cafés, bars, shops, events, exhibitions, and activities.",59.3293,18.0686),
            ("Munich", "Munich tourism: Get all the information on places to visit, what to see and things to do in Munich, here on the city's official website!",48.1351,11.5820)
        """)
    #fill tuples to trip tables
    # conn.execute("""INSERT INTO userdb(
        
    #     """)

    
create_tables
fill_tables_default
db.commit()
conn.close()   

print(get_city(db))
    




