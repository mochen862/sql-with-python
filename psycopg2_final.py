import psycopg2
import configparser
import pandas as pd
from sql_queries import *

def create_database():
    '''
    - Creates and connects to coffeeshops database
    - Returns the connection and the cursor to coffeeshops database
    '''
    # Read the parameters from the config file
    config = configparser.ConfigParser()
    config.read('private.cfg')
    DB_NAME_DEFAULT = config.get('SQL', 'DB_NAME_DEFAULT')
    DB_USER = config.get('SQL', 'DB_USER')
    DB_PASSWORD = config.get('SQL', 'DB_PASSWORD')
    
    # Connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname={} user={} password={}".format(DB_NAME_DEFAULT, DB_USER, DB_PASSWORD))
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # Create coffeeshops database
    cur.execute('DROP DATABASE IF EXISTS coffeeshops')
    cur.execute("CREATE DATABASE coffeeshops WITH ENCODING 'utf8' TEMPLATE template0")
    
    # Close connection to default database
    conn.close()
    
    # Connect to coffeeshops database
    conn = psycopg2.connect('host=127.0.0.1 dbname=coffeeshops user={} password={}'.format(DB_USER, DB_PASSWORD))
    cur = conn.cursor()
    
    return cur, conn

def drop_table(cur, conn):
    '''
    - Drops the employees table
    '''
    cur.execute(drop_employees_table)
    conn.commit()

def create_table(cur, conn):
    '''
    - Create the employee table
    '''
    cur.execute(create_employees_table)
    conn.commit()
    
def insert_table(cur, conn):
    '''
    - Insert the values from the coffeeshop.csv file into the employees table
    '''
    df = pd.read_csv('coffeeshop.csv')
    for i, row in df.iterrows():
        cur.execute(insert_employees_table, row.tolist())
        conn.commit()
        
def main():
    '''
    - Drops (if exists) and creates the coffeeshops database
    - Establishes connection and gets cursor to it
    - Drops the employees table if it already exists
    - Creates the employees table
    - Insert the coffeeshop.csv values into the employees table
    - Closes the connection to the database
    '''
    cur, conn = create_database()
    
    drop_table(cur, conn)
    create_table(cur, conn)
    insert_table(cur, conn)
    
    conn.close()
    
if __name__ == '__main__':
    '''
    - To only run the code inside the if statement when the program is run directly by the Python interpreter
    - The code inside the if statement is not executed when the file's code is imported as a module.
    - 
    '''
    main()
    
    
    
    