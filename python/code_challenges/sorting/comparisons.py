
new_movies = []


movies = [
  {
    "title": "Beetlejuice",
    "year": 1988,
    "genres": ["Comedy", "Fantasy"],
  },
  {
    "title": "The Cotton Club",
    "year": 1984,
    "genres": ["Crime", "Drama", "Music"],
  },
  {
    "title": "The Shawshank Redemption",
    "year": 1994,
    "genres": ["Crime", "Drama"],
  },
  {
    "title": "Crocodile Dundee",
    "year": 1986,
    "genres": ["Adventure", "Comedy"],
  },
  {
    "title": "Valkyrie",
    "year": 2008,
    "genres": ["Drama", "History", "Thriller"],
  },
  {
    "title": "Ratatouille",
    "year": 2007,
    "genres": ["Animation", "Comedy", "Family"],
  },
  {
    "title": "City of God",
    "year": 2002,

    "genres": ["Crime", "Drama"],
  },
  {
    "title": "Memento",
    "year": 2000,

    "genres": ["Mystery", "Thriller"],
  },
  {
    "title": "The Intouchables",
    "year": 2011,

    "genres": ["Biography", "Comedy", "Drama"],
  },
  {
    "title": "Stardust",
    "year": 2007,
    "genres": ["Adventure", "Family", "Fantasy"],
  },
]

def sort_movies_by_title(movies_list):
    sorted_movies = sorted(movies_list, key=lambda movie: movie.get("title", "").lstrip("The "))
    return [movie["title"] for movie in sorted_movies if "title" in movie]


def sort_movies_by_year(movies_list):
    movies_by_year = sorted(movies_list, key=lambda movie: (movie.get("year", 0), movie.get("title", "").lstrip("The ")), reverse=True)
    return [movie["title"] for movie in movies_by_year if "title" in movie]


movie_by_year = sort_movies_by_year(movies)
print(movie_by_year)

sorted_movies = sort_movies_by_title(movies)
print(sorted_movies)



