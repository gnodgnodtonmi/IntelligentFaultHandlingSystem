from app.dbs import db


# 车主与车辆信息
class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.String(30), primary_key=True, nullable=False)
    car_id = db.Column(db.Integer, autoincrement=True)
    car_type = db.Column(db.String(10), mullable=False)


# 将故障分为三级
class SystemFault(db.Model):
    __tablename__ = "system_fault"
    fault_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fault_name = db.Column(db.String(30), nullable=False)
    solution = db.Column(db.Integer, db.ForeignKey("solution.solution_id"), nullable=True)


class StructureFault(db.Model):
    __tablename__ = "structure_fault"
    fault_id = db.Column(db.Integer, primary_key=True)
    fault_name = db.Column(db.String(30), nullable=False)
    parent_fault = db.Column(db.Integer, db.ForeignKey("system_fault.fault_id"))
    solution = db.Column(db.Integer, db.ForeignKey("solution.solution_id"), nullable=True)


class CellFault(db.Model):
    __tablename__ = "cell_fault"
    fault_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fault_name = db.Column(db.String(30), nullable=False)
    parent_fault = db.Column(db.Integer, db.ForeignKey("structure_fault.fault_id"))
    solution = db.Column(db.Integer, db.ForeignKey("solution.solution_id"), nullable=True)
