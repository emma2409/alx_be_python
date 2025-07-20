task = input("Enter the task for the day: ")
priority = input("Enter the priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"  
    case _:
        message = f"'{task}' has an unrecognized priority level."

# Append urgency if time-bound
if time_bound == "yes" and "unrecognized" not in message:
    message += " that requires immediate attention today!"  
elif time_bound == "no" and "low priority task" in message:
    message += ". Consider completing it when you have free time."
else:
    message += " and can be scheduled for later."

# Output the customized reminder
print()
print(message)