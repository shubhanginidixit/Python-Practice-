from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# ---------------- DATABASE CONNECTION ----------------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Shubhangini#1234",  # change this if your MySQL password differs
        database="rems_db"
    )

# ---------------- HOME / PROPERTY PAGE ----------------
@app.route('/')
def home():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Property")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', properties=data)

# ---------------- ADD PROPERTY ----------------
@app.route('/add', methods=['GET', 'POST'])
def add_property():
    if request.method == 'POST':
        ptype = request.form['ptype']
        paddress = request.form['paddress']
        pstatus = request.form['pstatus']
        pprice = request.form['pprice']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Property (PType, PAddress, PStatus, PPrice) VALUES (%s, %s, %s, %s)",
            (ptype, paddress, pstatus, float(pprice))
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('home'))
    return render_template('add_property.html')

# ---------------- UPDATE STATUS ----------------
@app.route('/update/<int:pid>')
def update_status(pid):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT PStatus FROM Property WHERE PID = %s", (pid,))
    row = cursor.fetchone()
    if row:
        status = row[0]
        new_status = "Sold" if status == "Available" else "Available"
        cursor.execute("UPDATE Property SET PStatus = %s WHERE PID = %s", (new_status, pid))
        conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('home'))

# ---------------- DELETE PROPERTY ----------------
@app.route('/delete/<int:pid>')
def delete_property(pid):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Property WHERE PID = %s", (pid,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('home'))

# ---------------- TENANT MANAGEMENT ----------------
@app.route('/tenants', methods=['GET', 'POST'])
def tenants():
    conn = connect_db()
    cursor = conn.cursor()
    if request.method == 'POST':
        name = request.form['tname']
        contact = request.form['contact']
        address = request.form['taddress']
        cursor.execute(
            "INSERT INTO Tenant (TName, Contact, Address) VALUES (%s, %s, %s)",
            (name, contact, address)
        )
        conn.commit()
    cursor.execute("SELECT * FROM Tenant")
    tenants = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('tenants.html', tenants=tenants)

# ---------------- MAINTENANCE ----------------
@app.route('/maintenance', methods=['GET', 'POST'])
def maintenance():
    conn = connect_db()
    cursor = conn.cursor()
    if request.method == 'POST':
        pid = request.form['pid']
        desc = request.form['desc']
        cost = request.form['cost']
        date = request.form['date']
        cursor.execute(
            "INSERT INTO Maintenance (PID, Description, Cost, MDate) VALUES (%s, %s, %s, %s)",
            (pid, desc, float(cost), date)
        )
        conn.commit()
    cursor.execute("SELECT * FROM Maintenance")
    maintenance = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('maintenance.html', maintenance=maintenance)

# ---------------- OWNERSHIP / LEASE ----------------
@app.route('/ownership', methods=['GET', 'POST'])
def ownership():
    conn = connect_db()
    cursor = conn.cursor()
    if request.method == 'POST':
        pid = request.form['pid']
        tid = request.form['tid']
        lease_type = request.form['lease_type']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        cursor.execute(
            "INSERT INTO Lease (PID, TID, LeaseType, StartDate, EndDate) VALUES (%s, %s, %s, %s, %s)",
            (pid, tid, lease_type, start_date, end_date)
        )
        conn.commit()
    cursor.execute('''
        SELECT L.LID, P.PType, P.PAddress, T.TName, L.LeaseType, L.StartDate, L.EndDate
        FROM Lease L
        JOIN Property P ON L.PID = P.PID
        JOIN Tenant T ON L.TID = T.TID
        ORDER BY L.LID DESC
    ''')
    ownership_data = cursor.fetchall()
    cursor.execute("SELECT PID, PType, PAddress FROM Property")
    properties = cursor.fetchall()
    cursor.execute("SELECT TID, TName FROM Tenant")
    tenants = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('ownership.html', ownership=ownership_data, properties=properties, tenants=tenants)

# ---------------- REPORTS ----------------
@app.route('/reports')
def reports():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Property")
    total = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM Property WHERE PStatus='Available'")
    available = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM Property WHERE PStatus='Sold'")
    sold = cursor.fetchone()[0]
    cursor.execute("SELECT IFNULL(SUM(PPrice), 0) FROM Property")
    total_value = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM Tenant")
    tenants_count = cursor.fetchone()[0]
    cursor.execute("""
        SELECT T.TName, COUNT(*) AS cnt,
               SUM(CASE WHEN L.LeaseType='Sale' THEN 1 ELSE 0 END) AS sales_count,
               SUM(CASE WHEN L.LeaseType='Rent' THEN 1 ELSE 0 END) AS rent_count
        FROM Lease L
        JOIN Tenant T ON L.TID = T.TID
        GROUP BY T.TName
        ORDER BY cnt DESC
    """)
    per_tenant = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template(
        'reports.html',
        total=total, available=available, sold=sold,
        total_value=total_value, tenants_count=tenants_count,
        per_tenant=per_tenant
    )

if __name__ == '__main__':
    app.run(debug=True)


