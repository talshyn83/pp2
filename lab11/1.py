import psycopg2
import csv
from tabulate import tabulate

conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres",
                        password="bnqvvs_07", port=5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
      user_id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      surname VARCHAR(255) NOT NULL, 
      phone VARCHAR(255) NOT NULL
)""")

def insert_or_update_user(name, surname, phone):
    cur.execute("SELECT * FROM phonebook WHERE name = %s AND surname = %s", (name, surname))
    existing = cur.fetchone()
    if existing:
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s AND surname = %s", (phone, name, surname))
    else:
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
    conn.commit()

def bulk_insert_users_from_csv(filepath):
    incorrect_data = []
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            name, surname, phone = row[0], row[1], row[2]
            if phone.isdigit() and len(phone) >= 5:
                insert_or_update_user(name, surname, phone)
            else:
                incorrect_data.append(row)
    return incorrect_data

def get_paginated(limit, offset):
    cur.execute("SELECT * FROM phonebook ORDER BY user_id LIMIT %s OFFSET %s", (limit, offset))
    return cur.fetchall()

check = True
command = ''
temp = ''

name_var = ''
surname_var = ''
phone_var = ''
id_var = ''

start = True
back = False

back_com = ''
name_upd = ''
surname_upd = ''
phone_upd = ''

filepath = ''

while check:
    if start or back:
        start = False
        print("""
        List of the commands:
        1. Type "i" to INSERT data.
        2. Type "u" to UPDATE data.
        3. Type "q" to QUERY data.
        4. Type "d" to DELETE data.
        5. Type "f" to FINISH the program.
        6. Type "s" to SEE all data.
        7. Type "p" for PAGINATION view.
        """)
        command = input()

        if command.lower() == "i":
            print('Type "csv" or "con" to choose option between uploading csv file or typing from console: ')
            command = ''
            temp = input()
            if temp == "con":
                name_var = input("Name: ")
                surname_var = input("Surname: ")
                phone_var = input("Phone: ")
                insert_or_update_user(name_var, surname_var, phone_var)
                back_com = input('Type "back" to return: ')
                if back_com == "back":
                    back = True
            if temp == "csv":
                filepath = input("Enter a file path: ")
                incorrect = bulk_insert_users_from_csv(filepath)
                if incorrect:
                    print("Incorrect data:")
                    for i in incorrect:
                        print(i)
                back_com = input('Type "back" to return: ')
                if back_com == "back":
                    back = True

        if command.lower() == "d":
            back = False
            command = ''
            temp = input("Delete by (name/phone): ")
            if temp == "name":
                name_var = input("Enter name: ")
                cur.execute("DELETE FROM phonebook WHERE name = %s", (name_var,))
            elif temp == "phone":
                phone_var = input("Enter phone: ")
                cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone_var,))
            conn.commit()
            back_com = input('Type "back" to return: ')
            if back_com == "back":
                back = True

        if command.lower() == 'u':
            back = False
            command = ''
            temp = input('Type the name of the column that you want to change: ')
            if temp == "name":
                name_var = input("Enter name that you want to change: ")
                name_upd = input("Enter the new name: ")
                cur.execute("UPDATE phonebook SET name = %s WHERE name = %s", (name_upd, name_var))
                conn.commit()
            if temp == "surname":
                surname_var = input("Enter surname that you want to change: ")
                surname_upd = input("Enter the new surname: ")
                cur.execute("UPDATE phonebook SET surname = %s WHERE surname = %s", (surname_upd, surname_var))
                conn.commit()
            if temp == "phone":
                phone_var = input("Enter phone number that you want to change: ")
                phone_upd = input("Enter the new phone number: ")
                cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (phone_upd, phone_var))
                conn.commit()
            back_com = input('Type "back" to return: ')
            if back_com == "back":
                back = True

        if command.lower() == "q":
            back = False
            command = ''
            temp = input("Search by (id/name/surname/phone): ")
            if temp == "id":
                id_var = input("Enter ID: ")
                cur.execute("SELECT * FROM phonebook WHERE user_id = %s", (id_var,))
            if temp == "name":
                name_var = input("Enter part of name: ")
                cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", ('%' + name_var + '%',))
            if temp == "surname":
                surname_var = input("Enter part of surname: ")
                cur.execute("SELECT * FROM phonebook WHERE surname ILIKE %s", ('%' + surname_var + '%',))
            if temp == "phone":
                phone_var = input("Enter part of phone: ")
                cur.execute("SELECT * FROM phonebook WHERE phone ILIKE %s", ('%' + phone_var + '%',))
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))
            back_com = input('Type "back" to return: ')
            if back_com == "back":
                back = True

        if command.lower() == "s":
            back = False
            command = ''
            cur.execute("SELECT * from phonebook;")
            rows = cur.fetchall()
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
            back_com = input('Type "back" to return: ')
            if back_com == "back":
                back = True

        if command.lower() == "p":
            limit = int(input("Enter limit: "))
            offset = int(input("Enter offset: "))
            rows = get_paginated(limit, offset)
            print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))
            back_com = input('Type "back" to return: ')
            if back_com == "back":
                back = True

        if command.lower() == "f":
            command = ''
            check = False

conn.commit()
cur.close()
conn.close()