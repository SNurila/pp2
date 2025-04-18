import psycopg2
from config import load_config

def search_contacts(pattern):
    config = load_config('/Users/nurilasalamat/Desktop/pp2/lab11/phone book/database.ini')
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT c.contact_id, c.first_name, c.last_name, p.phone_number
                FROM contacts c
                JOIN phone_numbers p ON c.contact_id = p.contact_id
                WHERE c.first_name ILIKE %s
                   OR c.last_name ILIKE %s
                   OR p.phone_number ILIKE %s
            """, (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
            results = cur.fetchall()
            return results

if __name__ == '__main__':
    pattern = input("Enter search pattern (first_name, last_name, or phone): ")
    matches = search_contacts(pattern)
    
    for match in matches:
        print(match)