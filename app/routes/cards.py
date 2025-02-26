from flask import Blueprint, request, render_template, redirect, url_for, session
from app.db import get_db_connection
import json

cards = Blueprint('cards', __name__)

@cards.route('/', methods=['GET'])
def user_cards():
    user_input = request.args.get('user_id', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    # Consulta vulnerable a SQL Injection
    query = f"SELECT * FROM credit_cards WHERE user_id = ?"
    cursor.execute(query, (user_input,))

    cards = cursor.fetchall()
    conn.close()

    if not cards:
        return "No credit cards found!"

    # Mostrar tarjetas en texto claro (porque la BD las descifra automáticamente)
    return render_template('cards/cardsList.html', cards=cards)