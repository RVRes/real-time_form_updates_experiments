from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

field_status = {}


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('update_field')
def update_field(data):
    field_name = data['field_name']
    user_id = data['user_id']
    if field_status.get(field_name) is None:
        field_status[field_name] = user_id
        socketio.emit('field_updated',
                      {'field_name': field_name, 'user_id': user_id})


if __name__ == '__main__':
    socketio.run(app)
