import requests

def fetch_highest_grossing_nolan_movie(api_key):
    base_url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": api_key,
        "with_people": "5256",  # Christopher Nolan's TMDb person ID
        "sort_by": "revenue.desc",
        "vote_count.gte": 1000  # Minimum vote count threshold
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        movies = response.json()["results"]
        if movies:
            highest_grossing_movie = movies[0]
            title = highest_grossing_movie["title"]
            return title
        else:
            return None
    else:
        print("Failed to fetch movie data. Status code:", response.status_code)
        return None

# Replace "YOUR_API_KEY" with your actual TMDb API key
api_key = "978e5c7a7fe49a1a6496279638088e9c"
title = fetch_highest_grossing_nolan_movie(api_key)

if title:
    print("Highest-grossing Christopher Nolan movie:", title)
else:
    print("No Christopher Nolan movies found or an error occurred.")
