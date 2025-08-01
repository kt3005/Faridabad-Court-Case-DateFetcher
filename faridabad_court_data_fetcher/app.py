from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

def log_query(case_type, case_number, case_year):
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, case_type TEXT, case_number TEXT, case_year TEXT, timestamp TEXT)''')
    c.execute("INSERT INTO logs (case_type, case_number, case_year, timestamp) VALUES (?, ?, ?, ?)",
              (case_type, case_number, case_year, datetime.now().isoformat()))
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        case_type = request.form['case_type'].strip()
        case_number = request.form['case_number'].strip()
        case_year = request.form['case_year'].strip()

        log_query(case_type, case_number, case_year)

        # Mock data based on input (simulate real output)
        if case_type.upper() == "CS" and case_number == "1234" and case_year == "2022":
            result = {
                "parties": "A vs B",
                "filing_date": "2022-05-12",
                "next_hearing": "2025-08-15",
                "orders": [
                    {"title": "Latest Order", "link": "/static/sample_order.pdf"}
                ]
            }
        else:
            result = {"error": "⚠️ Case not found. Please check the details and try again."}

    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
