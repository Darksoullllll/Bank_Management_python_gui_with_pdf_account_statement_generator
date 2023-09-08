import tkinter as tk 
from withdraw_money import withdraw
from deposite_money import deposite
from view_balance import show_bal
from accn_statement import generate_statement_user
import mysql.connector
def user_detail(name,password):
    db_connection = mysql.connector.connect(
        host="127.0.0.1",      # Replace with your host
        user="root",  # Replace with your username
        password="database password",  # Replace with your password
        database="first create database in sql workbench"  # Replace with your database name
    )
    cursor = db_connection.cursor()
    new_name =  str(name)
    res = new_name.split()
    fname = res[0]
    lname = res[1]
    sql_query = "SELECT * FROM Account_Money WHERE fname=%s AND  lname=%s"
    cursor.execute(sql_query,(fname,lname))
    result = cursor.fetchall()
    column_mapping = {
        "fname": "First Name",
        "lname": "Last Name",
        "dob": "Date of Birth",
        "gender": "Gender",
        "accn": "Account Number"
    }
    result_dict = {}
    for i in range(1, len(cursor.description)-1):
        column_name = cursor.description[i][0]
        if column_name in column_mapping:
            result_dict[column_mapping[column_name]] = result[0][i]

    cursor.close()
    db_connection.close()
    return result_dict
def bank_main_Screen(name,password):
    window = tk.Tk()
    window.geometry("800x700")
    window.title("Welcome To Apna Bank " + name)

    # Label for the user window
    new_user_label = tk.Label(window, text="User Window of " + name, font=("Helvetica", 16, "bold"))
    new_user_label.pack(pady=20)
    
    new_name =  str(name)
    res = new_name.split()
    fname = res[0]
    lname = res[1]
    # Frame for displaying user details
    frame = tk.Frame(window)
    frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    # Retrieve user details
    res = user_detail(name, password)

    # Display user details in a grid
    row = 0
    for key, value in res.items():
        label = tk.Label(frame, text=f"{key}:", font=("Helvetica", 14))
        label.grid(row=row, column=0, sticky="w", padx=10, pady=5)

        value_label = tk.Label(frame, text=value, font=("Helvetica", 14, "bold"))
        value_label.grid(row=row, column=1, sticky="w", padx=10, pady=5)

        row += 1
    
   
    # Buttons for bank actions
    withdraw_money = tk.Button(window, text="Withdraw Money", width=20, height=3,command=lambda: withdraw(fname,lname))
    withdraw_money.pack(side=tk.LEFT, padx=20, pady=20)

    deposit_money = tk.Button(window, text="Deposit Money", width=20, height=3,command= lambda: deposite(fname,lname))
    deposit_money.pack(side=tk.LEFT, padx=20, pady=20)

    view_balance = tk.Button(window, text="View Balance", width=20, height=3,command= lambda: show_bal(fname,lname))
    view_balance.pack(side=tk.LEFT, padx=20, pady=20)
    
    generate_statement = tk.Button(window, text="Account Statement", width=20, height=3,command= lambda: generate_statement_user(fname,lname))
    generate_statement.pack(side=tk.LEFT, padx=20, pady=20)

    window.mainloop()
