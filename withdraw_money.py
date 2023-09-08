import tkinter as tk
from tkinter import messagebox
import mysql.connector
def perform_withdraw(window,wmoney,fname,lname):
    db_connection = mysql.connector.connect(
        host="127.0.0.1",      # Replace with your host
        user="root",  # Replace with your username
         password="database password",  # Replace with your password
        database="first create database in sql workbench"  # Replace with your database name
    )
    cursor = db_connection.cursor()

    sql_query = "Select money from Account_Money where fname = %s AND lname = %s"
    cursor.execute(sql_query,(fname,lname))
    result = cursor.fetchone()
    new_result = result[0]
    if(new_result<int(wmoney)):
        messagebox.showwarning("showwarning", "Insufficient Balance")
    else:
        new_result= new_result - int(wmoney)
        sql_query2 = "Update Account_Money set money = %s where fname = %s AND lname = %s"
        cursor.execute(sql_query2,(new_result,fname,lname))
        db_connection.commit()
        messagebox.showinfo("Update","Withdraw Money Successful Balance is Updated !!!")
    cursor.close()
    db_connection.close()
    window.destroy()

def withdraw(fname, lname):
    window = tk.Tk()
    window.title("Welcome To The Apna Bank")
    window.geometry("500x500")

    details_label = tk.Label(window, text="WITHDRAW MONEY", font=("Helvetica", 12))
    details_label.grid(row=0,column=0,padx=20,pady=20)

    label1 = tk.Label(window, text="First Name", font=("Helvetica", 14))
    label1.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    value_label1 = tk.Label(window, text=fname, font=("Helvetica", 14, "bold"))
    value_label1.grid(row=1, column=1, sticky="w", padx=10, pady=5)

    label2 = tk.Label(window, text="Last Name", font=("Helvetica", 14))
    label2.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    value_label2 = tk.Label(window, text=lname, font=("Helvetica", 14, "bold"))
    value_label2.grid(row=2, column=1, sticky="w", padx=10, pady=5)

    withdrawal_label = tk.Label(window, text="Withdrawal Amount", font=("Helvetica", 14))
    withdrawal_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

    withdrawal_entry = tk.Entry(window, font=("Helvetica", 14))
    withdrawal_entry.grid(row=3, column=1, padx=10, pady=5)
    withdraw_button = tk.Button(window, text="Withdraw", command=lambda: perform_withdraw(window,withdrawal_entry.get(),fname,lname), font=("Helvetica", 14))
    withdraw_button.grid(row=4, columnspan=2, pady=20)

    window.mainloop()
