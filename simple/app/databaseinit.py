import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

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

if __name__ == '__main__':
    create_connection(r"./pythonsqlite.db")