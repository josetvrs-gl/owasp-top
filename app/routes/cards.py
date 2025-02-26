from flask import Blueprint, request, render_template_string, redirect, url_for, session
from app.db import get_db_connection
import json

cards = Blueprint('cards', __name__)

@cards.route('/leak_cards', methods=['GET'])
def leak_cards():
    user_input = request.args.get('user_id', '')

    conn = get_db_connection()
    cursor = conn.cursor()

    # Consulta vulnerable a SQL Injection
    query = f"SELECT * FROM credit_cards WHERE user_id = {user_input}"
    cursor.execute(query)

    cards = cursor.fetchall()
    conn.close()

    if not cards:
        return "No credit cards found!"

    # Mostrar tarjetas en texto claro (porque la BD las descifra automáticamente)
    return render_template_string('''
        <h1 class="mb-5">Credit Card Details</h1>
        {% for card in cards %}
            <p>Card Number: {{ card['card_number'] }}</p>
            <p>Cardholder Name: {{ card['cardholder_name'] }}</p>
            <p>Expiration Date: {{ card['expiration_date'] }}</p>
            <hr>
        {% endfor %}
    ''', cards=cards)