from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

DATABASE_FILE = 'database.txt'
CSV_FILE = 'database.csv'


@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/<string:pagename>")
def html_page(pagename):
    return render_template(pagename)


def write_to_database(data_entries, database_file):
    try:
        email = data_entries['email']
        subject = data_entries['subject']
        message = data_entries['message']
    except:
        raise Exception('Wrong indexes in dictionary') 
    try:
        with open(database_file, mode='a') as database:
            database.write(f'\nEmail: {email}, Subject: {subject}, Message: {message}')
    except FileNotFoundError:
        raise Exception('Database file does not exist')

def  write_to_csv(data_entries, csv_file):
    try:
        email = data_entries['email']
        subject = data_entries['subject']
        message = data_entries['message']
        #entry = ','.join([email, subject, message])
    except:
        raise Exception('Wrong indexes in dictionary') 
    try:
        with open(csv_file, 'a', newline='') as database:
            csv_writer = csv.writer(database, delimiter=';')
            csv_writer.writerow([email, subject, message])
    except FileNotFoundError:
        raise Exception('Database file does not exist')




@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data, CSV_FILE)

        # print(data)
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return redirect('thanks.html') # Route is already defined, we only need a redirection to this route
