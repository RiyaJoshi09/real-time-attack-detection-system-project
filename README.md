## 🛡️ Project Description

The **Real-Time Web App Attack Detection System** is a Flask + React-based platform that detects and alerts on suspicious web traffic in real time. It uses regex-based pattern matching to identify common attack types like XSS, SQL Injection, and command injection.

This tool is intended for developers or security teams who want lightweight, extensible threat monitoring for their web applications.

---

## 🎯 Features

- Real-time HTTP payload analysis
- Regex-based detection rules (no ML required)
- WebSocket alerts to a live dashboard
- Log viewer and analytics
- REST API for integration with other tools

---

## 🧱 Tech Stack

### Backend:
- Python (Flask)
- Flask-SocketIO
- Regex pattern matching

### Frontend:
- React.js
- Socket.IO Client
- Tailwind CSS (or Material UI)
- Chart.js (optional)

### Optional:
- Docker / Docker Compose
- Nginx (reverse proxy)
- Redis (for scalability or async alerts)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourname/real-time-attack-detection.git
cd real-time-attack-detection
```

### 2. Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm start
```

> Frontend will start on http://localhost:3000 and connect to the Flask backend on http://localhost:5000

---

## 🧪 API Endpoints

### Analyze a Request
```
POST /analyze
Content-Type: application/json
{
    "url": "/login",
    "params": {
        "username": "admin",
        "password": "' OR 1=1 --"
    }
}
```

### Get Logs
```
GET /logs
```

---

## 🗂 Directory Structure
```
real-time-attack-detection/
├── backend/
│   ├── app.py
│   ├── detection_engine.py
│   ├── socket_events.py
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   └── services/
│   └── public/
└── docker-compose.yml
```

---

## 🔐 Security Notes
- All traffic should be encrypted using HTTPS.
- Consider IP whitelisting or token auth for the `/analyze` endpoint.
- Logs can be stored in a database for persistence and auditing.

---

## 📄 License
Appache 2.0 License. See `LICENSE` file for details.
