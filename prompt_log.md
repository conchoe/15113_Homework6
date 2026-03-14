1. can you give me a 15 minute learning guide on what sqlite is and how databases work in general, what are their use cases? How do i use databases to build things?

2. okay I want to make a workout logging data base that I can also use later on to perform data analysis on my workouts. ie percentage of how much I have progressed in the last few months etc. Can you help me implement a plan to create JUST the sqlite database

3. The key design decision: one table or two?

For pure logging, one table works fine. But for analysis (progress over time, personal records, volume by muscle group), a two-table design is much better:

visualize show_widget

The exercises table is basically a master list (e.g. "Bench Press", "Squat", "Deadlift") and workout_logs stores each individual session, referencing exercises by their ID. This way "Bench Press" is never misspelled across 200 rows, and your analysis queries can cleanly group by exercise or muscle group.

The implementation plan (database only)

Here's what we'll build in one focused step — just db_setup.py:

Create the two tables

Add a few seed exercises (so you can test immediately)

Add a helper function to verify everything was created correctly

Include a note in the file about how to wipe and recreate the DB during development

can you help me implement this plan for this