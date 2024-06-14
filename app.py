# from flask import Flask, render_template, request, redirect, jsonify, url_for, session
# from datetime import datetime
# import mysql.connector
# from mysql.connector import Error
# app = Flask(__name__)
# app.secret_key = 'xyzsdfg'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Abhinaya@2004'
# app.config['MYSQL_DB'] = 'student'

# def get_db_connection():
#     return mysql.connector.connect(
#         host=app.config['MYSQL_HOST'],
#         user=app.config['MYSQL_USER'],
#         password=app.config['MYSQL_PASSWORD'],
#         database=app.config['MYSQL_DB']
#     )


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/view')
# def view():
#     return render_template('view_attendance.html')

# @app.route('/faculty')
# def faculty():
#     return render_template('login.html')

# @app.route('/student')
# def student():
#     return render_template('login1.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     message = ''
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         username = request.form['username']
#         password = request.form['password']
#         db_connection = get_db_connection()
#         try:
#             with db_connection.cursor(dictionary=True) as cursor:
#                 cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password))
#                 user = cursor.fetchone()
#                 if user:
#                     session['loggedin'] = True
#                     session['username'] = user['username']
#                     message = 'Logged in successfully!'
#                     return render_template('dashboard.html')
#                 else:
#                     message = 'Please enter correct email / password!'
#         except Error as e:
#             print(f"Error: {e}")
#         finally:
#             db_connection.close()
#     return render_template('login.html', message=message)

# @app.route('/login1', methods=['GET', 'POST'])
# def login1():
#     message = ''
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
#         username = request.form['username']
#         password = request.form['password']
#         db_connection = get_db_connection()
#         try:
#             with db_connection.cursor(dictionary=True) as cursor:
#                 cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password))
#                 user = cursor.fetchone()
#                 if user:
                    # session['loggedin'] = True
                    # session['username'] = user['username']
#                     message = 'Logged in successfully!'
#                     cursor.execute('SELECT * FROM student WHERE rollno = %s', (username,))
#                     details = cursor.fetchall()
#                     print(details)
#                     return render_template('student.html', details =details)
#                 else:
#                     message = 'Please enter correct email / password!'
#         except Error as e:
#             print(f"Error: {e}")
#         finally:
#             db_connection.close()
#     return render_template('login1.html', message=message)

# @app.route('/take_attendance')
# def take_attendance():
#     # Check if faculty is logged in
#     if 'loggedin' in session:
#         return render_template('faculty.html')
#     else:
#         return redirect(url_for('index'))
    
# @app.route('/get_students', methods=['POST'])
# def get_students():
#     data = request.get_json()
#     class_selected = data['class']
    
#     query = """
#     SELECT rollno, name 
#     FROM details 
#     WHERE class = %s
#     """
    
#     db_connection = get_db_connection()
#     try:
#         with db_connection.cursor(dictionary=True) as cursor:
#             cursor.execute(query, (class_selected,))
#             students = cursor.fetchall()
#             return jsonify(students)
#     except Error as e:
#         print(f"Error: {e}")
#         return jsonify([])
#     finally:
#         db_connection.close()


# # @app.route('/update_attendance', methods=['POST'])
# # def update_attendance():
# #     data = request.get_json()
# #     print(data)
# #     rollno = data['rollno']
# #     period = data['period']
# #     date = data['date']
# #     status = data['status']
# #     class_selected = data['classSelect']  # Ensure class is included in the data received
# #     print(class_selected)
    
# #     period_column = f"p{period}"  # e.g., "p1", "p2"
    
# #     query = f"""
# #     INSERT INTO student (rollno, name, date, {period_column}, class)
# #     VALUES (%s, %s, %s, %s, %s)
# #     ON DUPLICATE KEY UPDATE
# #     {period_column} = VALUES({period_column})
# #     """
    
# #     db_connection = get_db_connection()
# #     try:
# #         with db_connection.cursor(dictionary=True) as cursor:
# #             cursor.execute(query, (rollno, name, date, status, class_selected))
# #             db_connection.commit()
# #             return jsonify({'success': True})
# #     except Error as e:
# #         print(f"Error: {e}")
# #         return jsonify({'success': False})
# #     finally:
# #         db_connection.close()
# def get_attendance_records(selected_class):
#     print(selected_class)
#     db_connection = get_db_connection()  # Assuming you have this function defined
#     attendance_records = []
#     try:
#         with db_connection.cursor(dictionary=True) as cursor:
#             # Fetch attendance records for the selected class from the database
#             cursor.execute('SELECT * FROM student WHERE class = %s', (selected_class,))
#             attendance_records = cursor.fetchall()
           
#     except Error as e:
#         print(f"Error: {e}")
#     finally:
#         db_connection.close()
#     return attendance_records



