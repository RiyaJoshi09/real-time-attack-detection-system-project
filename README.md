## 🛡️ Project Description

The **Real-Time Web App Attack Detection System** is a Flask + React-based platform that detects and alerts on suspicious web traffic in real time. It uses regex-based pattern matching to identify common attack types like XSS, SQL Injection, and command injection.

This tool is intended for developers or security teams who want lightweight, extensible threat monitoring for their web applications.


## 🎯 Features

- Real-time HTTP payload analysis
- Regex-based detection rules (no ML required)
- WebSocket alerts to a live dashboard
- Log viewer and analytics
- REST API for integration with other tools


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


## 📄 License
Apache License 2.0. See `LICENSE` file for details.
