
import sqlite3

is_db_open = False 
connection = sqlite3.connect("personenverwaltung1.db") 
is_db_open = True 
cursor = connection.cursor() 
sql_anweisung ="""CREATE TABLE Person (
    PersonID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Vorname TEXT,
    Groesse REAL,
    Gewicht REAL,
    Geburtsdatum DATE, 
    OrtID INTEGER
    )"""
cursor.execute(sql_anweisung)

sql_anweisung = " INSERT INTO Person (Name, Vorname, Groesse, Gewicht, Geburtsdatum, OrtID) VALUES (' Winkelmann ',' Frank ', 1.80,80.00,' 23.4.2020 ', 1)" 
cursor.execute(sql_anweisung)
sql_anweisung = " INSERT INTO Person (Name, Vorname, Groesse, Gewicht, Geburtsdatum, OrtID) VALUES (' Winkelmann ',' Frank ', 1.80,80.00,' 23.4.2020 ', 1)" 
cursor.execute(sql_anweisung)

sql_anweisung =" SELECT * FROM Person" 
cursor.execute(sql_anweisung)

for datensatz in cursor: 
    print (str (datensatz [0]) +"" + #PersonID 
            str (datensatz [1]) +"" + #Name 
            str (datensatz [2]) +"" + #Vorname 
            str (datensatz [3]) +" " + #Groesse 
            str (datensatz [4]) +"" + #Gewicht 
            str (datensatz [5]) +"" + #Geburtsdatum 
            str (datensatz [6]) ) #OrtID
if is_db_open == True: 
    connection. close ()
