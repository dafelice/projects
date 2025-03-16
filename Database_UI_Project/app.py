from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

app = Flask(__name__)

# Database connection helper
def get_db_connection():
    return sql.connect('database.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/name', methods=['POST', 'GET'])
def name():
    error = None
    result = []

    if request.method == 'POST':
        first_name = request.form.get('FirstName', '').strip()
        last_name = request.form.get('LastName', '').strip()
        
        if first_name and last_name:
            success = add_patient_to_db(first_name, last_name)
            if success:
                result = fetch_all_patients()
            else:
                error = 'Database Error: Could not add patient'
        else:
            error = 'Invalid input: Names cannot be empty'

    return render_template('input.html', error=error, result=result)

def add_patient_to_db(first_name, last_name):
    """ Inserts a new patient into the database, returns True if successful. """
    try:
        with get_db_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS patients (
                    pid INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname TEXT NOT NULL,
                    lastname TEXT NOT NULL
                );
            ''')
            conn.execute('INSERT INTO patients (firstname, lastname) VALUES (?, ?)', (first_name, last_name))
            conn.commit()
        return True
    except sql.Error as e:
        print("Database Error:", e)
        return False

@app.route('/add_patient')
def add_patient():
    result = fetch_all_patients()
    return render_template('input.html', result=result)

@app.route('/delete_patient', methods=['POST', 'GET'])
def delete_patient():
    result = fetch_all_patients()
    error = None

    if request.method == 'POST':
        first_name = request.form.get('FirstName', '').strip()
        last_name = request.form.get('LastName', '').strip()
        
        if first_name and last_name:
            success = delete_from_db(first_name, last_name)
            if not success:
                error = f"No patient found with name: {first_name} {last_name}"
            result = fetch_all_patients()  # Refresh list after deletion

    return render_template('delete.html', result=result, error=error)

def delete_from_db(first_name, last_name):
    """ Deletes a patient from the database, returns True if successful. """
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM patients WHERE firstname=? AND lastname=?", (first_name, last_name))
            conn.commit()
            return cursor.rowcount > 0  # Returns True if at least one row was deleted
    except sql.Error as e:
        print("Database Error:", e)
        return False

def fetch_all_patients():
    """ Fetch all patient records from the database. """
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM patients")
            return cursor.fetchall()
    except sql.Error as e:
        print("Database Error:", e)
        return []

if __name__ == "__main__":
    app.run(debug=True)
