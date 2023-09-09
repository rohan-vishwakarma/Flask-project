from . import create_app
from .models import db

app = create_app()

with app.app_context():
    db.create_all()


if __name__ =="__main__":
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occured {str(e)}")
