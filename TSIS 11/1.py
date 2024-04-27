import psycopg2
import csv
def main():
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password= "1234"
    )
    on=True
    mode='ASC'
    connection.autocommit = True
    all_contacts2=[]

    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS phonebook(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(20) NOT NULL,
        phone_number VARCHAR(20) NOT NULL
        ) """)
    while on:
        a=int(input("type:\n 1-add,\n2-delete,\n3-edit,\n4-look,\n6-resort,\n7-import from scv\n8-find by pattern\n:"))
        if a == 1:
            name_to_insert=input("enter name: ")
            number_to_insert=input("enter phone number: ")
            with connection.cursor() as cursor:
                cursor.execute(f"""INSERT INTO phonebook(first_name,phone_number)
                VALUES ('{name_to_insert}','{number_to_insert}')""")
                
        elif a == 4:
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM phonebook ORDER BY first_name ASC""")
                all=cursor.fetchall()
                for _,name,phone in all:
                    print("|"+name+"---"+phone+"|")
        elif a == 2:
            name_to_delete=input("delete: ")
            with connection.cursor() as cursor:
                cursor.execute(f"CALL delete_contact('{name_to_delete}')")
        elif a == 3:
            editing_name=input("what contact you will edit?: ")
            new_name=input("new name: ")
            new_number=input("new phone number: ")
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE phonebook SET phone_number='{new_number}' WHERE first_name='{editing_name}'")
        elif a ==6:
            mode_change=input("1-by askending,2-by deskending")
            pagination_offset=int(input("how many first ones you need to ignore(offset,integer)"))
            pagination_limit=int(input("how many result do you want to see(limit,ineger)"))

            if mode_change==1:
                mode='ASC'
                with connection.cursor() as cursor:
                    cursor.execute(f"""SELECT * from get_sorting_asc('DESK',{pagination_limit},{pagination_offset})""")
                    all=cursor.fetchall()
                    for name,phone in all:
                        print("|"+name+"---"+phone+"|")
            else:
                mode='DESC'
                with connection.cursor() as cursor:
                    cursor.execute(f"""SELECT * from get_sorting_desc('DESK',{pagination_limit},{pagination_offset})""")
                    all=cursor.fetchall()
                    for name,phone in all:
                        print("|"+name+"---"+phone+"|")

            
        elif a == 7:
            path=input("give path,NOT RELATIVE")

            with open(path, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';', quotechar='|',)
                for row in spamreader:
                     with connection.cursor() as cursor:
                        cursor.execute(f"""INSERT INTO phonebook(first_name,phone_number)
                        VALUES ('{row[0]}','{row[1]}')""")
        elif a == 8:
            patt=input("what pattern are you looking for:")
            with connection.cursor() as cursor:
                cursor.execute("SELECT find(%s)",[patt] )
                result = cursor.fetchall()
                print(result)
    connection.close()

if __name__ == "__main__":
    main()