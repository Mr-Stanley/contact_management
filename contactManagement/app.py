
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/contacts_db"
mongo = PyMongo(app)


@app.route("/")
def home_page():
    contacts = mongo.db.contacts.find()
    return render_template('home_page.html',contacts=contacts)


@app.route("/add_contact_form")
def add_contact():
    return render_template('add_contact_form.html')

@app.route("/")
def get_all_contacts():
    return mongo.db.contacts.find()


@app.route("/view_contact")
def view_contact():
    contacts = get_all_contacts()
    return render_template('view_contact_page.html', contacts=contacts)




@app.route('/add_contact_form', methods=['POST'])
def submit_contact_form():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        house_address = request.form['house_address']

        mongo.db.contacts.insert_one({'first_name': first_name, 'last_name': last_name, 'email': email, 'phone_number': phone_number, 'house_address': house_address})

        return redirect(url_for('home_page'))





if __name__ == '__main__':
    app.run(debug=True)
