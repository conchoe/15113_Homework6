# 15113_Homework6

I built a database for the intermediate-advanced lifter who cares about their progress, or any beginner who wants to begin taking the gym seriously. 

The motivation: Progressive overload is the most importatnt part of lifting. To build muslce or to gain strength it is a requirement that the work that you do increases over time. Many bodybuilders use their notes app or a a physical journal to keep track of their lifts, comparing this week to last week. While this is all that is needed to make sure you are progressing, the biggest problem for people going to the gym is feeling like they aren't making progress, which is easy to feel if you are only comparing this week to last week. So, I built a database that tracks your lifts and you can retrieve data from years or months ago truly see how much progress you have made. 

Database Schema
The app uses a relational SQLite database with two tables to ensure data integrity and make analysis easier.

Table: exercises
Acts as a master list for all possible movements.
| id | INTEGER | Primary Key (Unique ID) |
| name | TEXT | Name of the exercise (e.g., Squat) |
| muscle_group| TEXT | Target muscle (e.g., Legs) |
| equipment | TEXT | Equipment needed (e.g., Barbell) |

Table: workout_logs
Stores the data for every individual set performed.
| id | INTEGER | Primary Key (Unique ID) |
| exercise_id | INTEGER | Foreign Key (Links to exercises.id) |
| set_number | INTEGER | The set count (e.g., 1, 2, 3) |
| weight | REAL | Weight used in lbs or kg |
| reps | INTEGER | Number of repetitions completed |
| rpe | INTEGER | Intensity score from 1-10 |
| workout_date| TEXT | Date of entry (YYYY-MM-DD) |
| notes | TEXT | Optional comments on the set |

How to Run
Prerequisites: Ensure you have Python 3.x installed. No external libraries are required as sqlite3 is built-in.

Initialize Database: Run the setup script to create the tables and seed the initial exercises:

Bash
python db_setup.py
Launch App: Start the interactive tracker:

Bash
python app.py
Note: To reset the database at any time, delete the workout_tracker.db file and run db_setup.py again.

CRUD Operations
Create (Log a Workout): Select Option 1 from the menu. You will choose an exercise by its ID and enter your set number, weight, reps, and RPE.

Read (View Logs):

Select Option 2 to view all recorded sets across all time.

Select Option 3 to filter by a specific muscle group (e.g., "Chest") to see your progress on specific areas.

Update (Modify a Log): Select Option 4. The app will list your logs; enter the specific Log ID you wish to change to update the weight, reps, or RPE for that set.

Delete (Remove a Log): Select Option 5. Enter the Log ID of the entry you wish to remove. The app will ask for a final confirmation before deleting the record.