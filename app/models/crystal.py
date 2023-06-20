from app import db

class Crystal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    color = db.Column(db.String)
    powers = db.Column(db.String)
    charges = db.Column(db.Integer, default=0)
    healer_id = db.Column(db.Integer, db.ForeignKey('healer.id'))
    healer = db.relationship("Healer", back_populates="crystals")


    @classmethod
    def from_dict(cls, crystal_data):
        new_crystal = Crystal(
            name=crystal_data["name"],
            color=crystal_data["color"],
            powers=crystal_data["powers"],
            charges= crystal_data["charges"]
        )

        return new_crystal

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "powers": self.powers,
            "charges": self.charges if self.charges else 0
        }