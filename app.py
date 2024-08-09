from flask import Flask, render_template, request, redirect, url_for
import string
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/password_generator', methods=['GET', 'POST'])
def password_generator():
    if request.method == 'POST':
        length = int(request.form['length'])
        password = generate_password(length)
        return render_template('password_generator.html', password=password)
    return render_template('password_generator.html')

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))


@app.route('/password_checker', methods=['GET', 'POST'])
def password_checker():
    if request.method == 'POST':
        password = request.form['password']
        feedback, suggested_password = check_password_strength(password)
        return render_template('password_checker.html', feedback=feedback, suggested_password=suggested_password)
    return render_template('password_checker.html')

def check_password_strength(password):
    # Check password length
    if len(password) < 8:
        return "Password must be at least 8 characters long.", generate_password(12)

    # Check for uppercase, lowercase, numbers, and special characters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    if not has_upper or not has_lower or not has_digit or not has_special:
        return "Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character.", generate_password(12)

    return "Password is strong!", None

if __name__ == '__main__':
    app.run(debug=True)
