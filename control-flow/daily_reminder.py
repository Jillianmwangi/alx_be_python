task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()
reminder = f"Task: {task}\nPriority: {priority.capitalize()}"

match priority:
    case "high":
        reminder += "\nThis is a high-priority task."
    case "medium":
        reminder += "\nThis is a medium-priority task."
    case "low":
        reminder += "\nThis is a low-priority task."
    case _:
        reminder += "\nPriority level not recognized."

if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

print("\nReminder:")
print(reminder)