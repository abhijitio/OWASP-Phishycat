from flask import Flask, request

# socket flassk add
#from flask_socketio import SocketIO

# end

app = Flask(__name__)

# socket flassk add
#app.config['SECRET_KEY'] = 'secret!'
#socketio = SocketIO(app)
# end

from app import views


# socket flassk add

#if __name__ == '__main__':
#    socketio.run(app)

# end
