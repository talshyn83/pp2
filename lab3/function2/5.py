def average_imdb_score(movies):
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)
print(average_imdb_score(movies))