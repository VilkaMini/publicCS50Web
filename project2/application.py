import os

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('con')
def handle_con(con):
    print(con['data'])

@socketio.on('message')
def handle_message(msg):
    message = msg["time"] + " " + msg["username"] + ": " + msg["message"]
    emit('chat message', message)

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    print(data['room'])
    emit(username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit(username + ' has left the room.', room=room)










if __name__ == "__main__":
    socketio.run(app)