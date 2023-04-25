import sqlite3
from tabulate import tabulate
import sys

class TodoList:
    global conn, cursor, counter, table_clear
    try: 
        conn = sqlite3.connect('todo_list_database.db')
        print("[+] Sucesfuly connect to db")
        cursor = conn.cursor()
    except Exception as err:
        print(f"[!] {err}")


    def create_db(self):
        try: 
            cursor.execute("CREATE TABLE todo_data_list_database (id INTEGER PRIMARY KEY, describe TEXT NOT NULL, status TEXT NOT NULL);")
            conn.commit()
            print("[!] DB created")
        except:
            print('[!] DB already exist')    

    def insert_data(self):
        describe = input("[*] Describe > ")
        status = input('[*] Status > ')
        values = [describe, status]

        print("[ALERT] Check input data: ")
        print(f'describe: {describe}')
        print(f'status: {status}')
        access = input("Do u agree? Y/N: ")
        if access == 'Y':
            try: 
                cursor.execute('INSERT INTO todo_data_list_database (describe, status) VALUES (?, ?);', values)
                conn.commit()
                print("[+] Succesfuly added data to db")
                table_clear = False
                self.show_table(self)
            except Exception as err:
                print(f"[!!!] Error: {err}")
        else:
            print("[!] Operation cancled")

    def show_table(self):
        res = cursor.execute("SELECT * FROM todo_data_list_database")
         
        print(tabulate(res, tablefmt='fancy_grid'))
        
    
    def clear_db(self):
        cursor.execute("DELETE FROM todo_data_list_database;")
        conn.commit()

    def delete_id(self):
        id = input("Enter id of element to delete: ")
        conn.execute(f"DELETE FROM todo_data_list_database WHERE id = {id}")
        conn.commit()

    def help(self):
        flags = [['--a', 'add task in table'], ['--d', 'delete row in table'], 
                ['--c', 'clear table'], ['--s', 'show table'], ]
        print(tabulate(flags, tablefmt='fancy_grid'))




if __name__ == "__main__":
    todo = TodoList()
    print(sys.argv[1])
    if sys.argv[1] == '--a':
        todo.insert_data()
    if sys.argv[1] == '--c':
        todo.clear_db()
    if sys.argv[1] == '--s':
        todo.show_table()
    if sys.argv[1] == '--h':
        todo.help()
    if sys.argv[1] == '--r':
        todo.delete_id()
    print("[!] Type 'python main.py --h' to get help")
