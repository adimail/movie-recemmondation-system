function fetchMovies() {
    const directorName = document.getElementById("directorName").value;
    const apiKey = "978e5c7a7fe49a1a6496279638088e9c"; // Replace with your TMDb API key
    const apiUrl = `https://api.themoviedb.org/3/search/person?api_key=${apiKey}&query=${directorName}`;
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        if (data.results.length > 0) {
          const director = data.results[0];
          const directorId = director.id;
          const movieUrl = `https://api.themoviedb.org/3/discover/movie?api_key=${apiKey}&with_cast=${directorId}&sort_by=vote_average.desc`;
  
          fetch(movieUrl)
            .then(response => response.json())
            .then(movieData => {
              if (movieData.results.length > 0) {
                const movies = movieData.results.slice(0, 30); // Display only top 30 movies
                let output = "<h2>Top Movies:</h2>";
                output += `<div><img src="https://image.tmdb.org/t/p/w200/${director.profile_path}" alt="${director.name}"></div>`; // Display director's image
                output += "<ul>";
                for (let i = 0; i < movies.length; i++) {
                  const movie = movies[i];
                  output += `<li>${movie.title} - Rating: ${movie.vote_average}</li>`;
                }
                output += "</ul>";
                document.getElementById("output").innerHTML = output;
              } else {
                document.getElementById("output").innerHTML = "No movies found for this director.";
              }
            })
            .catch(error => {
              document.getElementById("output").innerHTML = "Error fetching movie data.";
            });
        } else {
          document.getElementById("output").innerHTML = "Director not found.";
        }
      })
      .catch(error => {
        document.getElementById("output").innerHTML = "Error fetching director data.";
      });
}
  