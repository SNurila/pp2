def high_imdb(movies):
    return movies["imdb"] > 5.5

movie_1 = {
    "name": "Bride Wars",
    "imdb": 5.4,
    "category": "Romance"
}

movie_2 = {
"name": "Love",
"imdb": 6.0,
"category": "Romance"
}

movie_3 = {
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
}


print(high_imdb(movie_1))
print(high_imdb(movie_2))
print(high_imdb(movie_3))