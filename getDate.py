###########################
# Creating by Gokce Demir #
#     25 October 2020     #
###########################

# When this project runs that getting today's date and current time.
from flask import Flask  #import flask
from datetime import date
from datetime import datetime

app = Flask(__name__) # creating applicaiton instance
@app.route("/")  # at the end point /
# This method gets today's date and current time. Return date as a string.
def getDate ():
    today = date.today()
    now = datetime.now()
    return "Now time is  " + now.strftime("%H:%M:%S") +" Today's date: " + today.strftime("%d/%m/%Y")          # which returns current time

def main():
    app.run(debug=True, host='0.0.0.0') # runs the flask app

if __name__ == "__main__":
    main()