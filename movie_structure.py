
class Movie:
    total = 0

    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.titleType = kwargs['titleType']
        self.originalTitle = kwargs['originalTitle']
        self.startYear = kwargs['startYear']
        self.runtimeMinutes = 0 if(kwargs['runtimeMinutes'] == '\\N') else int(
            kwargs['runtimeMinutes'])
        self.genres = [] if(kwargs['genres'] ==
                            '\\N') else kwargs['genres'].split(',')
        self.rating = float(kwargs['rating'])
        self.numVotes = int(kwargs['numVotes'])

        Movie.add_movie()

    @classmethod
    def total_movies(cls):
        return cls.total

    @classmethod
    def add_movie(cls):
        cls.total += 1
