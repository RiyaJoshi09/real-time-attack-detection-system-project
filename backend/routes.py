from flask import Blueprint, request, jsonify
import json, datetime
from detection_engine import detect_attack
from datetime import datetime, timezone

routes_blueprint = Blueprint('routes', __name__)
attack_logs = []

# Define the route normally, but don't emit yet
def create_routes(socketio):
    @routes_blueprint.route('/analyze', methods=['POST'])
    def analyze():
        data = request.get_json()
        payload = json.dumps(data)
        matches = detect_attack(payload)

        if matches:
            log = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "ip": request.remote_addr,
                "payload": data,
                "patterns": matches
            }
            attack_logs.append(log)
            socketio.emit('attack_alert', log)
            return jsonify({"status": "attack_detected", "details": log}), 200

        return jsonify({"status": "clean"}), 200

    @routes_blueprint.route('/logs', methods=['GET'])
    def get_logs():
        return jsonify(attack_logs)
