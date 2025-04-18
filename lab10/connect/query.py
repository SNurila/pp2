import psycopg2
from config import load_config


def get_vendors():
        config = load_config('/Users/nurilasalamat/Desktop/pp2/lab10/connect/database.ini')
        try:
            with psycopg2.connect(**config) as conn:
                with conn.cursor() as cur:
                    cur.execute('SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name')
                    print('The number of parts:', cur.rowcount)
                    row = cur.fetchone()

                    while row is not None:
                        print(row)
                        row = cur.fetchone()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)


def getVendors():
    config = load_config('/Users/nurilasalamat/Desktop/pp2/lab10/connect/database.ini')
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name')
                rows = cur.fetchall()
                
                for r in rows:    
                    print(r)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)



if __name__ == '__main__':
    get_vendors()
    print('##########')
    getVendors()