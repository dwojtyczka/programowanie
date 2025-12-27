import csv
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Movie:
    def __init__(self, id, title, genres):
        self.id = id
        self.title = title
        self.genres = genres

class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp

class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Movies(Resource):
    def get(self):
        data_list = []
        try:
            with open('data/movies.csv', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    if len(row) >= 3:
                        obj = Movie(row[0], row[1], row[2])
                        data_list.append(obj.__dict__)
            return data_list
        except FileNotFoundError:
            return {"error": "Brak pliku movies.csv"}, 404

class Links(Resource):
    def get(self):
        data_list = []
        try:
            with open('data/links.csv', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    if len(row) >= 3:
                        obj = Link(row[0], row[1], row[2])
                        data_list.append(obj.__dict__)
            return data_list
        except FileNotFoundError:
            return {"error": "Brak pliku links.csv"}, 404

class Ratings(Resource):
    def get(self):
        data_list = []
        try:
            with open('data/ratings.csv', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                count = 0
                for row in reader:
                    if len(row) >= 4:
                        obj = Rating(row[0], row[1], row[2], row[3])
                        data_list.append(obj.__dict__)
                        count += 1
                        if count >= 100: break # Limit dla wydajności
            return data_list
        except FileNotFoundError:
            return {"error": "Brak pliku ratings.csv"}, 404

class Tags(Resource):
    def get(self):
        data_list = []
        try:
            with open('data/tags.csv', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    if len(row) >= 4:
                        obj = Tag(row[0], row[1], row[2], row[3])
                        data_list.append(obj.__dict__)
            return data_list
        except FileNotFoundError:
            return {"error": "Brak pliku tags.csv"}, 404

api.add_resource(HelloWorld, '/')
api.add_resource(Movies, '/movies')
api.add_resource(Links, '/links')
api.add_resource(Ratings, '/ratings')
api.add_resource(Tags, '/tags')

if __name__ == '__main__':
    app.run(debug=True)
