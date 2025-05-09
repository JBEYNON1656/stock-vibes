from app import create_app
from dotenv import load_dotenv

load_dotenv() #loads utility to be able to access secrets in the .env file

app = create_app() #returns a Flask app instance after it has been set up

if __name__ == '__main__': #special condition in python that checks if the script is being run directly (vs imported as a module)
    app.run(debug=True) #runs the app. Debug mode provides helpful error messages 