# # @app.route('/update_attendance', methods=['POST'])
# # def update_attendance():
# #     data = request.get_json()
# #     print(data)

# #     rollno = data.get('rollno')
# #     period = data.get('period')
# #     date = data.get('date')
# #     status = data.get('status')
# #     class_name = data.get('selectedClass')
    

# #     if not all([rollno, period, date, status, class_name]):
# #         return jsonify({'success': False, 'message': 'Missing required fields'}), 400

# #     period_column = f'p{period}'

# #     conn = get_db_connection()
# #     if not conn:
# #         return jsonify({'success': False, 'message': 'Database connection error'}), 500

# #     try:
# #         cursor = conn.cursor()

# #         query = "SELECT rollno FROM student WHERE date = %s"
# #         cursor.execute(query, (date,))
# #         result = cursor.fetchone()
# #         print(result)

# #         if result:
# #             update_query = f"UPDATE student SET {period_column} = %s WHERE name = %s AND date = %s"
# #             cursor.execute(update_query, (status, rollno, date))
# #         else:
# #             insert_query = f"INSERT INTO student (rollno, date, {period_column}, class) VALUES (%s, %s, %s, %s)"
# #             cursor.execute(insert_query, (rollno, date, status, class_name))

# #         conn.commit()
# #         return jsonify({'success': True, 'message': 'Attendance updated successfully'})
# #     except mysql.connector.Error as err:
# #         conn.rollback()
# #         print(f"Error: {err}")
# #         return jsonify({'success': False, 'message': str(err)}), 500
# #     finally:
# #         cursor.close()
# #         conn.close()

# import logging

# @app.route('/update_attendance', methods=['POST'])
# def update_attendance():
#     data = request.get_json()
#     logging.info(f"Received data: {data}")

#     rollno = data.get('rollno')
#     period = data.get('period')
#     date = data.get('date')
#     status = data.get('status')
#     class_name = data.get('selectedClass')

#     if not all([rollno, period, date, status, class_name]):
#         return jsonify({'success': False, 'message': 'Missing required fields'}), 400

#     period_column = f'p{period}'

#     conn = get_db_connection()
#     if not conn:
#         logging.error("Failed to connect to the database")
#         return jsonify({'success': False, 'message': 'Database connection error'}), 500

#     try:
#         cursor = conn.cursor()

#         # Fetch the name from the records table based on rollno
#         query = "SELECT name FROM records WHERE rollno = %s"
#         cursor.execute(query, (rollno,))
#         record = cursor.fetchone()
#         if record:
#             name = record[0]
#         else:
#             name = None

#         if name:
#             query = "SELECT rollno FROM student WHERE date = %s"
#             cursor.execute(query, (date,))
#             result = cursor.fetchone()
#             logging.info(f"Existing attendance record: {result}")

#             if result:
#                 update_query = f"UPDATE student SET {period_column} = %s WHERE rollno = %s AND date = %s"
#                 cursor.execute(update_query, (status, rollno, date))
#             else:
#                 insert_query = f"INSERT INTO student (rollno, name, date, {period_column}, class) VALUES (%s, %s, %s, %s, %s)"
#                 cursor.execute(insert_query, (rollno, name, date, status, class_name))

#             conn.commit()
#             logging.info("Attendance updated successfully")
#             return jsonify({'success': True, 'message': 'Attendance updated successfully'})
#         else:
#             logging.error("Name not found for the given rollno")
#             return jsonify({'success': False, 'message': 'Name not found for the given rollno'}), 404
#     except mysql.connector.Error as err:
#         conn.rollback()
#         logging.error(f"Database error: {err}")
#         return jsonify({'success': False, 'message': str(err)}), 500
#     finally:
#         cursor.close()
#         conn.close()


# @app.route('/view_attendance', methods=['GET', 'POST'])
# def view_attendance():
#     if request.method == 'POST':
#         selected_class = request.form['class']
#         attendance_records = get_attendance_records(selected_class)
#         return render_template('view_attendance.html', selected_class=selected_class, attendance_records=attendance_records)
#     else:
#         return render_template('view_attendance.html')





# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, render_template, request, redirect, jsonify, url_for
from datetime import datetime, timedelta
import mysql.connector
from mysql.connector import Error
import jwt
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xyzabc'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Abhinaya@2004'
app.config['MYSQL_DB'] = 'student'

def get_db_connection():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expires in 1 hour
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def jwt_token_required(f):
    def decorator(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return redirect(url_for('index'))
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            request.username = data['username']
        except jwt.ExpiredSignatureError:
            return redirect(url_for('index'))
        except jwt.InvalidTokenError:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    decorator.__name__ = f.__name__
    return decorator

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view():
    return render_template('view_attendance.html')

@app.route('/faculty')
def faculty():
    return render_template('login.html')

@app.route('/student')
def student():
    return render_template('login1.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        db_connection = get_db_connection()
        try:
            with db_connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password))
                user = cursor.fetchone()
                if user:
                    token = generate_token(username)
                    response = redirect(url_for('dashboard'))
                    response.set_cookie('token', token)
                    return response
                else:
                    message = 'Please enter correct email / password!'
        except Error as e:
            print(f"Error: {e}")
        finally:
            db_connection.close()
    return render_template('login.html', message=message)

