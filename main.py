import tkinter as tk
from tkinter import font
import mysql.connector as mysql

root = tk.Tk()
root.title("Computer Science Project")
root.geometry("1280x720")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

title_font = font.Font(family="Century Gothic", size=24, weight="bold")
label_font = font.Font(family="Century Gothic", size=16)
button_font = font.Font(family="Century Gothic", size=16, weight="bold")

def create_match_database():
    def match_number_label():
        match_number_text = tk.Label(root, text="Enter Match Number (e.g., match31)", font=title_font, bg="#f2f2f2")
        match_number_text.place(relx=0.5, rely=0.3, anchor="center")

    def match_number_entry():
        global match_number_entry_widget
        match_number_entry_widget = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
        match_number_entry_widget.insert(0, "Enter here")
        match_number_entry_widget.bind("<FocusIn>", lambda args: match_number_entry_widget.delete('0', 'end'))
        match_number_entry_widget.place(relx=0.5, rely=0.375, anchor="center")

    def store_match_number():
        global match_number
        match_number = match_number_entry_widget.get()
        print("Database created successfully with name:", match_number)
        create_database_if_not_exist(match_number)

    def open_team_details_window():
        for widget in root.winfo_children():
            widget.destroy()

        def home_team_name_label():
            home_team_label = tk.Label(root, text="Enter Home Team Name", font=label_font, bg="#f2f2f2")
            home_team_label.place(x=10, y=10)

        def away_team_name_label():
            away_team_label = tk.Label(root, text="Enter Away Team Name", font=label_font, bg="#f2f2f2")
            away_team_label.place(x=550, y=10)

        def home_team_entry():
            global home_team_entry_field
            home_team_entry_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
            home_team_entry_field.place(x=10, y=50)

        def away_team_entry():
            global away_team_entry_field
            away_team_entry_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
            away_team_entry_field.place(x=550, y=50)

        def store_team_names():
            global home_team_name, away_team_name
            home_team_name = home_team_entry_field.get()
            away_team_name = away_team_entry_field.get()
            return home_team_name, away_team_name

        def create_match_details_table():
            home_team_name, away_team_name = store_team_names()
            mydb = mysql.connect(host="localhost", user="root", passwd="root")
            my_cur = mydb.cursor()
            connect = f"use {match_number}"
            my_cur.execute(connect)
            use = f"use {match_number}"
            my_cur.execute(use)
            my_cur.execute(f"CREATE TABLE IF NOT EXISTS match_details (home_team VARCHAR(255), away_team VARCHAR(255))")
            inject = f"INSERT INTO match_details (home_team, away_team) VALUES (%s, %s)"
            val = (home_team_name, away_team_name)
            my_cur.execute(inject, val)
            mydb.commit()
            mydb.close()
        def open_player_details_window():
            for widget in root.winfo_children():
                widget.destroy()
            def home_team_name_label_tw():
                home_team_label = tk.Label(root, text="Enter player names of team "+ home_team_name , font=label_font, bg="#f2f2f2")
                home_team_label.place(x=10, y=10)
            def away_team_name_label_tw():
                away_team_label = tk.Label(root, text="Enter player names of team "+ away_team_name, font=label_font, bg="#f2f2f2")
                away_team_label.place(x=500, y=10)
            away_team_name_label_tw()
            home_team_name_label_tw()
            def home_players_entry():
                captain_home_label = tk.Label(root, text="Enter Captain name", font=label_font, bg="#f2f2f2")
                captain_home_label.place(x=10, y=50)
                player2_home_label = tk.Label(root, text="Enter player 2 name", font=label_font, bg="#f2f2f2")
                player2_home_label.place(x=10, y=90)
                player3_home_label = tk.Label(root, text="Enter player 3 name", font=label_font, bg="#f2f2f2")
                player3_home_label.place(x=10, y=130)
                player4_home_label = tk.Label(root, text="Enter player 4 name", font=label_font, bg="#f2f2f2")
                player4_home_label.place(x=10, y=170)
                player5_home_label = tk.Label(root, text="Enter player 5 name", font=label_font, bg="#f2f2f2")
                player5_home_label.place(x=10, y=210)
                player6_home_label = tk.Label(root, text="Enter player 6 name", font=label_font, bg="#f2f2f2")
                player6_home_label.place(x=10, y=250)
                player7_home_label = tk.Label(root, text="Enter player 7 name", font=label_font, bg="#f2f2f2")
                player7_home_label.place(x=10, y=290)
                player8_home_label = tk.Label(root, text="Enter player 8 name", font=label_font, bg="#f2f2f2")
                player8_home_label.place(x=10, y=330)
                player9_home_label = tk.Label(root, text="Enter player 9 name", font=label_font, bg="#f2f2f2")
                player9_home_label.place(x=10, y=370)
                player10_home_label = tk.Label(root, text="Enter player 10 name", font=label_font, bg="#f2f2f2")
                player10_home_label.place(x=10, y=410)
                player11_home_label = tk.Label(root, text="Enter player 11 name", font=label_font, bg="#f2f2f2")
                player11_home_label.place(x=10, y=450)                
            def away_players_entry():
                captain_away_label = tk.Label(root, text="Enter Captain name", font=label_font, bg="#f2f2f2")
                captain_away_label.place(x=500, y=50)
                player2_away_label = tk.Label(root, text="Enter player 2 name", font=label_font, bg="#f2f2f2")
                player2_away_label.place(x=500, y=90)
                player3_away_label = tk.Label(root, text="Enter player 3 name", font=label_font, bg="#f2f2f2")
                player3_away_label.place(x=500, y=130)
                player4_away_label = tk.Label(root, text="Enter player 4 name", font=label_font, bg="#f2f2f2")
                player4_away_label.place(x=500, y=170)
                player5_away_label = tk.Label(root, text="Enter player 5 name", font=label_font, bg="#f2f2f2")
                player5_away_label.place(x=500, y=210)
                player6_away_label = tk.Label(root, text="Enter player 6 name", font=label_font, bg="#f2f2f2")
                player6_away_label.place(x=500, y=250)
                player7_away_label = tk.Label(root, text="Enter player 7 name", font=label_font, bg="#f2f2f2")
                player7_away_label.place(x=500, y=290)
                player8_away_label = tk.Label(root, text="Enter player 8 name", font=label_font, bg="#f2f2f2")
                player8_away_label.place(x=500, y=330)
                player9_away_label = tk.Label(root, text="Enter player 9 name", font=label_font, bg="#f2f2f2")
                player9_away_label.place(x=500, y=370)
                player10_away_label = tk.Label(root, text="Enter player 10 name", font=label_font, bg="#f2f2f2")
                player10_away_label.place(x=500, y=410)
                player11_away_label = tk.Label(root, text="Enter player 11 name", font=label_font, bg="#f2f2f2")
                player11_away_label.place(x=500, y=450)
            home_players_entry()
            away_players_entry()
            def home_players_entry_field():
                home_captain_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                home_captain_field.place(x=220, y=50)
                home_player2_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                home_player2_field.place(x=220, y=90)
                home_player3_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                home_player3_field.place(x=220, y=130)
                home_player4_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                home_player4_field.place(x=220, y=170)
                home_player5_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                home_player5_field.place(x=220, y=210)
                home_player6_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                home_player6_field.place(x=220, y=250)
                home_player7_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                home_player7_field.place(x=220, y=290)
                home_player8_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                home_player8_field.place(x=220, y=330)
                home_player9_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                home_player9_field.place(x=220, y=370)
                home_player10_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                home_player10_field.place(x=220, y=410)
                home_player11_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                home_player11_field.place(x=220, y=450)                
            home_players_entry_field()
            def away_players_entry_field():
                away_captain_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                away_captain_field.place(x=710, y=50)
                away_player2_field = tk.Entry(root, font=label_font, bg="white", bd=2, relief=tk.SOLID)
                away_player2_field.place(x=710, y=90)
            away_players_entry_field()
                
                
                
                
        def go_next():
            create_match_details_table()
            open_player_details_window()

        def submit_button():
            submit_button_widget = tk.Button(root, text="Next", command=go_next, font=button_font, bg="#4CAF50", fg="white", bd=2, relief=tk.SOLID)
            submit_button_widget.place(relx=0.5, rely=0.7, anchor="center")

        home_team_name_label()
        away_team_name_label()
        home_team_entry()
        away_team_entry()
        submit_button()

    def proceed_button():
        store_match_number()
        open_team_details_window()

    def next_button():
        submit_button_widget = tk.Button(root, text="Next", command=proceed_button, font=button_font, bg="#4CAF50", fg="white", bd=2, relief=tk.SOLID)
        submit_button_widget.place(relx=0.5, rely=0.5, anchor="center")

    match_number_label()
    match_number_entry()
    next_button()

def create_database_if_not_exist(db_name):
    mydb = mysql.connect(host="localhost", user="root", passwd="root")
    my_cur = mydb.cursor()
    my_cur.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    mydb.commit()
    mydb.close()

create_match_database()

root.mainloop()
