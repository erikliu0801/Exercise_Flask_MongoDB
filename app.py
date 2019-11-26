from flask import Flask, request
from flask_restplus import Resource, Api

## db/orm connect
# from flask_peewee.db import Database
# app.config.from_object('config.Configuration')
# db = Database(app)
# Set up the cache, a task queue, etc.

app = Flask(__name__)
api = Api(app)

todos = {}

@api.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

if __name__ == '__main__':
    app.run(port=8787)