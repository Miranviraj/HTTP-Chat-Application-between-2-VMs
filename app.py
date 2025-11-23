from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Store messages in a simple list (In-memory storage)
messages = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    username = data.get('username')
    msg = data.get('message')
    if username and msg:
        # Add message to the list
        messages.append({'username': username, 'message': msg})
        return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'error'}), 400

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    # Run with SSL (HTTPS) enabled on port 443
    app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))