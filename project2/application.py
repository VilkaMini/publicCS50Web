import os

from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

channelList = []
currentChannel = []
username = []
holder = {}
package = {}

@app.route("/")
def index():
    print("\n")
    print(channelList)
    print("\n")
    print(currentChannel)
    print("\n")
    print(username)
    print("\n")
    print(holder)
    print("\n")
    package["holder"] = holder
    package["currentChannel"] = currentChannel
    package["username"] = username
    package["channelList"] = channelList
    return render_template("index.html")

@socketio.on('con')
def handle_con(con):
    emit('load', package)
    package.clear()
    print(con['data'])

@socketio.on('user')
def userReg(uname):
    username.append(uname["username"])

@socketio.on('channelToServer')
def channelAppend(ch):
    channelList.append(ch['channel'])
    holder[ch['channel']] = []

@socketio.on('message')
def handle_message(msg):
    if not currentChannel:
        channelList.append("Index")
        currentChannel.append('Index')
        holder['Index'] = []
    message = msg["time"] + " " + msg["username"] + ": " + msg["message"]
    holder[currentChannel[0]].append(message)
    if len(holder[currentChannel[0]]) > 100:
        holder[currentChannel[0]].pop(0)
    emit('chatMessage', message)

@socketio.on('join')
def on_join(data):
    room = data['room']
    currentChannel.clear()
    currentChannel.append(room)
    passer = holder[currentChannel[0]]
    emit('channelChange', passer)

if __name__ == "__main__":
    socketio.run(app)