from core.pyba_logic import PybaLogic

class TrainersLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getTrainerCategoria(self, categoria):
        database = self.databaseObj
        sql = f"SELECT * FROM trainers where categoria = '{categoria}';"
        result = database.executeQuery(sql)
        return result

