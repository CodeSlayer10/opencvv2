from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import requests

db_connect = create_engine("sqlite:///Project_Alert.db")
app = Flask(__name__)
api = Api(app)




class UpdateBool(Resource):
    @staticmethod
    def get(self, id, Data):
        conn = db_connect.connect()
        command = "UPDATE isHuman SET {} where id='%s'".format(Data) % id
        query1 = conn.execute(command)
        return {id: [i for i in query1.cursor.fetchall()]}


class ShowId(Resource):
    @staticmethod
    def get():
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select * from isHuman ")  # This line performs query and returns json result
        return {'Id': [i[1] for i in query.cursor.fetchall()]}


class ShowBool(Resource):
    @staticmethod
    def get():
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select * from isHuman ")  # This line performs query and returns json result
        return {'bool': [i[0] for i in query.cursor.fetchall()]}


api.add_resource(UpdateBool, '/ID/<string:id>/<string:Data>')  # Route_1
api.add_resource(ShowId, '/SID')  # Route_2
api.add_resource(ShowBool, '/SB')  # Route_3
if __name__ == '__main__':
    app.run(port='5002')