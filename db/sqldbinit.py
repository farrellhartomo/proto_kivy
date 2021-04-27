import sqlite3

conn = sqlite3.connect(':memory:')

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
            city_desc TEXT
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
    
class fill_tables:
    #fill tuples to user tables
    conn.execute("""INSERT INTO userdb(user_id,first_name,last_name) 
    VALUES
        (142342, 'John','Doe'),
        (192387, 'Mark','Ronson')
        """)
    #fill tuples to city tables
    conn.execute("""INSERT INTO citydb(city_name,city_desc)
        VALUES
            ("Stockholm","Visit Stockholm is your guide to Stockholm and the Stockholm Archipelago. Get tips on restaurants, cafés, bars, shops, events, exhibitions, and activities."),
            ("Munich", "Munich tourism: Get all the information on places to visit, what to see and things to do in Munich, here on the city's official website!")
        """)
    #fill tuples to trip tables
    # conn.execute("""INSERT INTO userdb(
        
    #     """)
    

create_tables
conn.commit()
conn.close()   
    




