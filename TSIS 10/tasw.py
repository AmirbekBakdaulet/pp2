import psycopg2

def user_insert(user,score):
    max=score

    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password= "1234"
    )
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS scores(
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(20),
        score INT
        ) """)
        
        cursor.execute(f"SELECT * FROM scores WHERE user_name='{user}'")
        for users_history in cursor.fetchall():
            if users_history[2]>max:
                max=users_history[2]

        cursor.execute(f"""UPDATE scores SET score={score} WHERE user_name='{user}'""")
        connection.commit()
    return max
    
def find_user(user):
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password= "1234"
    )
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS scores(
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(20),
        score INT
        ) """)
        cursor.execute(f"SELECT score FROM scores WHERE user_name='{user}'")
        if len(cursor.fetchall())!=0:
            cursor.execute(f"SELECT score FROM scores WHERE user_name='{user}'")
            connection.commit()
            return cursor.fetchall()[0][0]

        else:
            cursor.execute(f"""INSERT INTO scores (user_name,score)
            VALUES ('{user}',0)""")
            connection.commit()
            return 0