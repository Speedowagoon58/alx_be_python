# daily_reminder.py

def get_task_details():
    # Get task description
    task = input("Enter your task: ")
    
    # Get priority level
    priority = input("Priority (high/medium/low): ").lower()
    
    # Get time sensitivity
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    # Create reminder message matching the exact format from example
    if time_bound == "yes":
        reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
    else:
        if priority == "low":
            reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
        else:
            reminder = f"Note: '{task}' is a {priority} priority task."
    
    return reminder

def main():
    # Get task details from user
    task, priority, time_bound = get_task_details()
    
    # Generate and display the reminder
    reminder = generate_reminder(task, priority, time_bound)
    print("\n" + reminder)

if __name__ == "__main__":
    main()