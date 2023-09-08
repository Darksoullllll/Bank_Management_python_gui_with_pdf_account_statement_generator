import tkinter as tk
import tkinter.messagebox
import mysql.connector
from user_main_screen import bank_main_Screen
def isfound(existing_user_window,name,password):
    db_connection = mysql.connector.connect(
        host="127.0.0.1",      # Replace with your host
        user="root",  # Replace with your username
         password="database password",  # Replace with your password
        database="first create database in sql workbench"  # Replace with your database name
    )
    cursor = db_connection.cursor()
    sql_query = "SELECT * FROM users WHERE name=%s AND password=%s"
    cursor.execute(sql_query,(name,password))
    result = cursor.fetchall()
    if result:
        result1 = result[0][1]  # Assuming the first column is the ID column
        result2 = result[0][4]  # Assuming the second column is the name column
        
        if result1 == name and result2 == password:
            tkinter.messagebox.showinfo("Success", "Welcome Back " + name)
            existing_user_window.destroy()
            bank_main_Screen(name, password)
            
        else:
            tkinter.messagebox.showerror("Error", "Invalid User Name or Password")
    else:
        tkinter.messagebox.showerror("Error", "User not found")
    
    cursor.close()
    db_connection.close()
def exisiting_user_create():
    exisiting_user_window = tk.Tk()
    exisiting_user_window.geometry("350x150")
    exisiting_user_window.title("LOGIN")

    
    name_label = tk.Label(exisiting_user_window, text="Name:")
    name_label.grid(row=1, column=0, padx=20, pady=5)
    name_entry = tk.Entry(exisiting_user_window)
    name_entry.grid(row=1, column=1, padx=20, pady=5)

    password_label = tk.Label(exisiting_user_window, text="Password:")
    password_label.grid(row=2, column=0, padx=20, pady=5)
    password_entry = tk.Entry(exisiting_user_window, show="*")
    password_entry.grid(row=2, column=1, padx=20, pady=5)

    register_button = tk.Button(exisiting_user_window, text="LOGIN", font=("Helvetica", 14),command=lambda: isfound(exisiting_user_window,name_entry.get(),password_entry.get()))
    register_button.grid(row=4, column=1, pady=20)

