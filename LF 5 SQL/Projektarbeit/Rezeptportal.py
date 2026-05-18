import sqlite3

is_db_open = False 
connection = sqlite3.connect("Recipeportal.db") 
is_db_open = True 
cursor = connection.cursor() 

sql_command ="""CREATE TABLE User (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    First_Name TEXT,
    EMail TEXT,
    Password TEXT NOT NULL,
    Birthdate DATE,
    Registration_Date DATE
    )"""
cursor.execute(sql_command)

sql_command ="""CREATE TABLE Recipe (
    RecipeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Work_time INTEGER,
    Total_time INTEGER,
    Difficulty TEXT,
    Registration_Date DATE,
    )"""
cursor.execute(sql_command)

sql_command ="""CREATE TABLE Ingredient (
    IngredientID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    
    