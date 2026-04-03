import psycopg2 
import csv
from functions import functions
from procedures import procedures
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD


conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

def create_table_if_not_exists() :
    req = """
            CREATE TABLE IF NOT EXISTS contacts (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                phone VARCHAR(63)
            )
          """
    with conn.cursor() as cursor:
        cursor.execute(req)
        conn.commit()


def create_all_functions_and_procedures() :
    try:
        with conn.cursor() as cursor:
            for i in functions + procedures:
                cursor.execute(i)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def print_contacts(contacts: list[tuple]) :
    print()
    if not contacts:
        print("(no contacts)")
        return
    
    for c in contacts:
        print(f"[{c[0]}]. {c[1]} - {c[2]}")


def get_all_contacts() -> list[tuple]:
    req = """
            SELECT * FROM contacts
          """
    with conn.cursor() as cursor:
        cursor.execute(req)
        data = cursor.fetchall()

    return data


def call_function(name: str, *args: tuple[object]) :
    with conn.cursor() as cursor:
        cursor.callproc(name, args)
        data = cursor.fetchall()

    return data


def call_procedure(name: str, *args: tuple[object]) :
    command = f"CALL {name}(" + ("%s, " * len(args)).strip(", ") + ")"
    try:
        with conn.cursor() as cursor:
            cursor.execute(command, args)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def find_contacts(pattern: str) -> list[tuple]:
    return call_function("find_by_pattern", pattern)


def add_from_terminal() :
    name = input("New name: ")
    phone = input("New phone: ")
    call_procedure("add_or_update", name, phone)


def insert_from_csv(path: str) :
    names = []
    phones = []
    with open(path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            name, phone = row
            names.append(name)
            phones.append(phone)
    call_procedure("mass_insert", names, phones)


def get_contacts_with_pagination(limit: int, offset: int) :
    return call_function("select_with_pagination", limit, offset)


def delete_contact(pattern: str) :
    call_procedure("delete_contact", pattern)
    

def main() :
    create_table_if_not_exists()
    create_all_functions_and_procedures()

    while True:

        print()
        print("--- PhoneBook ---")
        print("1(s). Show all contacts")
        print("2(p). Show contacts with pagination")
        print("3(a). Add or update contact (from terminal)")
        print("4(c). Add or update from CSV")
        print("5(f). Find by name or phone")
        print("6(d). Delete contact")
        print("0(q). Exit")


        choice = input("\nChoice: ")

        if choice == "1" or choice == "s":
            print_contacts(get_all_contacts())
        elif choice == "2" or choice == "p":
            limit = int(input("Amount of contacts: "))
            limit = limit if limit else 0
            offset = int(input("Offset: "))
            offset = offset if offset else 0
            print_contacts(get_contacts_with_pagination(limit=limit, offset=offset))
        elif choice == "3" or choice == "a":
            add_from_terminal()
        elif choice == "4" or choice == "c":
            filename = input("CSV file path: ")
            insert_from_csv(filename)
        elif choice == "5" or choice == "f":
            pattern = input("Find: ")
            print_contacts(find_contacts(pattern))
        elif choice == "6" or choice == "d":
            pattern = input("Name or phone: ")
            delete_contact(pattern)
        elif choice == "0" or choice == "q":
            break
        else:
            print("Please choose valid option")

    conn.close()

if __name__ == "__main__":
    main()
