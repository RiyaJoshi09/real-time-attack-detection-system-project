from flask import Flask
from flask_socketio import SocketIO
from routes import routes_blueprint, create_routes
from socket_events import register_socket_events
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

socketio = SocketIO(app, cors_allowed_origins=Config.CORS_ALLOWED_ORIGINS, async_mode='threading')


# Register routes and WebSocket events
create_routes(socketio)  # attach socketio to routes
app.register_blueprint(routes_blueprint)
register_socket_events(socketio)

if __name__ == '__main__':
    socketio.run(app, debug=Config.DEBUG)
