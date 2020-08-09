from flask import Flask
app = Flask(__name__)
db_uri = 'mysql+pymysql://root:pass@localhost:3306/users'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
