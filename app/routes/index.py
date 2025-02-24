from flask import Blueprint, request, render_template_string, redirect, url_for, session
from app.db import get_db_connection
import json

index = Blueprint('index', __name__)

@index.route('/')
def home():
    if not session or not session['user_id']:
        return redirect(url_for('auth.login'))
    # WELCOME WITH USER NAME
    user_id = session['user_id']
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    user_name = user[1]
    
    is_admin = False
    if user_name == "admin":
        is_admin = True
    
    conn.close()
    return render_template_string('''
        <h1>Welcome, {{ data }}</h1>
        <form action="{{ url_for('users.profile', user_id=session['user_id']) }}" method="GET">
            <button type="submit">Profile</button>
        </form>
        {% if is_admin %}
        <form action="{{ url_for('users.all_users') }}" method="GET">
            <button type="submit">All Users</button>
        </form>
        {% endif %}
        <form action="{{ url_for('auth.logout') }}" method="POST">
            <button type="submit">Logout</button>
        </form>
    ''', data=user_name, is_admin=is_admin)