import csv
import math
from movie_structure import Movie


class MoviesInfo:

    movies_list = []

    def __init__(self, path):

        with open(path, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                self.movies_list.append(Movie(**row))

    def filter_by_genre(self, genre):

        filter_movies = [movie.rating
                         for movie in self.movies_list if genre.capitalize() in movie.genres]
        if filter_movies:
            print(f"Movies Found against \"{genre.capitalize()}\" genre:", len(
                filter_movies))
            print(f"Average mean rating of \"{genre.capitalize()}\" genre:", round(
                sum(filter_movies)/len(filter_movies), 2))
        else:
            print("No movies found against this genre.")

    def movie_ratings(self, year):

        filter_movies = [
            movie for movie in self.movies_list if movie.startYear == year]
        if filter_movies:
            highest_rating_movie = max(
                filter_movies, key=lambda x: x.rating)
            lowest_rating_movie = min(filter_movies, key=lambda x: x.rating)
            print(
                f"Highest rated movie in {year}: {highest_rating_movie.rating} - {highest_rating_movie.originalTitle}")
            print(
                f"Lowest rated movie in {year} {lowest_rating_movie.rating} - {lowest_rating_movie.originalTitle}")
            print(f"Average mean minutes for year, {year}:", round(
                sum([movie.runtimeMinutes for movie in filter_movies])/len(filter_movies), 2))
        else:
            print("No movies data found against this year.")

    def movie_votes(self, year):

        def get_votes(movie):
            return movie.numVotes

        filter_movies = [
            movie for movie in self.movies_list if movie.startYear == year]
        if filter_movies:
            filter_movies.sort(key=get_votes, reverse=True)
        else:
            print("No movies data found against this year.")

        votes_per_smily = math.ceil(filter_movies[0].numVotes/80)
        for movie in filter_movies[:10]:
            print(
                f"{movie.originalTitle} - {'😀' * int(math.ceil(movie.numVotes/votes_per_smily))} - {movie.numVotes}")
