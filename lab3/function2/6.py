def average_imdb_score_by_category(movies, category):
    category_movies = [movie for movie in movies if movie["category"].lower() == category.lower()]
    if category_movies:
        total_score = sum(movie["imdb"] for movie in category_movies)
        return total_score / len(category_movies)
    return 0
print(average_imdb_score_by_category(movies, "Romance"))