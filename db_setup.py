import sqlite3

def setup_database():
    # Connect to the database file
    conn = sqlite3.connect('workout_tracker.db')
    cursor = conn.cursor()

    # Enable Foreign Key support so the link between tables stays strong
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Create the 'exercises' table (The Master List)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            muscle_group TEXT NOT NULL,
            equipment TEXT
        )
    ''')

    # 2. Create the 'workout_logs' table (The Session Data)
    # Added: set_number (INTEGER) and rpe (INTEGER)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workout_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise_id INTEGER NOT NULL,
            set_number INTEGER NOT NULL,  -- Added this to track which set it is
            weight REAL NOT NULL,
            reps INTEGER NOT NULL,
            rpe INTEGER,                  -- Added this (Rate of Perceived Exertion 1-10)
            workout_date TEXT NOT NULL,   -- Format: YYYY-MM-DD
            notes TEXT,
            FOREIGN KEY (exercise_id) REFERENCES exercises (id)
        )
    ''')

    # 3. Seed some initial data
    # No changes needed here, since this only populates the exercise list
    seed_exercises = [
        ('Bench Press', 'Chest', 'Barbell'),
        ('Squat', 'Legs', 'Barbell'),
        ('Deadlift', 'Back', 'Barbell'),
        ('Overhead Press', 'Shoulders', 'Dumbbell'),
        ('Bicep Curl', 'Arms', 'Dumbbell')
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO exercises (name, muscle_group, equipment) 
        VALUES (?, ?, ?)
    ''', seed_exercises)

    conn.commit()
    print("✅ Database updated with RPE and Set Number columns!")
    
    # Verification Helper
    cursor.execute("SELECT name FROM exercises")
    exercises = cursor.fetchall()
    print(f"Current Exercises available: {[e[0] for e in exercises]}")
    
    conn.close()

if __name__ == "__main__":
    # IMPORTANT: Since you changed the table structure, you MUST delete 
    # the old 'workout_tracker.db' file in your folder before running this 
    # so the table can be recreated with the new columns!
    setup_database()