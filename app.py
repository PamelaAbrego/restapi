from flask import Flask
from flask_restful import Api
from resources.person_resource import Person
from resources.contenido import contenido

app = Flask(__name__)
api = Api(app)

api.add_resource(Person, "/all_person")
api.add_resource(contenido, "/contenido/<string:categoria>")


if __name__ == "__main__":
    app.run(debug=True)