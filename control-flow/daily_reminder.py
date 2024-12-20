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
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
        case _:
            return "Invalid priority level entered."
    
    # Add time sensitivity note
    if time_bound == "yes":
        base_message += " that requires immediate attention today!"
    else:
        if priority == "low":
            base_message += ". Consider completing it when you have free time."
        else:
            base_message += ". Plan to complete this task soon."
    
    return base_message

def main():
    # Get task details from user
    task, priority, time_bound = get_task_details()
    
    # Generate and display the reminder
    reminder = generate_reminder(task, priority, time_bound)
    print("\nReminder:", reminder)

if __name__ == "__main__":
    main()