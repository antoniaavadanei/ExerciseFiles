import mysql.connector as mysql
import sqlite3

MY_HOST = 'localhost'
MY_USER = 'root'
MY_PASS = 'anaaremere123'


def main():
    print("Challenge 1 : Read from mysql and insert into sqlite")
    db_mysql = None
    cur_mysql = None
    db_sqlite = None
    cur_sqlite = None

    # connecting to sqlite3
    try:
        db_sqlite = sqlite3.connect(":memory:")
        cur_sqlite = db_sqlite.cursor()
        print("connected to sqlite")

    except sqlite3.Error as e:
        print(f"could not open database: {e}")
        exit(1)

    # connecting to mysql
    try:
        db_mysql = mysql.connect(host=MY_HOST, user=MY_USER, password=MY_PASS, database='challenge_1')
        cur_mysql = db_mysql.cursor(prepared=True)
        print("connected to mysql")

    except mysql.Error as err:
        print(f"could not connect to MySQL: {err})")
        exit(1)
 
    # create mysql table
    try:
        cur_mysql.execute('DROP TABLE IF EXISTS person')
        create_table_stmt = '''CREATE TABLE person (
                                id SERIAL PRIMARY KEY,
                                name varchar(255) DEFAULT NULL,
                                age int(11)
                            )'''
        cur_mysql.execute(create_table_stmt)
        print("table created on mysql server")

    except mysql.Error as err:
        print(f"could not create mysql table, error: ({err})")
        exit(1)

    # crate sqlite table
    try:
        cur_sqlite.execute('DROP TABLE IF EXISTS person')
        create_table_stmt = '''CREATE TABLE person (
                                id SERIAL PRIMARY KEY,
                                name varchar(255) DEFAULT NULL,
                                age int(11)
                            )'''
        cur_sqlite.execute(create_table_stmt)
        print("table created on sqlite server")

    except mysql.Error as err:
        print(f"could not create sqlite table, error: ({err})")
        exit(1)

    # populate mysql table
    try:
        vals = ((1,'Antonia',23),
                (2,'Stefan',23),
                (3,'Georgian',29),
                (4,'Mihaela',30),
                (5,'Iris',20))
        cur_mysql.executemany("INSERT INTO person (id, name, age) VALUES (?, ?, ?)",vals)
        db_mysql.commit()

    except mysql.Error as err:
        print(f"populating mysql error ({err})")
        exit(1)

    # copying to sqlite
    try:
        print("copying to sqlite")
        cur_mysql.execute("SELECT * FROM person")
        for row in cur_mysql:
            cur_sqlite.execute("INSERT INTO person VALUES (?, ?, ?)",row)
            db_sqlite.commit()
        print("copy done")

    except mysql.Error as err:
        print(f"Error in copying({err})")
        exit(1)

    # Printing from sqlite
    try:
        print("Printing from sqlite")
        cur_sqlite.execute("SELECT * FROM person")
        for row in cur_sqlite:
            print(row)
        # close connection
        cur_mysql.close()
        db_mysql.close()
        cur_sqlite.close()
        db_sqlite.close()

    except mysql.Error as err:
        print(f"mysql error ({err})")
        exit(1)


if __name__ == "__main__":
    main()