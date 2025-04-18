import psycopg2
from config import load_config

def get_or_create_user(username):
    config = load_config('/Users/nurilasalamat/Desktop/pp2/lab10/snake/database.ini')
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT user_id, current_level FROM user_info WHERE username = %s", (username,))
            result = cur.fetchone()

            if result:
                user_id, level = result
                print(f"Welcome back {username}! You're on level {level}.")
            else:
                cur.execute("INSERT INTO user_info (username) VALUES (%s) RETURNING user_id, current_level", (username,))
                user_id, level = cur.fetchone()
                print(f"New user {username} created. Starting from level {level}.")

            return user_id, level


if __name__ == "__main__":
    get_or_create_user('aisha')
