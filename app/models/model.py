from app.dbs import db


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.String(30), primary_key=True, nullable=False)
    car_id = db.Column(db.Integer, autoincrement=True)
    car_type = db.Column(db.String(10), mullable=False)


# class Wholefault(db.Model):
#     __tablename__ = "wholefault"
class SystemFault(db.Model):
    __tablename__ = "system_fault"
    fault_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fault_name = db.Column(db.String(30), nullable=False)
