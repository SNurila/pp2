import psycopg2
import re
from config import load_config
def is_valid_phone(phone):
    return re.match(r'^\d{3,4}-\d{3}-\d{4}$', phone) is not None

def insert_many_users(users):
    config = load_config('/Users/nurilasalamat/Desktop/pp2/lab11/phone book/database.ini')
    invalid_entries = []

    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            for user in users:
                first_name = user['first_name']
                last_name = user['last_name']
                email = user['email']
                phone_number = user['phone_number']
                phone_type = user['type']

                if not is_valid_phone(phone_number):
                    invalid_entries.append(user)
                    continue  

    
                cur.execute("""
                    SELECT contact_id FROM contacts
                    WHERE first_name = %s AND last_name = %s
                """, (first_name, last_name))
                result = cur.fetchone()

                if result:
                    contact_id = result[0]
        
                    cur.execute("""
                        UPDATE phone_numbers
                        SET phone_number = %s, type = %s
                        WHERE contact_id = %s
                    """, (phone_number, phone_type, contact_id))
                else:
                    
                    cur.execute("""
                        INSERT INTO contacts (first_name, last_name, email)
                        VALUES (%s, %s, %s)
                        RETURNING contact_id
                    """, (first_name, last_name, email))
                    contact_id = cur.fetchone()[0]
                    cur.execute("""
                        INSERT INTO phone_numbers (contact_id, phone_number, type)
                        VALUES (%s, %s, %s)
                    """, (contact_id, phone_number, phone_type))

    return invalid_entries
if __name__ == '__main__':
    new_users = [
        {"first_name": "Alice", "last_name": "Wonderland", "email": "alice@example.com", "phone_number": "123-456-7890", "type": "mobile"},
        {"first_name": "Bob", "last_name": "Builder", "email": "bob@example.com", "phone_number": "1111-222-3333", "type": "home"},
        {"first_name": "Charlie", "last_name": "Chaplin", "email": "charlie@example.com", "phone_number": "wrong-phone", "type": "mobile"},
    ]

    invalid = insert_many_users(new_users)
    print("Invalid entries:")
    for entry in invalid:
        print(entry)
