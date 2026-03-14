import sqlite3
from datetime import date

def get_db_connection():
    conn = sqlite3.connect('workout_tracker.db')
    conn.row_factory = sqlite3.Row
    return conn

def add_workout_log():
    """CREATE: Adds a new workout entry with Set Number and RPE"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    print("\n--- Select an Exercise ---")
    cursor.execute("SELECT id, name FROM exercises")
    exercises = cursor.fetchall()
    for ex in exercises:
        print(f"{ex['id']}: {ex['name']}")
    
    try:
        ex_id = int(input("Enter Exercise ID: "))
        set_num = int(input("Enter Set Number (e.g., 1): ")) # NEW
        weight = float(input("Enter Weight: "))
        reps = int(input("Enter Reps: "))
        rpe = int(input("Enter RPE (Intensity 1-10): "))     # NEW
        notes = input("Notes (optional): ")
        today = date.today().strftime("%Y-%m-%d")

        # Added set_number and rpe to the INSERT statement
        cursor.execute('''
            INSERT INTO workout_logs (exercise_id, set_number, weight, reps, rpe, workout_date, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (ex_id, set_num, weight, reps, rpe, today, notes))
        
        conn.commit()
        print("✅ Log added successfully!")
    except ValueError:
        print("❌ Invalid input. Please use numbers where required.")
    finally:
        conn.close()

def view_logs(filter_muscle=None):
    """READ: Displays logs including the new Set and RPE data"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Updated query to pull set_number and rpe
    query = '''
        SELECT l.id, e.name, l.set_number, l.weight, l.reps, l.rpe, l.workout_date 
        FROM workout_logs l
        JOIN exercises e ON l.exercise_id = e.id
    '''
    
    if filter_muscle:
        query += " WHERE e.muscle_group = ?"
        cursor.execute(query, (filter_muscle,))
    else:
        query += " ORDER BY l.workout_date DESC, l.id DESC"
        cursor.execute(query)
        
    logs = cursor.fetchall()
    
    print(f"\n--- {'All Logs' if not filter_muscle else filter_muscle + ' Logs'} ---")
    # Updated headers to show Set and RPE
    print(f"{'ID':<4} {'Date':<12} {'Exercise':<15} {'Set':<5} {'Weight':<8} {'Reps':<6} {'RPE':<4}")
    print("-" * 60)
    for log in logs:
        print(f"{log['id']:<4} {log['workout_date']:<12} {log['name']:<15} {log['set_number']:<5} {log['weight']:<8} {log['reps']:<6} {log['rpe']:<4}")
    
    conn.close()

def update_log():
    """UPDATE: Modify an existing record"""
    view_logs()
    try:
        log_id = int(input("\nEnter the ID of the log you want to update: "))
        new_weight = float(input("Enter new weight: "))
        new_reps = int(input("Enter new reps: "))
        new_rpe = int(input("Enter new RPE: ")) # Added this to the update option
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE workout_logs 
            SET weight = ?, reps = ?, rpe = ? 
            WHERE id = ?
        ''', (new_weight, new_reps, new_rpe, log_id))
        conn.commit()
        conn.close()
        print("✅ Log updated!")
    except ValueError:
        print("❌ Error: Please enter valid numbers.")

def delete_log():
    """DELETE: Remove a record"""
    view_logs()
    log_id = input("\nEnter the ID of the log to delete: ")
    confirm = input(f"Are you sure you want to delete log {log_id}? (y/n): ")
    
    if confirm.lower() == 'y':
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM workout_logs WHERE id = ?", (log_id,))
        conn.commit()
        conn.close()
        print("✅ Log deleted.")

def main_menu():
    while True:
        print("\n--- 🏋️ WORKOUT TRACKER ---")
        print("1. Log a Workout (Create)")
        print("2. View All Logs (Read)")
        print("3. View Logs by Muscle Group (Filter)")
        print("4. Update a Log (Update)")
        print("5. Delete a Log (Delete)")
        print("6. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            add_workout_log()
        elif choice == '2':
            view_logs()
        elif choice == '3':
            muscle = input("Enter muscle group: ")
            view_logs(filter_muscle=muscle)
        elif choice == '4':
            update_log()
        elif choice == '5':
            delete_log()
        elif choice == '6':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main_menu()