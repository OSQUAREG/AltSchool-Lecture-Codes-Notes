# install needed packages using the command line: pip install flask Flask-SQLAlchemy
# When installing a project gotten elsewhere, install its requirements before running Flask: pip install -r requirements.txt

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(base_dir, 'users.db')  # defining the db type and name
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# Creating the User class for each instance of the user to be created in the table.
class User(db.Model):
    # defining the table name
    __tablename__ = 'user'

    # defining the table columns
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"User {self.username}"


@app.route('/')
def index():
    # Querying the User table and return it on the home (index) page.
    users = User.query.all()

    # context help to return the details in the frontend.
    context = {
        'users': users
    }

    return render_template('models.html', **context)


# Creating a user (as an instance of the User class)
@app.route('/users', methods=['POST'])
def create_user():

    # Getting the details from the form fields created on the frontend.
    # note: the parameter in the form.get() must be same as the name attribute of form field i.e. name="username"
    form_username = request.form.get('username')
    form_email = request.form.get('email')
    form_age = request.form.get('age')
    form_gender = request.form.get('gender')

    # Tying the User table columns to the form fields.
    new_user = User(username=form_username, email=form_email,
                    age=form_age, gender=form_gender)

    # Adding and committing the new user created to the database.
    db.session.add(new_user)
    db.session.commit()

    # Redirecting to the index url.
    return redirect(url_for('index'))


# Updating a user
@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    user_to_update = User.query.get_or_404(id)

    if request.method == 'POST':
        user_to_update.username = request.form.get('username')
        user_to_update.email = request.form.get('email')
        user_to_update.age = request.form.get('age')
        user_to_update.gender = request.form.get('gender')

        db.session.commit()

        return redirect(url_for('index'))

    context = {
        'user': user_to_update
    }

    return render_template('update.html', **context)


# Deleting a user
@app.route('/delete/<int:id>/', methods=['GET'])
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)

    db.session.delete(user_to_delete)
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)


# Command line to run .py file: python app.py (ensure you are in the project folder)
# CTRL + C to quit.
