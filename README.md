# HTTP-Chat-Application
This is a continuous assessment to create an HTTP chat application between 2 VMs using Google Cloud/AWS.

HTTP Chat Application Assignment
--------------------------------
Student Names:
- D.M.M.V Devinda - IT_IFLS_001/B003/0005
- M.D.H.R Karanayaka - IT_IFLS_001/B003/0024
- E.K. Amarasinghe - IT_IFLS_001/B003/0002
- J.B.W.R Mihiranga - IT_IFLS_001/B003/0031
- G.K.D Nayanajith - IT_IFLS_001/B003/0033
<br>

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
   4. Access via browser: https://34.131.165.237

5. API Endpoints
   - GET /            : Loads the UI
   - POST /send       : Sends a message JSON {username, message}
   - GET /get_messages: Returns JSON list of messages

6. Files Included
   - app.py
   - templates/index.html
   - Dockerfile
   - requirements.txt
