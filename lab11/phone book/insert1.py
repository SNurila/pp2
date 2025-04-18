import psycopg2
from config import load_config

def search_contacts(pattern):
    config = load_config('/Users/nurilasalamat/Desktop/pp2/lab11/phone book/database.ini')
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            query = """
                SELECT c.first_name, c.last_name, c.email, p.phone_number, p.type
                FROM contacts c
                JOIN phone_numbers p ON c.contact_id = p.contact_id
                WHERE c.first_name ILIKE %s
                   OR c.last_name ILIKE %s
                   OR c.email ILIKE %s
                   OR p.phone_number ILIKE %s;
            """
            cur.execute(query, (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
            results = cur.fetchall()
            return results

if __name__ == '__main__':
    matches = search_contacts('Nurila')
    for match in matches:
        print(match)
