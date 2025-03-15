import requests

# Function to fetch and display TODOs
def fetch_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    
    if response.status_code == 200:  # Check if request was successful
        todos = response.json()  # Convert the response to JSON
        
        # Print the first 10 TODOs
        for i, todo in enumerate(todos[:10], start=1):
            print(f"TODO {i}:")
            print(f"  ID: {todo['id']}")
            print(f"  Title: {todo['title']}")
            print(f"  Completed: {todo['completed']}")
            print("-" * 20)
    else:
        print(f"Failed to fetch TODOs. Status code: {response.status_code}")

# Call the function to execute
fetch_todos()
