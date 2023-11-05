import json

from flask import Flask, jsonify, request
from model.twit import Twit
from  model.comments import Comment

twits = []
comments = []


app = Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Twit):
            return {'body': obj.body, 'auther': obj.author}
        else:
            return super().default(obj)

app.json_encoder = CustomJSONEncoder


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})


@app.route('/twit', methods=['POST'])
def create_twit():
    '''{"body": "Hello world", "author": "@aqaguy"}
    '''
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['body'])
    twits.append(twit)
    return jsonify({'status': 'success'})
@app.route('/twit', methods=['GET'])
def read_twits():
    return jsonify({'twits': twits})

@app.route('/comments', methods=['POST'])
def creat_comments():
    '''{"comments": "Hi, guys", "author": "@sasha"}
    '''
    comments_json = request.get_json()
    comments = Comment(comments_json['comments'], comments_json['comments'])
    comments.append(comments)
    return jsonify({'status': 'success'})
@app.route('/comments', methods=['POST'])
def read_comments():
    return jsonify({'comments': 'comments'})




if __name__ == '__main__':
    app.run(debug=True)

