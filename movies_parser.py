import math
import os
import argparse
from dotenv import load_dotenv
from datetime import date

import file_reader


def validate_genre(value):
    if not value.isalpha():
        raise argparse.ArgumentTypeError("Argument value must be string.")
    return value


def validate_year(value):

    if(len(value) == 4):
        if not int(value) < 1890 and int(value) > date.today().year:
            raise argparse.ArgumentTypeError(
                f"Argument(year) should be between 1890 to {date.today().year}")
    else:
        raise argparse.ArgumentTypeError("Argument(year) is not a valid year.")

    return value


def filter_by_genre(movies, genre):

    filter_movies = [movie['rating']
                     for movie in movies if genre.capitalize() in movie['genres']]
    if filter_movies:
        print(f"Movies Found against \"{genre.capitalize()}\" genre:", len(
            filter_movies))
        print(f"Average mean rating of \"{genre.capitalize()}\" genre:", round(
            sum(filter_movies)/len(filter_movies), 2))
    else:
        print("No movies found against this genre.")


def movie_ratings(movies, year):

    filter_movies = [movie for movie in movies if movie['startYear'] == year]
    if filter_movies:
        highest_rating_movie = max(filter_movies, key=lambda x: x['rating'])
        lowest_rating_movie = min(filter_movies, key=lambda x: x['rating'])
        print(
            f"Highest rated movie in {year}: {highest_rating_movie['rating']} - {highest_rating_movie['originalTitle']}")
        print(
            f"Lowest rated movie in {year} {lowest_rating_movie['rating']} - {lowest_rating_movie['originalTitle']}")
        print(f"Average mean minutes for year, {year}:", round(
            sum([movie['runtimeMinutes'] for movie in filter_movies])/len(filter_movies), 2))
    else:
        print("No movies data found against this year.")


def get_votes(movie):
    return movie.get('numVotes')


def movie_votes(movies, year):
    filter_movies = [movie for movie in movies if movie['startYear'] == year]
    if filter_movies:
        filter_movies.sort(key=get_votes, reverse=True)
    else:
        print("No movies data found against this year.")

    votes_per_smily = math.ceil(filter_movies[0]['numVotes']/80)
    for movie in filter_movies[:10]:
        print(
            f"{movie['originalTitle']} - {'😀' * int(math.ceil(movie['numVotes']/votes_per_smily))} - {movie['numVotes']}")


if __name__ == '__main__':
    load_dotenv()  # for loading environment variables

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-r", "--Rating", help="Display the highest rating and movie name, lowest rating and movie name, and average runtime minutes", type=validate_year)

    parser.add_argument(
        "-g", '--Genre', help="Display the number of movies and the mean rating for specified genre.", type=validate_genre)

    parser.add_argument(
        "-v", "--Votes", help="For a given year print the top ten highest rated movies (using numVotes)", type=validate_year)

    args = parser.parse_args()

    file_path = os.getenv('FILE')
    movies = file_reader.readFile(file_path)

    if args.Genre:
        filter_by_genre(movies, args.Genre)

    if args.Rating:
        movie_ratings(movies, args.Rating)

    if args.Votes:
        movie_votes(movies, args.Votes)
