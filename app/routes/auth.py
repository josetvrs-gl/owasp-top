from flask import Blueprint, request, render_template_string, redirect, url_for, session
from app.db import get_db_connection
from app.utils.passwords import is_valid_password
import json

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'GET':
        if session and session['user_id']:
            user_id = session['user_id']
            return redirect(url_for('index.home'))
            
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # VULNERABLE SQL QUERY (DO NOT USE IN PRODUCTION)
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        
        # SECURE SQL QUERY
        #query = "SELECT * FROM users WHERE username = ? AND password = ?"
        #cursor.execute(query, (username, password))
        
        user = cursor.fetchone()
        conn.close()
        
        if user:
            user_id = user[0]
            session['user_id'] = user_id
            return redirect(url_for('index.home'))
        else:
            message = "Invalid credentials!"
    
    return render_template_string('''
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <input type="submit" value="Login">
        </form>
        <p>{{ message }}</p>
    ''', message=message)
    
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    message = ""
            
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check if user exists
        query = "SELECT * FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        
        if user:
            message = "Username already exists, please change it"
        else:
            # PASSWORD VALIDATION
            #is_valid, error_message = is_valid_password(password)
            query = f"INSERT INTO users (username, password) VALUES (?, ?)"
            cursor.execute(query, (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('auth.login'))
        conn.close()
    
    return render_template_string('''
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <input type="submit" value="Sign Up">
        </form>
        <p>{{ message }}</p>
    ''', message=message)



@auth.route('/logout', methods=['POST'])
def logout():
    session.clear()  # Clear session
    return redirect(url_for('auth.login'))  # Redirect to login page
