import csv
import psycopg2
from config import load_config

def insert_csv():
    try:
        config = load_config('/Users/nurilasalamat/Desktop/pp2/lab10/phone book/database.ini')
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open('/Users/nurilasalamat/Desktop/pp2/lab10/phone book/contacts_data.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        cur.execute("""
                                    INSERT INTO contacts(first_name, last_name, email)
                                    VALUES (%s, %s, %s) RETURNING contact_id
                                    """, (row['first_name'], row['last_name'], row['email'])
                                    )
                        contact_id = cur.fetchone()[0]

                        cur.execute("""
                                    INSERT INTO phone_numbers(contact_id, phone_number, type)
                                    VALUES(%s, %s, %s)""",
                                    (contact_id, row['phone_number'], row['type']))
                    conn.commit()

                                    
    except Exception as error:
        print(error)

if __name__ == '__main__':
    insert_csv()