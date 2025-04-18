
import psycopg2
from config import load_config

def create_tables():

    commands = (
        '''
        CREATE TABLE contacts(
        contact_id SERIAL PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255),
        email VARCHAR(255)
        )
        ''',
        '''
        CREATE TABLE phone_numbers (
        id SERIAL PRIMARY KEY,
        contact_id INTEGER,
        phone_number TEXT NOT NULL,
        type TEXT,  -- e.g., "mobile", "home", "work"
        FOREIGN KEY (contact_id) REFERENCES contacts(contact_id) ON DELETE CASCADE
        )       
        ''')
    
    try:
        config = load_config('/Users/nurilasalamat/Desktop/pp2/lab10/phone book/database.ini')
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for c in commands:
                    cur.execute(c)

    except(psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()



