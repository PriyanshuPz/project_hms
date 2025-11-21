from sys import exit
import mysql.connector as sql
import os


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def authenticate_user():
    u1 = input("Enter username: ")
    pwd1 = input("Enter password: ")

    if u1 == "admin" and pwd1 == "password":
        return True
    else:
        print("Wrong username & password!")
        input("Press Enter to try again...")
        clear_terminal()
        display_welcome()
        return False


def display_welcome():
    WELCOME_MESSAGE = """
----------------------------------------------
HOSPITAL MANAGEMENT SYSTEM
BY Priyanshu Verma
GITHUB: @PriyanshuPz
----------------------------------------------
"""
    print(WELCOME_MESSAGE)


def patient_menu(conn, cursor):
    while True:
        clear_terminal()
        display_welcome()
        print("=== PATIENT MANAGEMENT ===")
        print("1. Register New Patient")
        print("2. View All Patients")
        print("3. Search Patient by Name")
        print("4. Back to Main Menu")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            p_name = input("Enter Patient Name: ")
            p_age = int(input("Enter Age: "))
            p_problems = input("Enter the Problem/Disease: ")
            p_phono = int(input("Enter Phone number: "))
            sql_insert = "INSERT INTO patient_details VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_insert, (p_name, p_age, p_problems, p_phono))
            print("PATIENT SUCCESSFULLY REGISTERED")
            conn.commit()
            input("Press Enter to continue...")

        elif choice == 2:
            sql_w = "SELECT * FROM patient_details"
            cursor.execute(sql_w)
            r = cursor.fetchall()
            print("\n--- ALL PATIENT DETAILS ---")
            if r:
                for i in r:
                    print(f"Name: {i[0]}, Age: {i[1]}, Problem: {i[2]}, Phone: {i[3]}")
            else:
                print("No patients found.")
            input("Press Enter to continue...")

        elif choice == 3:
            h = input("Enter the patient name (partial name allowed): ")
            sql_w = "SELECT * FROM patient_details WHERE p_name LIKE %s"
            cursor.execute(sql_w, (f"%{h}%",))
            u = cursor.fetchall()
            print(f"\n--- SEARCH RESULTS FOR '{h}' ---")
            if u:
                for i in u:
                    print(f"Name: {i[0]}, Age: {i[1]}, Problem: {i[2]}, Phone: {i[3]}")
            else:
                print("No patients found matching that name.")
            input("Press Enter to continue...")

        elif choice == 4:
            break


def doctor_menu(conn, cursor):
    while True:
        clear_terminal()
        display_welcome()
        print("=== DOCTOR MANAGEMENT ===")
        print("1. Register New Doctor")
        print("2. View All Doctors")
        print("3. Search Doctor by Name")
        print("4. Back to Main Menu")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            d_name = input("Enter Doctor Name: ")
            d_age = int(input("Enter Age: "))
            d_department = input("Enter the Department: ")
            d_phono = int(input("Enter Phone number: "))
            sql_insert = "INSERT INTO doctor_details VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_insert, (d_name, d_age, d_department, d_phono))
            print("DOCTOR SUCCESSFULLY REGISTERED")
            conn.commit()
            input("Press Enter to continue...")

        elif choice == 2:
            sql_x = "SELECT * FROM doctor_details"
            cursor.execute(sql_x)
            s = cursor.fetchall()
            print("\n--- ALL DOCTOR DETAILS ---")
            if s:
                for i in s:
                    print(
                        f"Name: {i[0]}, Age: {i[1]}, Department: {i[2]}, Phone: {i[3]}"
                    )
            else:
                print("No doctors found.")
            input("Press Enter to continue...")

        elif choice == 3:
            d = input("Enter the doctor name (partial name allowed): ")
            sql_d = "SELECT * FROM doctor_details WHERE d_name LIKE %s"
            cursor.execute(sql_d, (f"%{d}%",))
            v = cursor.fetchall()
            print(f"\n--- SEARCH RESULTS FOR '{d}' ---")
            if v:
                for i in v:
                    print(
                        f"Name: {i[0]}, Age: {i[1]}, Department: {i[2]}, Phone: {i[3]}"
                    )
            else:
                print("No doctors found matching that name.")
            input("Press Enter to continue...")

        elif choice == 4:
            break


def worker_menu(conn, cursor):
    while True:
        clear_terminal()
        display_welcome()
        print("=== WORKER MANAGEMENT ===")
        print("1. Register New Worker")
        print("2. View All Workers")
        print("3. Search Worker by Name")
        print("4. Back to Main Menu")

        choice = int(input("ENTER YOUR CHOICE: "))

        if choice == 1:
            w_name = input("Enter Worker Name: ")
            w_age = int(input("Enter Age: "))
            w_workname = input("Enter type of work: ")
            w_phono = int(input("Enter Phone number: "))
            sql_insert = "INSERT INTO worker_details VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_insert, (w_name, w_age, w_workname, w_phono))
            print("WORKER SUCCESSFULLY REGISTERED")
            conn.commit()
            input("Press Enter to continue...")

        elif choice == 2:
            sql_y = "SELECT * FROM worker_details"
            cursor.execute(sql_y)
            t = cursor.fetchall()
            print("\n--- ALL WORKER DETAILS ---")
            if t:
                for i in t:
                    print(
                        f"Name: {i[0]}, Age: {i[1]}, Work Type: {i[2]}, Phone: {i[3]}"
                    )
            else:
                print("No workers found.")
            input("Press Enter to continue...")

        elif choice == 3:
            f = input("Enter the worker name (partial name allowed): ")
            sql_f = "SELECT * FROM worker_details WHERE w_name LIKE %s"
            cursor.execute(sql_f, (f"%{f}%",))
            w = cursor.fetchall()
            print(f"\n--- SEARCH RESULTS FOR '{f}' ---")
            if w:
                for i in w:
                    print(
                        f"Name: {i[0]}, Age: {i[1]}, Work Type: {i[2]}, Phone: {i[3]}"
                    )
            else:
                print("No workers found matching that name.")
            input("Press Enter to continue...")

        elif choice == 4:
            break


def main():
    clear_terminal()
    display_welcome()

    print("Connecting to database")

    try:
        conn = sql.connect(
            host="localhost", user="root", passwd="password", database="hms_db"
        )
        if conn.is_connected():
            clear_terminal()
            display_welcome()
            print("✓ Successfully connected to database!\n")
        else:
            print("✗ Connection to database failed!")
            input("Press Enter to exit...")
            exit()
        c1 = conn.cursor()

        while True:
            print("1. LOGIN")
            print("2. EXIT")
            choice = int(input("ENTER YOUR CHOICE: "))

            if choice == 1:
                is_authenticated = authenticate_user()
                if is_authenticated:
                    while True:
                        clear_terminal()
                        display_welcome()
                        print("1. Patient Management")
                        print("2. Doctor Management")
                        print("3. Worker Management")
                        print("4. Exit")

                        choice = int(input("ENTER YOUR CHOICE: "))

                        if choice == 1:
                            patient_menu(conn, c1)
                        elif choice == 2:
                            doctor_menu(conn, c1)
                        elif choice == 3:
                            worker_menu(conn, c1)
                        elif choice == 4:
                            print("Thank you for using HMS!")
                            conn.close()
                            exit()
                else:
                    continue

            elif choice == 2:
                print("Thank you for using HMS!")
                conn.close()
                exit()

    except sql.Error as e:
        print(f"Database connection failed: {e}")
        input("Press Enter to exit...")
        exit()


if __name__ == "__main__":
    main()
