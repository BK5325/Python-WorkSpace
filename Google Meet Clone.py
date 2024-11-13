from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

@socketio.on("join_room")
def join_room(data):
    room = data["room"]
    socketio.join_room(room)
    emit("joined_room", {"message": "Joined room successfully"}, room=room)

@socketio.on("leave_room")
def leave_room(data):
    room = data["room"]
    socketio.leave_room(room)
    emit("left_room", {"message": "Left room successfully"}, room=room)