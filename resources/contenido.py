from flask_restful import Resource, reqparse
from logic.contenido_logic import ContenidoLogic

class contenido(Resource):
    def __init__(self):
        self.contenido_put_args = self.createParser()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("categoria", type=str, help="categoria del contenido")
        args.add_argument("nombre", type=str, help="nombre")
        args.add_argument("descripcion", type=str, help="descripcion")
        args.add_argument("fecha", type=str, help="fecha")
        args.add_argument("autor", type=str, help="autor")
        args.add_argument("enlace", type=str, help="enlace")
        return args

    def post(self, id):
        logic = ContenidoLogic()
        result = logic.getContenidoId(id)
        if len(result) == 0:
            return {}
        return result[0], 200
    
    def get(self, categoria):
        logic = ContenidoLogic()
        result = logic.getContenidoCategoria(categoria)
        if len(result) == 0:
            return {}
        return result, 200
