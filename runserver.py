#allows me to run in the server
from api import create_app

app = create_app()
if __name__ == "__main__":
    app.run()