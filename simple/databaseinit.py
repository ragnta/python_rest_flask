import sqlite3
from sqlite3 import Error
from app import MadDao
from app import Reader
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_Medicine(conn, medicine):
    """
        Create medicine:
        :conn - database connection
        :medicine - medicine
    """
    sql = ''' INSERT INTO Medicine(id,barcode, shortBar, name, dosage, pieces  )
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, medicine)
    return cur.lastrowid

def create_Resident(conn, resident):
    """
        Create resident:
        :conn - database connection
        :resident - resident
    """
    sql = ''' INSERT INTO Resident(id, name, birthday)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, resident)
    return cur.lastrowid

def create_Dosage(conn, dosage):
    """
        Create dosage:
        :conn - database connection
        :dosage - dosage
    """
    sql = ''' INSERT INTO Dosage(dosage_id, interval, times)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, dosage)
    return cur.lastrowid


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_Resident_Medicine(conn, resident_medicine):
    """
        Create resident_medicine:
        :conn - database connection
        :resident_medicine - resident medicine relationship
    """
    sql = ''' INSERT INTO Resident_Medicine(resident_id, medicine_id, untilDate, dosage_id)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, resident_medicine)
    return cur.lastrowid

def main():
    conn = create_connection(r"./pythonsqlite.db")
        ##id,barcode, shortBar, name, dosage, pieces
    sql_create_medicine_table = """ CREATE TABLE IF NOT EXISTS Medicine (
                                        id text PRIMARY KEY,
                                        barcode text NOT NULL,
                                        shortBar text,
                                        name text,
                                        dosage text,
                                        pieces text
                                    ); """

    create_table(conn, sql_create_medicine_table)
    dao = MadDao(Reader())
    medicines = dao.getAllMadicines()
    ## TODO convert medicines to string object or something
    [create_Medicine(conn, x) for x in medicines]


if __name__ == '__main__':
    main()