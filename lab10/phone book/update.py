import psycopg2
from config import load_config

def update(contact_id, first_name, phone_number):
    
    sql_con = """UPDATE contacts
            SET first_name = %s
            WHERE contact_id = %s"""
    sql_ph = '''UPDATE phone_numbers
                SET phone_number = %s
                WHERE contact_id = %s'''
    config = load_config('/Users/nurilasalamat/Desktop/pp2/lab10/phone book/database.ini')
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:

                cur.execute(sql_con, (first_name, contact_id))

                cur.execute(sql_ph, (phone_number, contact_id))
            conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    update(1, 'George', '590-394-39')