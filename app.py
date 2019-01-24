from flask import Flask
from flask_restful import Resource, reqparse, Api

app = Flask(__name__)
api = Api(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['PROPAGATE_EXCEPTIONS'] = True
#
#from base import Movies, db
#db.init_app(app)
#app.app_context().push()
#db.create_all()

class Movies_List(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('director', type=str, required=False, help='Director of the movie')
    parser.add_argument('genre', type=str, required=False, help='Genre of the movie')
    parser.add_argument('collection', type=int, required=True, help='Gross collection of the movie')
    
#    def get(self, movie):
#        item = Movies.find_by_title(movie)
#        if item:
#            return item.json()
#        return {'Message': 'Movie is not found'}
#    
#    def post(self, movie):
#        if Movies.find_by_title(movie):
#            return {' Message': 'Movie with the  title {} already exists'.format(movie)}
#        args = Movies_List.parser.parse_args()
#        item = Movies(movie, args['director'], args['genre'], args['collection'])
#        item.save_to()
#        return item.json()
#        
#    def put(self, movie):
#        args = Movies_List.parser.parse_args()
#        item = Movies.find_by_title(movie)
#        if item:
#            item.collection = args['collection']
#            item.save_to()
#            return {'Movie': item.json()}
#        item = Movies(movie, args['director'], args['genre'], args['collection'])
#        item.save_to()
#        return item.json()
#            
#    def delete(self, movie):
#        item  = Movies.find_by_title(movie)
#        if item:
#            item.delete_()
#            return {'Message': '{} has been deleted from records'.format(movie)}
#        return {'Message': '{} is already not on the list'.format()}
    
class All_Movies(Resource):
    def get(self):
#        return {'Movies': list(map(lambda x: x.json(), Movies.query.all()))}
        return "test"
    
users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

class UserAll(Resource):
    def get(self):
        return users

    
api.add_resource(All_Movies, '/')
api.add_resource(Movies_List, '/<string:movie>')
api.add_resource(User, "/user/<string:name>")
api.add_resource(UserAll, "/user")

if __name__=='__main__':
    
    app.run(debug=True)
