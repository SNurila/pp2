import psycopg2
from config import load_config

def create():

    commands = (
        '''
        CREATE TABLE user_info (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        current_level INT DEFAULT 1
        )
        ''',
        '''
        CREATE TABLE user_score (
        score_id SERIAL PRIMARY KEY,
        user_id INT REFERENCES user_info(user_id) ON DELETE CASCADE,
        score INT,
        level INT,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )       
        ''')
    
    try:
        config = load_config('/Users/nurilasalamat/Desktop/pp2/lab10/snake/database.ini')
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for c in commands:
                    cur.execute(c)

    except(psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create()

