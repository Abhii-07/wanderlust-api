from app import db

# class Destination(db.Model):
#     # Destination model definition

# class Itinerary(db.Model):
#     # Itinerary model definition

# class Expense(db.Model):
#     # Expense model definition

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    location = db.Column(db.String(100))

class Itinerary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'))
    activity = db.Column(db.String(200))

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'))
    category = db.Column(db.String(100))
    amount = db.Column(db.Float)
