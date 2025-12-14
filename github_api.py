import requests

username = "VRaz104"
url = f"https://api.github.com/users/{username}"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    print(f"Status Code: {response.status_code}")
    print(f"Username: {data['login']}")
    print(f"Public Repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
    print(f"Profile URL: {data['html_url']}")
    
except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")
except KeyError as e:
    print(f"Unexpected API response format. Missing key: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")