import psycopg2
from config import load_config

def delete_contact_by_username_or_phone(username=None, phone_number=None):
    config = load_config('/Users/nurilasalamat/Desktop/pp2/lab11/phone book/database.ini')

    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CALL delete_contact_by_username_or_phone(%s, %s)
            """, (username, phone_number))

            conn.commit()


if __name__ == '__main__':
    delete_contact_by_username_or_phone(username="Jane Smith")

    delete_contact_by_username_or_phone(phone_number="590-394-39")
