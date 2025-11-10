"""
Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

Task Description:

Develop a script named daily_reminder.py. This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized event for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

Instructions:

Prompt for a Single Task:

Ask the user to input a task description and save it into a task variable
Prompt for the task’s priority (high, medium, low) and save it into a priority variable
In a time_bound variable, Ask if the task is time-bound (yes or no)
Process the Task Based on Priority and Time Sensitivity:

Use a Match Case statement to react differently based on the task’s priority.
Within the Match Case or after, use an if statement to modify the event if the task is time-bound.
Provide a Customized Reminder:

Print a event about the task that includes its priority level and whether immediate action is required based on time sensitivity.
A message should be ‘that requires immediate attention today!’
"""


# daily_reminder.py

# Step 1: Prompt user for task info
task = input("Enter your task for today: ")
priority = input("Enter the priority (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

# Step 2: Use match-case for priority
match priority:
    case "high":
        event = "high priority"
    case "medium":
        event = "medium priority"
    case "low":
        event = "low priority"
    case _:
        event = "priority not recognized"

# Step 3: Adjust message based on time sensitivity
if time_bound == "yes":
    message = f"Reminder: '{task}' is a {event} task that requires immediate attention today!"
else:
    message = f"Note: '{task}' is a {event} task. Consider completing it when you have free time."

# Step 4: Loop to remind user
user_response = ""
while user_response.lower() != "done":
    print(message)
    user_response = input("Type 'done' once you have completed or acknowledged the task: ")

print("Great! Task acknowledged. Have a productive day!")


# Works as intended

