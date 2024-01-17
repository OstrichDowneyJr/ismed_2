import sqlite3


class Patient:
    def __init__(self, name, lastname, time, date, up, down, rate) -> None:
        self.name = name
        self.lastname = lastname
        self.time = time 
        self.date = date
        self.up = up
        self.down = down 
        self.rate = rate
        
    def __str__(self):
       return (f"{self.name} {self.lastname} {self.date} {self.time} {self.up} {self.down} {self.rate}")

connection = sqlite3.connect("patient.sqlite")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS blood_pressure (name TEXT, lastname TEXT, time TIME, date DATE, up INTIGER, down INTIGER, rate INTIGER)")

def fetch_name(selected_name):
    """fetches a name from a patient.sqlite database
        param1: name -> Str
        return: records from database -> list of strings"""

    patients = []
    cursor.execute("SELECT * FROM blood_pressure WHERE name LIKE ?",(selected_name,))    
    rows = cursor.fetchall()
    for index, row in enumerate(rows):
        patients.append(str(Patient(rows[index][0], rows[index][1], rows[index][2], rows[index][3], rows[index][4], rows[index][5], rows[index][6])))
    return patients 
