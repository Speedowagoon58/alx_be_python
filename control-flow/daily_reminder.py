# daily_reminder.py

def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            priority_message = "a high priority task"
        case "medium":
            priority_message = "a medium priority task"
        case "low":
            priority_message = "a low priority task"
        case _:  # Default case for invalid input
            print("Invalid priority entered.")
            return  # Exit the program

    if time_bound == "yes":
        time_message = "that requires immediate attention today!"
    elif time_bound == "no":
        time_message = ". Consider completing it when you have free time."
    else:
        print("Invalid time-bound input.")
        return

    reminder = f"'{task}' is {priority_message}{time_message}"
    print("Reminder:", reminder)

if __name__ == "__main__":
    main()