import tkinter as tk
import mysql.connector
def curr_b(fname,lname):
    db_connection = mysql.connector.connect(
        host="127.0.0.1",      # Replace with your host
        user="root",  # Replace with your username
         password="database password",  # Replace with your password
        database="first create database in sql workbench"  # Replace with your database name
    )
    cursor = db_connection.cursor()

    sql_query = "select money from Account_Money where fname=%s and lname = %s"
    cursor.execute(sql_query,(fname,lname))
    result = cursor.fetchone()
    cursor.close()
    db_connection.close()
    return result[0]
    
def show_bal(fname,lname):
    window = tk.Tk()
    window.title("Welcome To The Apna Bank")
    window.geometry("500x500")

    details_label = tk.Label(window, text="CURRENT BALANCE", font=("Helvetica", 12))
    details_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

    label1 = tk.Label(window, text="First Name:", font=("Helvetica", 14))
    label1.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    value_label1 = tk.Label(window, text=fname, font=("Helvetica", 14, "bold"))
    value_label1.grid(row=1, column=1, sticky="w", padx=10, pady=5)

    label2 = tk.Label(window, text="Last Name:", font=("Helvetica", 14))
    label2.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    value_label2 = tk.Label(window, text=lname, font=("Helvetica", 14, "bold"))
    value_label2.grid(row=2, column=1, sticky="w", padx=10, pady=5)

    mlabel = tk.Label(window, text="Current Balance:", font=("Helvetica", 14))
    mlabel.grid(row=3, column=0, sticky="w", padx=10, pady=5)

    ans = curr_b(fname, lname)
    mvalue = tk.Label(window, text="Rs " + str(ans), font=("Helvetica", 14))
    mvalue.grid(row=3, column=1, sticky="w", padx=10, pady=5)

    window.mainloop()