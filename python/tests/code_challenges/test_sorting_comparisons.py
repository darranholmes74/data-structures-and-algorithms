from code_challenges.sorting.comparisons import sort_movies_by_title, sort_movies_by_year, movies
# from code_challenges.sorting.movies import movies

def test_sort_movie_by_year():
    expected = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]
    assert sort_movies_by_year(movies) == expected
# Expected test output of test #2
def test_sort_movie_by_title():
    expected = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"];
    assert sort_movies_by_title(movies) == expected
