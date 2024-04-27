import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password= "1234"
)
cur = conn.cursor()

# Function to search PhoneBook based on pattern
def search_phone_book(pattern):
    cur.execute("""
        SELECT * FROM PhoneBook
        WHERE name LIKE %s OR surname LIKE %s OR phone LIKE %s
    """, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
    return cur.fetchall()

# Procedure to insert/update user by name and phone
def insert_or_update_user(name, phone):
    cur.execute("""
        SELECT EXISTS(SELECT 1 FROM PhoneBook WHERE name = %s)
    """, (name,))
    exists = cur.fetchone()[0]
    if exists:
        cur.execute("""
            UPDATE PhoneBook SET phone = %s WHERE name = %s
        """, (phone, name))
    else:
        cur.execute("""
            INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)
        """, (name, phone))
    conn.commit()

# Procedure to insert many new users by list of name and phone
def insert_users(name_list, phone_list):
    for name, phone in zip(name_list, phone_list):
        if len(phone) != 10:
            print(f"Phone number {phone} is incorrect.")
        else:
            cur.execute("""
                INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)
            """, (name, phone))
    conn.commit()

# Function to query data from the tables with pagination
def get_phone_book_page(limit_val, offset_val):
    cur.execute("""
        SELECT * FROM PhoneBook
        ORDER BY id
        LIMIT %s OFFSET %s
    """, (limit_val, offset_val))
    return cur.fetchall()

# Procedure to delete data from tables by username or phone
def delete_from_phone_book(identifier):
    cur.execute("""
        DELETE FROM PhoneBook WHERE name = %s OR phone = %s
    """, (identifier, identifier))
    conn.commit()

# Close the cursor and connection when done
cur.close()
conn.close()
