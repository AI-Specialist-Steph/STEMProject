from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET'] = "teachdentA$$678"
socketio = SocketIO(app, cors_allowed_origins="*")



@socketio.on('texts')
def handle_texts(texts):
    print("notification: " + texts)
    if texts != "User online":
        send(texts, broadcast=True)

@app.route('/t')
def design():
    return render_template("design.html")

if __name__ == "__main__":
    socketio.run(app,host="localhost")
