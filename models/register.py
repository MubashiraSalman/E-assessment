from db import db


class Register(db.Model):
    idd = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    # photo = db.Column(db.Blob, nullable=False)

    @classmethod
    def insert_in_db(cls, email, password):
        reg = Register(email=email, password=password)
        db.session.add(reg)
        db.session.commit()
        return reg
