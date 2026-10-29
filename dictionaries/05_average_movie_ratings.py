# Assignment
# Given a list of movie titles and corresponding lists of rating scores, build a
# dictionary that associates each movie title with its list of ratings. Then,
# calculate and display the average rating for each movie formatted to one
# decimal place.
#
# Solution

from statistics import mean

# Movie titles and their corresponding lists of ratings.
movies = [
    'Monty Python and the Holy Grail',
    "Monty Python' s Life of Brian",
    "Monty Python' s Meaning of Life",
    'And Now For Something Completely Different',
]
grail_ratings = [9, 10, 9.5, 8.5, 3, 7.5, 8]
brian_ratings = [10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9]
life_ratings = [7, 6, 5]
different_ratings = [6, 5, 6, 6]

ratings_list = [grail_ratings, brian_ratings, life_ratings, different_ratings]

# A dictionary mapping each movie title to its list of numeric ratings.
ratings: dict[str, list[float]] = {}

# Associate each movie title with its corresponding rating list by index.
for movie_index in range(len(movies)):
    ratings[movies[movie_index]] = ratings_list[movie_index]

# Calculate and display the arithmetic mean rating for each movie.
for movie in ratings:
    average_rating = mean(ratings[movie])
    print(f"The movie '{movie}' has an average rating of {average_rating:.1f}")
