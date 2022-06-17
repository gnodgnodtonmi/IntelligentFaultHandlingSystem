from dbs import db


class Car(db.Model):
    __tablename__ = "car"
    car_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_type = db.Column(db.String(10), mullable=False)
    user_id = db.Column(db.String(20), nullable=False)


