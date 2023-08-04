from flask import Flask
from flask_restful import Api,Resource,reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        data = pd.read_csv('users.csv')
        data = data.to_dict('records')
        return {'data':data},200
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name',required=True)
        parser.add_argument('age',required=True)
        parser.add_argument('city',required=True)
        args=parser.parse.args()

        data = pd.read_csv('users.csv')

        new_data = pd.DataFrame({
            'name' : [args['name']],
            'age'  : [args['age']],
            'city' : [args['city']]
        })

        data = data.append(new_data,ignore_index=True)
        return {'data' : new_data.todict('records')},201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name',required=True)
        args=parser.parse_args()

        data = pd.read_csv('users.csv')

        data = data[data['name'] != args[name]]

        data.to_csv('C:/Users/ISHITA SWAMI/Desktop/users.csv',index=False)
        return {'message':'Record deleted successfully.'},200

api.add_resource(Users,'/users')
if __name__ == '__main__':
    app.run()
        