import os
from flask import Blueprint, request, render_template

ping = Blueprint('ping', __name__)

@ping.route('/', methods=['GET', 'POST'])
def ping_ip():
    output = ""
    if request.method == 'POST':
        target = request.form['target']  # User input
        output = os.popen(f"ping -c 3 {target}").read()  # VULNERABLE

    return render_template('ping/ipping.html', output=output)
