
class Movie:
    total = 0

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.title_type = kwargs['titleType']
        self.original_title = kwargs['originalTitle']
        self.start_year = kwargs['startYear']
        self.runtime_minuntes = kwargs['runtimeMinutes']
        self.genres = kwargs['genres'].split(',')
        self.rating = float(kwargs['rating'])
        self.num_votes = kwargs['numVotes']

        Movie.add_movie()

    @classmethod
    def total_movies(cls):
        return cls.total

    @classmethod
    def add_movie(cls):
        cls.total += 1
