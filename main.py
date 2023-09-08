import tkinter as tk
from new_user import new_user_create
from existing_user import exisiting_user_create

root = tk.Tk()
root.title("Bank Management System")
root.geometry("700x300")
root.maxsize(700,300)
root.minsize(700,300)
label = tk.Label(root, text="WELCOME TO THE BANK!!!", font=("Helvetica", 16, "bold"))
label.pack(padx=20, pady=20)

open_button1 = tk.Button(root, text="NEW USER", font=("Helvetica", 16, "bold"),width=20, command=new_user_create)
open_button1.pack(pady=10)  # Add vertical space below the button

open_button2 = tk.Button(root, text="EXISTING USER", font=("Helvetica", 16, "bold"), width=20,command=exisiting_user_create)
open_button2.pack(pady=10)  # Add vertical space below the button

root.mainloop()





