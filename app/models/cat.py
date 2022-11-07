from app import db
from flask import abort, make_response

class Cat(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String)
  color = db.Column(db.String)
  personality = db.Column(db.String)
  caretaker_id = db.Column(db.Integer, db.ForeignKey("caretaker.id"))
  caretaker = db.relationship("Caretaker", back_populates="cats")

  def to_dict(self):
    return {
      "name": self.name,
      "color": self.color,
      "personality": self.personality,
      "id": self.id,
      "caretaker_id": self.caretaker_id
    }

  @classmethod
  def from_dict(cls,req_body):
    return cls(
      name=req_body['name'], 
      personality=req_body['personality'], 
      color=req_body['color']
    )
  
  def update(self,req_body):
    try:
      self.name = req_body["name"]
      self.color = req_body["color"]
      self.personality = req_body["personality"]
    except KeyError as error:
      abort(make_response({'message': f"Missing attribute: {error}"}))