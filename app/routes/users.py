from flask import Blueprint, request, render_template_string, redirect, url_for, session
from app.db import get_db_connection
import json

users = Blueprint('users', __name__)

@users.route('/')
def all_users():
    # Handle user profile display here
    if not session:
        return redirect(url_for('auth.login'))
    if session['user_id'] != 1:
        return render_template_string('''
            <h1>Not Allowed: 404</h1>
            <p>Only accessible for admin user</p>
            <form action="{{ url_for('index.home') }}" method="POST">
                <button type="submit">HOME</button>
            </form>
        ''')
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()
    if users:
        data = json.dumps(users)
    else:
        data = "Users not found"
        
    return render_template_string('''
        <p>Users</p>
        <p>{{ message }}</p>
        <form action="{{ url_for('index.home') }}" method="GET">
            <button type="submit">HOME</button>
        </form>
    ''', message=data)

@users.route('/<int:user_id>')
def profile(user_id):
    # Handle user profile display here
    if not session:
        return redirect(url_for('auth.login'))
    if user_id != session['user_id']:
        return render_template_string('''
            <h1>Not Allowed: 404</h1>
            <p>Please authenticate to see this information</p>
            <form action="{{ url_for('index.home') }}" method="GET">
                <button type="submit">HOME</button>
            </form>
        ''')
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        data = json.dumps(user)
    else:
        data = "User not found"
        
    return render_template_string('''
        <p>You info:</p>
        <p>{{ message }}</p>
        <form action="{{ url_for('index.home') }}" method="GET">
            <button type="submit">HOME</button>
        </form>
    ''', message=data)
