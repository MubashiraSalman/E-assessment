from app import app
from db import db
from models import register
import routes

with app.app_context():
    db.create_all()

app.run(port=999)
