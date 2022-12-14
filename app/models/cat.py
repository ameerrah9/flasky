from app import db

class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    personality = db.Column(db.String, nullable=False)
    pet_count = db.Column(db.Integer)
    caretaker_id = db.Column(db.Integer, db.ForeignKey("caretaker.id"))
    caretaker = db.relationship("Caretaker", back_populates="cats")


    @classmethod
    def from_dict(cls, data_dict):
        return cls(name=data_dict["name"],
            color=data_dict["color"],
            personality=data_dict["personality"],
            pet_count=data_dict["pet_count"],
            )

    def to_dict(self):
        caretaker_name = self.caretaker.name if self.caretaker else ""

        return dict(
            id=self.id,
            name=self.name,
            color=self.color,
            personality=self.personality,
            pet_count=self.pet_count,
            caretaker=caretaker_name,
        )