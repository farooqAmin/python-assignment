import math
import os
import argparse
import pdb
from dotenv import load_dotenv
from datetime import date

from file_reader import MoviesInfo


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
    movies = MoviesInfo(file_path)

    if args.Genre:
        movies.filter_by_genre(args.Genre)

    if args.Rating:
        movies.movie_ratings(args.Rating)

    if args.Votes:
        movies.movie_votes(args.Votes)
