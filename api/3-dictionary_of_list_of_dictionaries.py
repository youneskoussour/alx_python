import json
import requests



def get_employee_info(employee_id):
    """Fetch the employee details from the given URL by appending the employee_id and convert the data to JSON."""
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    """Fetch the employee's todo by appending the todo route to the URL."""
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    """Compute the number of done tasks and the total number of tasks."""
    completed_tasks = [{'username': employee_data['username'], 'task': task['title'], 'completed': task['completed']} for task in todos_data]

    """Return the completed tasks."""
    return completed_tasks

def export_all_tasks():
    """Records all tasks from all employees and export data in the JSON format."""
    all_employees_tasks = {}

    # Iterate over employee IDs from 1 to 10 (based on JSONPlaceholder API)
    for employee_id in range(1, 11):
        all_employees_tasks[str(employee_id)] = get_employee_info(employee_id)

    # Writing to JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_tasks, json_file, indent=4)

if __name__ == "__main__":
    export_all_tasks()