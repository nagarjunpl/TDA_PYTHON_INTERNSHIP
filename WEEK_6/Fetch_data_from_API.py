# Fetching data from an API using requests library in Python
# Make sure to install the requests library if you haven't already : pip install requests

import requests # Importing the requests library

# URL of the API
url = "https://api.github.com/users/arjun" # Example API endpoint

# Send GET request
response = requests.get(url)

# Print status code (200 means success)
print("Status Code:", response.status_code)

# Print response in JSON format
print(response.json()) # Convert response to JSON and print it


# # Extract specific data from the JSON response

# data = response.json()
# print("Username:", data["login"])
# print("Public Repos:", data["public_repos"])

