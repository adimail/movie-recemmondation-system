import requests

api_key = "978e5c7a7fe49a1a6496279638088e9c"
base_url = "https://api.themoviedb.org/3/movie/550"  # Example API endpoint, replace with your desired endpoint

params = {
        "api_key": api_key,
    }

response = requests.get(base_url, params=params)

print(response.text)