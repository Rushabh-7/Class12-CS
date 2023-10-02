import tkinter as tk
from tkinter import font
import mysql.connector as mysql

root = tk.Tk()
root.title("Computer Science Project")
root.geometry("1280x650")
root.resizable(False, False)
root.configure(bg="#0b0c10")

title_font=font.Font(family="Century Gothic", size=36, weight="bold")
label_font=font.Font(family="Century Gothic", size=28)
button_font=font.Font(family="Century Gothic", size=20, weight="bold")

def create_database():
    
    def db_name_label():
        db_name_text=tk.Label(root, text="Database Name:", font=label_font, bg="#0b0c10", fg="#66fcf1")
        db_name_text.place(relx=0.5, rely=0.4, anchor="center")
    db_name_label()
    def db_entry_widget():
        global db_entry_field
        db_entry_field=tk.Entry(root, font=label_font, bg="#1f2833", fg="#66fcf1", bd=5, relief="solid")
        db_entry_field.insert(0, "Enter here",)
        db_entry_field.configure(justify="center", fg="#f2f2f2")
        db_entry_field.bind("<FocusIn>", lambda args: db_entry_field.delete('0', 'end'))
        db_entry_field.place(relx=0.5, rely=0.5, anchor="center")
    def store_db_name():
        global db_name
        db_name=db_entry_field.get()
        print("Database created with name: ", db_name)
        creating_db(db_name)        
    db_entry_widget()
    def creating_db(db_name):        
        mydb=mysql.connect(host="localhost", user="root", passwd="root")
        mycur=mydb.cursor()
        mycur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")        
        mydb.commit()
        mydb.close()
    

    def next_window():        
        for widget in root.winfo_children():
            widget.destroy()
            
            
    def next_window_button():
        store_db_name()
        next_window()    
    def next_button():
        next_button=tk.Button(root, text="Next", font=button_font, bg="#1f2833", fg="#66fcf1", bd=5, relief="solid", command=next_window_button)
        next_button.place(relx=0.5, rely=0.6, anchor="center")
    next_button()
        
create_database()

root.mainloop()
