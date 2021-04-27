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
            city_id INT PRIMARY KEY,
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
    
create_tables
conn.commit()
conn.close()   
    




