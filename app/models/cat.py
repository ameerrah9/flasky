from app import db

class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    personality = db.Column(db.String, nullable=False)

    def to_dict(self):
        return dict(
            id=self.id, 
            name=self.name, 
            color=self.color,
            personality=self.personality
    )