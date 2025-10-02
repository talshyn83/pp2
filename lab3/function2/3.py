def movies_above_5_5(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]
print(movies_above_5_5(movies))