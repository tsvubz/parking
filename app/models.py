from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    """
    User model for the application.
    """
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def set_password(self, password):
        """
        Hash the password using generate_password_hash.
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
        Check the hashed password using check_password_hash.
        """
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"User('{self.user_name}', '{self.email}')"


class Vehicle(db.Model):
    """
    Vehicle model for the application.
    """
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(20), nullable=False)
    make = db.Column(db.String(50), nullable=True)
    model = db.Column(db.String(50), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Vehicle('{self.license_plate}', '{self.make}', '{self.model}')"

class ParkingSpot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(100))
    spot_number = db.Column(db.String(10))
    is_available = db.Column(db.Boolean, default=True)
    image = db.Column(db.String(100))  # URL or path to the image of the parking spot
    bookings = db.relationship('Booking', backref='spot', lazy='dynamic')

    def __repr__(self):
        return f"ParkingSpot('{self.location}', '{self.spot_number}', Available: {self.is_available})"

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, index=True)
    start_time = db.Column(db.DateTime, index=True)
    end_time = db.Column(db.DateTime, index=True)
    status = db.Column(db.String(20))  # 'confirmed', 'cancelled', 'completed'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    spot_id = db.Column(db.Integer, db.ForeignKey('parking_spot.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))

    def __repr__(self):
        return f"Booking('{self.date}', '{self.start_time}', '{self.end_time}', Status: {self.status})"