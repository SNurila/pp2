import psycopg2
from config import load_config

def delete_contact(identifier, by='name'):
    config = load_config('/Users/nurilasalamat/Desktop/pp2/lab10/phone book/database.ini')
    
    if by == 'name':
        query = '''DELETE FROM contacts WHERE first_name = %s'''
    elif by == 'phone':
        query = '''DELETE FROM phone_numbers WHERE phone_number = %s'''
    else:
        print("Invalid delete option. Use 'name' or 'phone'.")
        return
    
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(query, (identifier,))

            conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
if __name__ == '__main__':
    delete_contact("John", by='name')      
    delete_contact("123-456-7890", by='phone')