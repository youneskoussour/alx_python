from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(_name_)

############################# TO DO 1 ############################
app.config['SQLALCHEMY_DATABASE_URI']= f'mysql://{db_username}:{db_password}@{"localhost"}/{db_name}'

###############################################################

db = SQLAlchemy(app)

############################  TO DO 2 ##############################
class User(db.Model):
    id = db.Column(db.integer,primary_key = True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)

def _repr_(self):
    return f"<User{self.username}>"
#################################################################

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables


@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"
@app.route('/',strict_slashes = False)
def index():
    return "Hello, ALX Flask!"
@app.route('/add_user',methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        new_user = User(name=name,email=email)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
        except:
            db.session.rollback()
            flash('Error: User with this email already exists', "error")
        return redirect(url_for("add_user"))
    else:
        return render_template("add_user.html")
@app.route('/users')
def users():
    all_users=User.query.all()
    return render_template('users.html',users=all_users)
# the below function involves deletion of users with and updates.
# Update a User
@app.route('/update_user/<int:user_id>', methods=['GET','POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        flash('User not found!', 'error')
        return redirect('/')

    if request.method == 'POST':
        # Handle POST request
        updated_name = request.form.get('name')
        updated_email = request.form.get('email')

        # Validate data
        if not updated_name or not updated_email:
            flash('Name and email are required!', 'error')
        else:
            # Check if the email is already taken by another user
            existing_user = User.query.filter_by(email=updated_email).first()
            if existing_user and existing_user.id != user.id:
                flash('Email is already taken by another user!', 'error')
            else:
                # Update the user
                user.name = updated_name
                user.email = updated_email
                db.session.commit()
                flash('User updated successfully!', 'success')
                return redirect('/')

    return render_template('update_user.html', user=user)

# Delete a User
@app.route('/delete_user/<int:user_id>', methods=['GET','POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        flash('User not found!', 'error')
        return redirect('/')

    if request.method == 'POST':
        # Handle POST request
        try:
            db.session.delete(user)
            db.session.commit()
            flash('User deleted successfully!', 'success')
            return redirect('/')
        except Exception as e:
            db.session.rollback()
            flash('Error deleting user. Please try again.', 'error')

    return render_template('delete_user.html', user=user)
if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)