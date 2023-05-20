import requests

API_KEY = "YOUR_TMDB_API_KEY"

def fetch_movies():
    url = f"https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "sort_by": "vote_average.desc",
        "with_people": "5256",  # 5256 is the person ID for Christopher Nolan
        "page": 1
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data["results"][:3]  # Retrieve only the top 3 movies

def main():
    movies = fetch_movies()

    for movie in movies:
        title = movie["title"]
        release_year = movie["release_date"][:4]
        vote_average = movie["vote_average"]
        print(f"{title} ({release_year}) - Vote Average: {vote_average}")

if __name__ == "__main__":
    main()
