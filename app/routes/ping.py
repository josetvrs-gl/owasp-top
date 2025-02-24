import os
from flask import Blueprint, request, render_template_string

ping = Blueprint('ping', __name__)

@ping.route('/', methods=['GET', 'POST'])
def ping_ip():
    output = ""
    if request.method == 'POST':
        target = request.form['target']  # User input
        output = os.popen(f"ping -c 3 {target}").read()  # VULNERABLE

    return render_template_string('''
        <h1>Ping a Server</h1>
        <form method="POST">
            <input type="text" name="target" placeholder="Enter IP or Domain" required><br>
            <input type="submit" value="Ping">
        </form>
        <pre>{{ output }}</pre>
    ''', output=output)
