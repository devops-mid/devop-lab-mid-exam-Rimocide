import re
from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get data from form
        name = request.form['name']
        email = request.form['email']
        phone = request.form.get('phone', '')  # Optional field
        cnic = request.form.get('cnic', '').strip()  # CNIC field
        
        print(f"Received CNIC: {cnic}")  # Debugging CNIC value
        
        # Remove any non-numeric characters from CNIC (e.g., dashes)
        cnic = re.sub(r'\D', '', cnic)
        
        # Debugging after cleaning CNIC
        print(f"Cleaned CNIC: {cnic}")
        
        # Validate CNIC (must be exactly 13 digits)
        if not cnic or len(cnic) != 13 or not cnic.isdigit():
            print("Invalid CNIC format.")  # Debugging if CNIC is invalid
            return "Invalid CNIC. It should be a 13-digit number.", 400
        
        # Save the user to the database
        user = User(name=name, email=email, phone=phone, cnic=cnic)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error: {e}")  # Print the error if any
        return "An internal server error occurred.", 500
