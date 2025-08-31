"""
Sample Flask application with intentional security issues for testing
"""
import os
import pickle
import subprocess
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded credentials (Security issue)
DB_PASSWORD = "admin123"
API_KEY = "secret_key_123"

# Vulnerable template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevSecOps Demo</title>
</head>
<body>
    <h1>Welcome {{ name }}!</h1>
    <form method="POST">
        <input type="text" name="input_data" placeholder="Enter data">
        <input type="submit" value="Submit">
    </form>
    <p>Result: {{ result }}</p>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    """Main endpoint with multiple security issues"""
    result = ""
    
    if request.method == 'POST':
        user_input = request.form.get('input_data', '')
        
        # Command injection vulnerability
        if user_input.startswith('ping'):
            # UNSAFE: Direct command execution
            result = subprocess.check_output(f"ping -c 1 {user_input[5:]}", shell=True)
        
        # Deserialization vulnerability
        elif user_input.startswith('serialized'):
            try:
                # UNSAFE: Pickle deserialization
                data = pickle.loads(bytes.fromhex(user_input[11:]))
                result = f"Deserialized: {data}"
            except:
                result = "Deserialization failed"
    
    return render_template_string(HTML_TEMPLATE, name="User", result=result)

@app.route('/debug')
def debug_mode():
    """Endpoint with debug mode enabled"""
    # Security misconfiguration
    app.debug = True
    return "Debug mode enabled"

@app.route('/users/<user_id>')
def get_user(user_id):
    """Potential SQL injection vulnerability"""
    # Simulated SQL query (vulnerable to injection)
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return f"Executing query: {query}"

if __name__ == '__main__':
    # Running with debug mode in production (security issue)
    app.run(debug=True, host='0.0.0.0', port=5000)