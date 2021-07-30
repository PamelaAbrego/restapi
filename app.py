from flask import Flask
from flask_restful import Api
from resource.contenido import contenido
from resource.trainers import trainers

app = Flask(__name__)
api = Api(app)

api.add_resource(contenido, "/contenido/<string:categoria>")
api.add_resource(trainers, "/trainers/<string:categoria>")

if __name__ == "__main__":
    app.run(debug=True)