import tkinter as tk
from tkcalendar import Calendar
import random
import mysql.connector
import tkinter.messagebox
def databases(add_money,first_name,last_name,d_o_b,gender,accn,money):
    money_val =  float(money)
    if(money_val < 0 ):
        tkinter.messagebox.showinfo("Error","Money Can't be Negative please try Again")
    db_connection = mysql.connector.connect(
        host="127.0.0.1",      # Replace with your host
        user="root",  # Replace with your username
         password="database password",  # Replace with your password
        database="first create database in sql workbench"  # Replace with your database name
    )
    cursor = db_connection.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS Account_Money (
            id INT AUTO_INCREMENT PRIMARY KEY,
            fname VARCHAR(255),
            lname VARCHAR(255),
            dob VARCHAR(255),
            gender VARCHAR(20),
            accn VARCHAR(255),
            money int
        )
    """

    cursor.execute(create_table_query)
    # Insert user data into the database
    insert_query = "INSERT INTO Account_Money (fname,lname,dob,gender,accn,money) VALUES (%s, %s, %s, %s, %s, %s)"
    data = (first_name,last_name,d_o_b,gender,accn,money)
    cursor.execute(insert_query, data)
    
    # Commit changes and close the connection
    db_connection.commit()
    db_connection.close()
    tkinter.messagebox.showinfo("Success","THANK YOU FOR CHOOSING APNA BANK !!!!")
    add_money.destroy()

def insert_money():
    add_money = tk.Tk()
    add_money.geometry("800x700")
    add_money.title("Add Money To Open Your Account")

    
    add_money_label = tk.Label(add_money, text="OPENING ACCOUNT", font=("Helvetica", 16, "bold"))
    add_money_label.grid(row=0, columnspan=2, padx=20, pady=20)

    user_name = tk.Label(add_money,text="First Name: ")
    user_name.grid(row=1, column=0, padx=20, pady=5)
    name_entry1 = tk.Entry(add_money)
    name_entry1.grid(row=1, column=1, padx=20, pady=5)
    
    user_name = tk.Label(add_money,text="Last Name: ")
    user_name.grid(row=2, column=0, padx=20, pady=5)
    name_entry2 = tk.Entry(add_money)
    name_entry2.grid(row=2, column=1, padx=20, pady=5)

    user_dob = tk.Label(add_money,text="Date Of Birth: ")
    user_dob.grid(row=3,column=0 ,padx=20, pady=5 )
    dob_calender = Calendar(add_money, selectmode="day", year=2023, month=8, day=31,width=10, height=8)
    dob_calender.grid(row=3,column=1,padx=20,pady=5)
    select_button = tk.Button(add_money, text="Select Date")
    select_button.grid(row=4,column=1,padx=20,pady=5)
    date_is = dob_calender.get_date()

    options = ["Male", "Female", "Others"]
    selected_option = tk.StringVar(add_money)
    selected_option.set(options[0])
    
    gender_label = tk.Label(add_money, text="Gender:")
    gender_label.grid(row=5, column=0, padx=20, pady=5)
    select_box = tk.OptionMenu(add_money, selected_option, *options)
    select_box.grid(row=5, column=1, padx=20, pady=20)

    def generate_unique_account_number():
        while True:
            unique_account_number = random.randint(100000, 999999)  # Generate a 6-digit account number
            if unique_account_number not in generated_accn:
                generated_accn.add(unique_account_number)
                return unique_account_number

    user_accn = tk.Label(add_money,text="User Account No: ")
    user_accn.grid(row=6, column=0, padx=20, pady=5)

    generated_accn = set()
    unique_account_number = generate_unique_account_number()
    account_number_label = tk.Label(add_money, text=str(unique_account_number))
    account_number_label.grid(row=6, column=1, padx=20, pady=5)

    money_label = tk.Label(add_money, text="Enter Money:")
    money_label.grid(row=7, column=0, padx=20, pady=5)
    money_entry = tk.Entry(add_money)
    money_entry.grid(row=7, column=1, padx=20, pady=5)

    open_button = tk.Button(add_money, text="Open Account", font=("Helvetica", 14), command=lambda: databases(add_money,name_entry1.get(), name_entry2.get(),date_is, selected_option.get(), unique_account_number,money_entry.get()))
    open_button.grid(row=8, column=1, pady=20)



