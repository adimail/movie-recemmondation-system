import requests

def fetch_highest_rated_nolan_movie(api_key):
    base_url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": api_key,
        "with_people": "5256",  # Christopher Nolan's TMDb person ID
        "sort_by": "vote_average.desc",
        "vote_count.gte": 1000  # Minimum vote count threshold
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        movies = response.json()["results"]
        if movies:
            highest_rated_movie = movies[0]
            title = highest_rated_movie["title"]
            rating = highest_rated_movie["vote_average"]
            return title, rating
        else:
            return None, None
    else:
        print("Failed to fetch movie data. Status code:", response.status_code)
        return None, None

# Replace "YOUR_API_KEY" with your actual TMDb API key
api_key = "978e5c7a7fe49a1a6496279638088e9c"
title, rating = fetch_highest_rated_nolan_movie(api_key)

if title and rating:
    print("Highest-rated Christopher Nolan movie:")
    print("Title:", title)
    print("Rating:", rating)
else:
    print("No Christopher Nolan movies found or an error occurred.")
