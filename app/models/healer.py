from app import db

class Healer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    crystals = db.relationship("Crystal", back_populates="healer")