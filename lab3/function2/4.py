def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]
print(movies_by_category(movies, "Romance"))