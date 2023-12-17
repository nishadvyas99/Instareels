from flaskapp import app
from flask_migrate import Migrate
# from dotenv import load_dotenv

# load_dotenv()
# migrate = Migrate(app, db)

def main():
    app.run(debug=1)


if __name__ == "__main__":
    main()    