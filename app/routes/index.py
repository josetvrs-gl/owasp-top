from flask import Blueprint, render_template, redirect, url_for, session
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
    return render_template('index.html', data=user_name, is_admin=is_admin)