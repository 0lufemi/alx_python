import requests
import csv
import sys

def get_employee_info(employee_id):
    # Get employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    # Get employee's TODO list
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Create a CSV file with the employee's ID as the filename
    csv_filename = f'{employee_id}_copy.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        # Create a CSV writer
        csv_writer = csv.writer(csvfile)

        # Write the header row
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write each task as a row in the CSV file
        for task in todo_data:
            csv_writer.writerow([employee_id, employee_data['username'], str(task['completed']), task['title']])

if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_info(employee_id)
        print(f"Data exported to {employee_id}_copy.csv")
    except ValueError:
        print("Please provide a valid integer for the employee ID.")
        sys.exit(1)
