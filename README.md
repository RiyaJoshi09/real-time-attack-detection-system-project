# 🚨 Real-Time Web App Attack Detection System

A real-time security monitoring system that detects and logs suspicious payloads submitted to a web application. The project features a **Flask-based backend** and a **React + Material UI frontend**, with **WebSocket-based real-time alerts** for detected attacks.

---

## 📦 Features

* 🔍 Detects common web attacks (XSS, SQL Injection, Directory Traversal, etc.)
* ⚡ Real-time attack alerts using **WebSockets (Socket.IO)**
* 📊 Attack log table with **IP address**, **payload**, and **timestamp**
* 🚨 Visual **alert banner** for new attack detection
* 🌐 RESTful API for **submitting and retrieving logs**
* 🐳 **Dockerized backend** for easy deployment

---

## 🛠️ Technologies Used

### 🖙 Backend

* Python + Flask
* Flask-SocketIO
* Regex-based attack detection engine
* Docker

### 🔼 Frontend

* React
* Material UI
* Axios
* Socket.IO Client

---

## 📁 Project Structure

```
real-time-attack-detection-system/
├── backend/
│   ├── app.py
│   ├── detection_engine.py
│   ├── routes.py
│   ├── socket_events.py
│   ├── config.py
│   ├── Dockerfile
│   └── test_app.py
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── AlertBanner.js
│   │   │   ├── AttackLogsTable.js
│   │   │   ├── Header.js
│   │   │   └── Footer.js
│   │   ├── pages/
│   │   │   ├── Dashboard.js
│   │   │   └── NotFound.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── api.js
│   └── package.json
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/real-time-attack-detection-system.git
cd real-time-attack-detection-system
```

---

## 🐍 Backend Setup (Flask)

### ⚖️ Prerequisites

* Python 3.9+
* pip

### ▶️ Run Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Or run with Docker:

```bash
cd backend
docker build -t attack-detector-backend .
docker run -p 5000:5000 attack-detector-backend
```

---

### 📬 Test API

#### Clean request:

```bash
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"input": "hello"}'
```

#### Malicious request:

```bash
curl -X POST http://localhost:5000/scan \
  -H "Content-Type: application/json" \
  -d '{"input": "<script>alert(1)</script>"}'
```

---

## ⚛️ Frontend Setup (React + Material UI)

### ⚖️ Prerequisites

* Node.js
* npm

### ▶️ Run Frontend

```bash
cd frontend
npm install
npm start
```

> 🔗 Make sure the backend is running at [http://localhost:5000](http://localhost:5000)

---

## 🔬 Running Backend Tests

```bash
cd backend
pytest
```

---

## 📸 Demo

> *(Optional: Add a screen recording or image here)*

---

## 📌 Environment Variables

Create a `.env` file in the frontend root directory:

```
REACT_APP_API_URL=http://localhost:5000
```

---

## 🔮 Future Scope
* 💾 Persistent storage with a database

* 📊 Charts and statistics (e.g. attack frequency)

* 🔐 Authentication and role-based access control

* 🌍 IP geolocation of attackers

* 📧 Email or Slack alerts

* ☁️ Kubernetes deployment with full observability

* 🔁 Log export options (CSV, JSON)

* 🧠 ML-based anomaly detection engine
