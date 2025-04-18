import psycopg2
from config import load_config

def search_by_first_name(name):
    config = load_config('/Users/nurilasalamat/Desktop/pp2/lab10/phone book/database.ini')
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.first_name, c.last_name, c.email, p.phone_number, p.type
                FROM contacts c
                JOIN phone_numbers p ON c.contact_id = p.contact_id
                WHERE c.first_name ILIKE %s
            """, (f'%{name}%',))
            rows = cur.fetchall()
            for row in rows:
                print(row)
def search_by_phone_number(number):
    config = load_config('/Users/nurilasalamat/Desktop/pp2/lab10/phone book/database.ini')
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.first_name, c.last_name, c.email, p.phone_number, p.type
                FROM contacts c
                JOIN phone_numbers p ON c.contact_id = p.contact_id
                WHERE p.phone_number = %s
            """, (number,))
            rows = cur.fetchall()
            for row in rows:
                print(row)
def search_by_phone_type(phone_type):
    config = load_config('/Users/nurilasalamat/Desktop/pp2/lab10/phone book/database.ini')
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.first_name, c.last_name, c.email, p.phone_number, p.type
                FROM contacts c
                JOIN phone_numbers p ON c.contact_id = p.contact_id
                WHERE p.type = %s
            """, (phone_type,))
            rows = cur.fetchall()
            for row in rows:
                print(row)

if __name__ == '__main__':
    search_by_first_name('Nurila')
    search_by_phone_number('234-567-8901')
    search_by_phone_type('home')