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
    # Use match case for priority handling
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
        case _:
            base_message = "Invalid priority level"
    
    # Use if statement for time-bound modification
    if time_bound == "yes":
        final_message = f"Reminder: {base_message} that requires immediate attention today!"
    else:
        if priority == "low":
            final_message = f"Note: {base_message}. Consider completing it when you have free time."
        else:
            final_message = f"Note: {base_message}."
    
    return final_message

def main():
    # Get task details
    task, priority, time_bound = get_task_details()
    
    # Generate and print reminder
    print("\n" + generate_reminder(task, priority, time_bound))

if __name__ == "__main__":
    main()