import socket
import pymysql.cursors
from flask import Flask, render_template, request, redirect 

def find_available_port():
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to an address and port
    s.bind(('localhost', 0))
    # Get the port bound by the socket
    port = s.getsockname()[1]
    # Close the socket
    s.close()
    return port

app = Flask(__name__, template_folder='/home/gcpcloud305/flaskfiles/signuppage')

# MySQL connection configuration
mysql_config = {
    'host': '35.200.228.255',  # Update with your Cloud SQL instance IP
    'user': 'root',               # Update with your MySQL username
    'password': 'Lavu@1234',           # Update with your MySQL password
    'database': 'customers'                # Update with your database name
}
@app.route('/')
def index():
    return render_template('signup.html')

@app.route('/signup_login', methods=['POST'])
def signup_login():
    customer_type = request.form.get('customer_type')
    if customer_type == 'existing':
        username = request.form['username']
        password = request.form['password']
        
        # Connect to MySQL database
        connection = pymysql.connect(**mysql_config)
        
        try:
            with connection.cursor() as cursor:
                # Execute the SQL query to check for the existence of the user
                sql = "SELECT * FROM Customers WHERE username = %s AND password = %s"
                cursor.execute(sql, (username, password))
                result = cursor.fetchone()  # Fetch one row
                
                if result:
                    # Pass username and password to the template
                    return render_template('existing_user.html', username=username, password=password)
                else:
                    # User does not exist or credentials are incorrect
                    return "Invalid username or password. Please try again."
        finally:
            connection.close()
    elif customer_type == 'new':
        # Retrieve form data for new customer
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        dob = request.form['dob']
        phone = request.form['phone']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        Address = "same",
        DateOfBirth = "1993-12-23",
        gender = "Male"
        
        # Connect to MySQL database
        connection = pymysql.connect(**mysql_config)
        
        try:
            with connection.cursor() as cursor:
                # Execute the SQL query to insert the new customer record
                sql = "INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, Username, Password, DateOfBirth, Gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (firstname, lastname, email, phone,Address, username, password, DateOfBirth, gender))
                connection.commit()
                
                # Redirect to a success page or render a success message
                return render_template('signup_success.html', username=username)
        finally:
            connection.close()
    else:
        return "Invalid customer type!"

if __name__ == '__main__':
    port = find_available_port()
    print(f"Starting Flask server on port {port}")
    app.run(debug=True, port=port)
