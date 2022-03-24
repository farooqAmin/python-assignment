import csv


def readFile(path):
    data = []
    with open(path, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            data.append({
                'id': row['id'],
                'titleType': row['titleType'],
                'originalTitle': row['originalTitle'],
                'startYear': row['startYear'],
                'runtimeMinutes':  0 if(row['runtimeMinutes'] == '\\N') else int(row['runtimeMinutes']),
                'genres': [] if(row['genres'] == '\\N') else row['genres'].split(','),
                'rating': float(row['rating']),
                'numVotes': int(row['numVotes'])
            })

    return data
