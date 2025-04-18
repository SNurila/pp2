import psycopg2
from config import load_config

def insert_data_from_user():
    try:
        config = load_config('/Users/nurilasalamat/Desktop/pp2/lab10/phone book/database.ini')
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")

                cur.execute("""
                    INSERT INTO contacts (first_name, last_name, email) 
                    VALUES (%s, %s, %s) RETURNING contact_id
                """, (first_name, last_name, email))

                contact_id = cur.fetchone()[0]  

                print(f"Contact added with ID: {contact_id}")

                phone_number = input("Enter phone number: ")
                phone_type = input("Enter phone type (e.g., mobile, home): ")

                cur.execute("""
                    INSERT INTO phone_numbers (contact_id, phone_number, type) 
                    VALUES (%s, %s, %s)
                """, (contact_id, phone_number, phone_type))


                conn.commit()

    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    insert_data_from_user()
