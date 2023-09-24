from . import create_app
from .Authentication.models import db

app = create_app()

with app.app_context():
    db.create_all()


if __name__ =="__main__":
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        print(f"An error occured {str(e)}")
