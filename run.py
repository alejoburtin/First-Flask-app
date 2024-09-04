#This script imports your Flask app and runs it
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
