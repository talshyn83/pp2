def is_good_movie(movie):
    return movie["imdb"] > 5.5
print(is_good_movie(movies[0]))