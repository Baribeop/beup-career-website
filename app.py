# import required modules 
from flask import Flask  # Flask is a class of the module flask

# instantiate Flask , create object of class Flask
app =  Flask(__name__) # __name__ is the variable name known as __main__


# create path/route for accessing web pages, @ is a decorator (advance python concept) which allows access to additional functionality
#when the path / is followed, view function displays the return statement 
@app.route('/') 
def home(): 
  return 'Welcome to Beup career website'

# if the script app.py is run but not imported, the app should run
if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug=True)
  
  

