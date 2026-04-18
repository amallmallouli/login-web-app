from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')

# Fake DB
users = {
    'admin': generate_password_hash('password123'),
    'user': generate_password_hash('user123')
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Requête invalide'}), 400

    username = data.get('username')
    password = data.get('password')

    if username in users and check_password_hash(users[username], password):
        session['username'] = username
        return jsonify({'redirect': url_for('dashboard')}), 200
    else:
        return jsonify({'message': 'Identifiants incorrects'}), 401

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('index'))

    return render_template('dashboard.html', username=session['username'])

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