@app.route('/login1', methods=['GET', 'POST'])
def login1():
    message = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        db_connection = get_db_connection()
        try:
            with db_connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT * FROM user WHERE username = %s AND password = %s', (username, password))
                user = cursor.fetchone()
                if user:
                    token = generate_token(username)
                    response = redirect(url_for('student_dashboard'))
                    response.set_cookie('token', token)
                    cursor.execute('SELECT * FROM student WHERE rollno = %s', (username,))
                    details = cursor.fetchall()
                    return render_template('student.html', details=details)
                else:
                    message = 'Please enter correct email / password!'
        except Error as e:
            print(f"Error: {e}")
        finally:
            db_connection.close()
    return render_template('login1.html', message=message)

@app.route('/dashboard')
@jwt_token_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/student_dashboard')
@jwt_token_required
def student_dashboard():
    username = request.username
    db_connection = get_db_connection()
    try:
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM student WHERE rollno = %s', (username,))
            details = cursor.fetchall()
            return render_template('student.html', details=details)
    except Error as e:
        print(f"Error: {e}")
    finally:
        db_connection.close()

@app.route('/take_attendance')
@jwt_token_required
def take_attendance():
    return render_template('faculty.html')

@app.route('/get_students', methods=['POST'])
@jwt_token_required
def get_students():
    data = request.get_json()
    class_selected = data['class']
    query = """
    SELECT rollno, name 
    FROM details 
    WHERE class = %s
    """
    db_connection = get_db_connection()
    try:
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute(query, (class_selected,))
            students = cursor.fetchall()
            return jsonify(students)
    except Error as e:
        print(f"Error: {e}")
        return jsonify([])
    finally:
        db_connection.close()

@app.route('/update_attendance', methods=['POST'])
@jwt_token_required
def update_attendance():
    data = request.get_json()
    logging.info(f"Received data: {data}")
    rollno = data.get('rollno')
    period = data.get('period')
    date = data.get('date')
    status = data.get('status')
    class_name = data.get('selectedClass')
    if not all([rollno, period, date, status, class_name]):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400
    period_column = f'p{period}'
    conn = get_db_connection()
    if not conn:
        logging.error("Failed to connect to the database")
        return jsonify({'success': False, 'message': 'Database connection error'}), 500
    try:
        cursor = conn.cursor()
        query = "SELECT name FROM records WHERE rollno = %s"
        cursor.execute(query, (rollno,))
        record = cursor.fetchone()
        if record:
            
            name = record[0]
            print(name)
        else:
            name = None
        if name:
            query = "SELECT name FROM student WHERE date = %s and rollno = %s"
            cursor.execute(query, (date,rollno,))
            result = cursor.fetchone()
            print(result)
            logging.info(f"Existing attendance record: {result}")
            if result:
                print('update')
                update_query = f"UPDATE student SET {period_column} = %s WHERE rollno = %s AND date = %s"
                cursor.execute(update_query, (status, rollno, date))
            else:
                print('insert')
                insert_query = f"INSERT INTO student (rollno, name, date, {period_column}, class) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (rollno, name, date, status, class_name))
            conn.commit()
            logging.info("Attendance updated successfully")
            return jsonify({'success': True, 'message': 'Attendance updated successfully'})
        else:
            logging.error("Name not found for the given rollno")
            return jsonify({'success': False, 'message': 'Name not found for the given rollno'}), 404
    except mysql.connector.Error as err:
        conn.rollback()
        logging.error(f"Database error: {err}")
        return jsonify({'success': False, 'message': str(err)}), 500
    finally:
        cursor.close()
        conn.close()

@app.route('/view_attendance', methods=['GET', 'POST'])
@jwt_token_required
def view_attendance():
    if request.method == 'POST':
        selected_class = request.form['class']
        attendance_records = get_attendance_records(selected_class)
        return render_template('view_attendance.html', selected_class=selected_class, attendance_records=attendance_records)
    else:
        return render_template('view_attendance.html')

def get_attendance_records(selected_class):
    print(selected_class)
    db_connection = get_db_connection()
    attendance_records = []
    try:
        with db_connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM student WHERE class = %s', (selected_class,))
            attendance_records = cursor.fetchall()
    except Error as e:
        print(f"Error: {e}")
    finally:
        db_connection.close()
    return attendance_records

if __name__ == '__main__':
    app.run(debug=True)

