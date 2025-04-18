import psycopg2
from config import load_config

def query_data_with_pagination(limit, offset):
    config = load_config('/Users/nurilasalamat/Desktop/pp2/lab11/phone book/database.ini')

    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:

            cur.execute("""
                SELECT contact_id, first_name, last_name, email
                FROM contacts
                LIMIT %s OFFSET %s
            """, (limit, offset))
            contacts = cur.fetchall()


            cur.execute("""
                SELECT phone_number, type
                FROM phone_numbers
                LIMIT %s OFFSET %s
            """, (limit, offset))
            phone_numbers = cur.fetchall()

    return contacts, phone_numbers


if __name__ == '__main__':
    limit = 2
    offset = 0
    contacts, phone_numbers = query_data_with_pagination(limit, offset)

    print("Contacts:", contacts)
    print("Phone Numbers:", phone_numbers)
