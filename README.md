# HTTP-Chat-Application-between-2-VMs
Continuous Assessment

HTTP Chat Application Assignment
--------------------------------
Student Names:
D.M.M.V Devinda
M.D.H.R Karanayaka
E.K Amarasinghe
J.W.B.R Mihiranga
G.K.D Nayanajith

1. Overview
   This is a secure (HTTPS) chat application hosted on Google Cloud using Docker.
   It uses Flask (Python) for the backend and HTML/AJAX for the frontend.

2. Architecture
   [Client Browser] <--- HTTPS (Port 443) ---> [Google Cloud VM] <--- [Docker Container]

3. Prerequisites
   - Google Cloud Account
   - Docker installed on VM

4. How to Run
   1. Navigate to the project folder.
   2. Build the docker image: "sudo docker build -t secure-chat ."
   3. Run the container: "sudo docker run -d -p 443:443 secure-chat"
   4. Access via browser: https://<VM_EXTERNAL_IP>

5. API Endpoints
   - GET /            : Loads the UI
   - POST /send       : Sends a message JSON {username, message}
   - GET /get_messages: Returns JSON list of messages

6. Files Included
   - app.py
   - templates/index.html
   - Dockerfile
   - requirements.txt
