from flask import Flask
from flask_socketio import SocketIO
from routes import routes_blueprint, create_routes
from socket_events import register_socket_events
from config import Config
import eventlet
import os

eventlet.monkey_patch()

app = Flask(__name__)
app.config.from_object(Config)

socketio = SocketIO(app, cors_allowed_origins=Config.CORS_ALLOWED_ORIGINS)

# Register routes and WebSocket events
create_routes(socketio)
app.register_blueprint(routes_blueprint)
register_socket_events(socketio)

if __name__ == '__main__':
    # Get host and port from environment variables (Docker-friendly)
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.environ.get("FLASK_RUN_PORT", 5000))
    
    # Run the app with eventlet
    socketio.run(app, host=host, port=port, debug=Config.DEBUG)