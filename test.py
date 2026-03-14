import sqlite3
import os

db = "workouts.db"
con = sqlite3.connect(db)
cursor = con.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS workouts (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   date TEXT,
                   exercise TEXT,
                   sets INTEGER,
                   reps INTEGER
               )
               ''')

cursor.execute("INSERT INTO workouts (date, exercise, sets, reps) VALUES (?, ?, ?, ?)",
               ('2026-03-13', 'Smith Bench', 2, 8))

con.commit()

print("Workout Log")
cursor.execute("SELECT * FROM workouts")
all_exercises = cursor.fetchall()
for workout in all_exercises:
    print(f'date: {workout[1]}, exercise: {workout[2]}, sets: {workout[3]}, reps: {workout[4]}')

con.close()

