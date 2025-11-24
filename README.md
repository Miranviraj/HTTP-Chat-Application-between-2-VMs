# HTTP-Chat-Application
This is a continuous assessment to create an HTTP chat application between 2 VMs using Google Cloud/AWS.

> **Module:** Designing & Developing Applications on Cloud (IT4118)  
> **Assignment:** HTTP Chat Application (Continuous Assessment)  
> **Platform:** Google Cloud Platform (GCP)

---

## 🎓 Student Contributors

| Student Name | Registration ID |
| :--- | :--- |
| **D.M.M.V Devinda** | `IT_IFLS_001/B003/0005` |
| **M.D.H.R Karanayaka** | `IT_IFLS_001/B003/0024` |
| **E.K. Amarasinghe** | `IT_IFLS_001/B003/0002` |
| **J.B.W.R Mihiranga** | `IT_IFLS_001/B003/0031` |
| **G.K.D Nayanajith** | `IT_IFLS_001/B003/0033` |

---

## 🚀 1. Project Overview

This project implements a robust **Hybrid Communication System** deployed on Google Cloud. Unlike traditional single-protocol chat apps, this solution offers two simultaneous modes of communication between Virtual Machines:

1.  **🌐 Web Mode (HTTPS - Port 443):** A secure, browser-based chat interface powered by **Flask** and **Docker**.
2.  **💻 Terminal Mode (TCP - Port 5000):** A low-latency, raw socket chat for direct command-line communication.

---

## 🏗️ 2. System Architecture

The system follows a **Client-Server** model hosted on a GCP Compute Engine instance with a **Static IP**. It handles traffic on two distinct ports simultaneously.

---

## 📋 3. Prerequisites

Before running the application, ensure the following environment is configured:

✅ Google Cloud Account with Compute Engine enabled.

✅ Two Virtual Machines (Ubuntu 22.04 LTS).

✅ Docker & Python 3 installed on the Server VM.

✅ Static External IP reserved for the Server VM.

✅ Firewall Rules Configured:

- allow-https-chat (Target: All instances | Range: 0.0.0.0/0 | Port: tcp:443)
- allow-socket-chat (Target: All instances | Range: 0.0.0.0/0 | Port: tcp:5000)

---

## 📂 4. Project File Structure

/chat-app
├── app.py              # 🌐 Web Server Logic (Flask)<br>
├── server.py           # 💻 Terminal Server Logic (Sockets)<br>
├── client.py           # 💻 Terminal Client Logic (Sockets)<br>
├── Dockerfile          # 🐳 Container instructions<br>
├── requirements.txt    # 📦 Python Dependencies<br>
├── cert.pem, key.pem   # 🔒 SSL Certificates<br>
└── /templates<br>
    └── index.html      # 🎨 Frontend UI

---

## ⚙️ 5. How to Run (Step-by-Step)
To utilize the Dual-Mode capability, follow these steps on the Server (VM1).

🅰️ Server-Side Setup (VM1)

1. Start the Web Server (Background). This runs the HTTPS web app inside a Docker container.
```
# Build the image
sudo docker build -t secure-chat .

# Run in detached mode (-d)
sudo docker run -d -p 443:443 secure-chat
```


2. Start the Terminal Server (Foreground). This runs the raw TCP socket listener in the main terminal window.
```
#Start the socket server <br>
python3 server.py
```
> You should see: "Server listening on port 5000..."

🅱️ Client-Side Usage (VM2 or Desktop)

You can now connect using either method (or both at the same time!).

Option 1: Web Chat (Browser) 🌐

1. Open Chrome, Edge, or Safari.
2. Navigate to: https://34.131.165.237.
3. Note: Accept the security warning (caused by self-signed certificates).

Option 2: Terminal Chat (Command Line) 💻

1. SSH into your Client VM (VM2).
2. Ensure client.py has the correct SERVER_IP inside the code.
3. Run the script:
```
python3 client.py
```
4. Type messages directly into the terminal!

---

## 🔌 6. Web API Endpoints
For the browser-based application, the following endpoints are exposed:

| **HTTP Method** | **Endpoint** | **Function** |
| :--- | :--- | :--- |
| **GET** | / | Renders the Chat UI (index.html). |
| **POST** | /send | "Accepts JSON {username, message} to save chat data." |
| **GET** | /get_messages | Returns the chat history as a JSON list. |

---
