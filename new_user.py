import tkinter as tk
import tkinter.messagebox
import mysql.connector
from adding_money_in_bank_new_user import insert_money

def databases(new_user_window,name,email,gender,password):
    db_connection = mysql.connector.connect(
        host="127.0.0.1",      # Replace with your host
        user="root",  # Replace with your username
        password="database password",  # Replace with your password
        database="first create database in sql workbench"  # Replace with your database name
    )
    cursor = db_connection.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            gender VARCHAR(20),
            password VARCHAR(255)
        )
    """
    cursor.execute(create_table_query)
    # Insert user data into the database
    insert_query = "INSERT INTO users (name, email, gender, password) VALUES (%s, %s, %s, %s)"
    data = (name, email, gender, password)
    cursor.execute(insert_query, data)
    
    # Commit changes and close the connection
    db_connection.commit()
    db_connection.close()
    
    tkinter.messagebox.showinfo("Success","User registered successfully in the bank!")
    new_user_window.destroy()
    insert_money()
def new_user_create():
    new_user_window = tk.Tk()
    new_user_window.geometry("400x300")
    new_user_window.title("New User Registration")

    new_user_label = tk.Label(new_user_window, text="New User Registration", font=("Helvetica", 16, "bold"))
    new_user_label.grid(row=0, columnspan=2, padx=20, pady=20)

    name_label = tk.Label(new_user_window, text="Name:")
    name_label.grid(row=1, column=0, padx=20, pady=5)
    name_entry = tk.Entry(new_user_window)
    name_entry.grid(row=1, column=1, padx=20, pady=5)

    email_label = tk.Label(new_user_window, text="Email:")
    email_label.grid(row=2, column=0, padx=20, pady=5)
    email_entry = tk.Entry(new_user_window)
    email_entry.grid(row=2, column=1, padx=20, pady=5)

    options = ["Male", "Female", "Others"]
    selected_option = tk.StringVar(new_user_window)
    selected_option.set(options[0])
    
    gender_label = tk.Label(new_user_window, text="Gender:")
    gender_label.grid(row=3, column=0, padx=20, pady=5)
    select_box = tk.OptionMenu(new_user_window, selected_option, *options)
    select_box.grid(row=3, column=1, padx=20, pady=20)
    
    password_label = tk.Label(new_user_window, text="Password:")
    password_label.grid(row=4, column=0, padx=20, pady=5)
    password_entry = tk.Entry(new_user_window, show="*")
    password_entry.grid(row=4, column=1, padx=20, pady=5)

    register_button = tk.Button(new_user_window, text="Register", font=("Helvetica", 14), command=lambda: databases(new_user_window,name_entry.get(), email_entry.get(), selected_option.get(), password_entry.get()))
    register_button.grid(row=5, column=1, pady=20)
    
