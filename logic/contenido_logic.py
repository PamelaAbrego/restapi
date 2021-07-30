from core.pyba_logic import PybaLogic

class ContenidoLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getContenidoCategoria(self, categoria):
        database = self.databaseObj
        sql = f"SELECT * FROM contenido where categoria = '{categoria}';"
        result = database.executeQuery(sql)
        return result

