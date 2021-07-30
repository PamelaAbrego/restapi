from flask_restful import Resource, reqparse
from logic.trainers_logic import TrainersLogic

class trainers(Resource):
    def __init__(self):
        self.tip_put_args = self.createParser()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("categoria", type=str, help="categoria del tip")
        args.add_argument("nombre", type=str, help="nombre")
        args.add_argument("descripcion", type=str, help="descripcion")
        args.add_argument("enlace", type=str, help="enlace")
        return args
    
    def get(self, categoria):
        logic = TrainersLogic()
        result = logic.getTrainerCategoria(categoria)
        if len(result) == 0:
            return {}
        return result, 200
