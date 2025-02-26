from flask import Blueprint, render_template, redirect, url_for, session
from app.db import get_db_connection

users = Blueprint('users', __name__)

@users.route('/')
def all_users():
    # TO CHECK IF THE USER IS LOGGED IN
    if not session:
        return redirect(url_for('auth.login'))
    # TO MAKE USER LIST ONLY ACCESSIBLE FOR ADMIN, UNCOMMENT THE FOLLOWING TWO LINES
    #if session['user_id'] != 1:
    #    return render_template('errors/notAllowed.html')
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()
    return render_template('users/usersList.html', users=users)

@users.route('/<int:user_id>')
def profile(user_id):
    if not session:
        return redirect(url_for('auth.login'))
    # TO ONLY ALLOW THE USER THE SEE ITS OWN PROGILE
    #if user_id != session['user_id']:
    #    return render_template('errors/notAllowed.html')
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    conn.close()
    return render_template('users/profile.html', user=user)
