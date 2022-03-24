import os
import pdb
import argparse
from dotenv import load_dotenv

import file_reader


def validate_genre(value):
    print(value)
    return value


def validate_year(value):
    print(value)
    return value


if __name__ == '__main__':
    load_dotenv()

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-r", "--Retrieve", help="Display the highest rating and movie name, lowest rating and movie name, and average runtime minutes", type=validate_year)

    parser.add_argument(
        "-g", '--Genre', help="Display the number of movies and the mean rating for specified genre.", type=validate_genre)

    parser.add_argument(
        "-v", "--Votes", help="For a given year print the top ten highest rated movies (using numVotes)", type=validate_year)

    args = parser.parse_args()

    # pdb.set_trace()

    file_path = os.getenv('FILE')
    movies = file_reader.readFile(file_path)

    if args.Genre:
        print("Displaying Output as: % s" % args.Genre)

    if args.Retrieve:
        print("Displaying Output as: % s" % args.Retrieve)

    if args.Votes:
        print("Displaying Output as: % s" % args.Votes)

    # data = []
    # for movie in movies:
    #     print(movie['startYear'])
    # data.append(Movie(**movie))
    # pdb.set_trace()
