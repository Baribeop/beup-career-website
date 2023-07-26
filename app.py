# import required modules
from flask import Flask, render_template, jsonify  # Flask is a class of the module flask

# instantiate Flask , create object of class Flask
app = Flask(__name__)  # __name__ is the variable name known as __main__
jobs = [{
  'id': 1,
  'title': 'Data Scientist',
  'salary': '₦230000',
  'location': 'Lagos,Nigeria'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'salary': 'Rs.30000',
  'location': 'Delhi,India'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'salary': '£12000',
  'location': 'London,Uk'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'salary': '$23000',
  'location': 'Remote'
}]

# create path/route for accessing web pages, @ is a decorator (advance python concept) which allows access to additional functionality
#when the path / is followed, view function displays the return statement


# Display jobs from list above using HTML
@app.route('/')
def home():
  return render_template('home.html', jobs=jobs)


# using forms to add jobs
@app.route('/add')
def add_job():
  return render_template('jobs.html')


# Endpoint for job application
@app.route('/apply')
def form():
  return render_template('form.html')


#Display using API
@app.route('/list_job')
def api_list_job():
  return jsonify(jobs)


# if the script app.py is run but not imported, the app should run
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
