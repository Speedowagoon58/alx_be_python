import datetime
from datetime import datetime, timedelta

current_date = datetime.now()
formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted current date and time: {formatted_date}")

def display_current_datetime():
    current_date = datetime.now()
    print(f'Current date and time: {current_date}')

def calculate_future_date(): 
    # Get the current date
    current_date = datetime.now()
    
    # Prompt the user for the number of days to add
    days_to_add = int(input('Enter the number of days to add to the current date: ')) 
    
    # Add the number of days to the current date
    future_date = current_date + timedelta(days=days_to_add)
    
    # Return and display the future date
    print(f'The date after {days_to_add} days will be: {future_date}')
    return future_date 

# Call the functions
display_current_datetime()
calculate_future_date()