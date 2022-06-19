from app.dbs import db


# 车主与车辆信息表
class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_id = db.Column(db.Integer, autoincrement=True)
    car_type = db.Column(db.String(10), nullable=False)


# 将故障分为三级，各一个表
class SystemFault(db.Model):
    __tablename__ = "system_fault"
    fault_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fault_name = db.Column(db.String(30), nullable=False)
    fault_type = db.Column(db.String(30), default="SystemFault")


class StructureFault(db.Model):
    __tablename__ = "structure_fault"
    fault_id = db.Column(db.Integer, primary_key=True)
    fault_name = db.Column(db.String(30), nullable=False)
    parent_fault = db.Column(db.Integer, db.ForeignKey("system_fault.fault_id"))
    fault_type = db.Column(db.String(30), default="StructureFault")


class CellFault(db.Model):
    __tablename__ = "cell_fault"
    fault_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fault_name = db.Column(db.String(30), nullable=False)

    parent_fault = db.Column(db.Integer, db.ForeignKey("structure_fault.fault_id"))
    solution = db.Column(db.Integer, db.ForeignKey("solution.solution_id"), nullable=True)
    fault_type = db.Column(db.String(30), default="CellFault")


# 解决方案表
class Solution(db.Model):
    __tablename__ = "solution"
    solution_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(60), nullable=False)
    step = db.Column(db.String(128), nullable=True)
    picture = db.Column(db.String(128), nullable=True)


# 方案步骤表
class Step(db.Model):
    __tablename__ = "step"
    step_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(128), nullable=False)


# 方案图片表
class Pictures(db.Model):
    __tablename__ = "picture"
    picture_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    picture_path = db.Column(db.String(128), nullable=False)


# 常见故障表
class CommonFault(db.Model):
    __tablename__ = "common_fault"
    common_fault_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cell_fault = db.Column(db.Integer, db.ForeignKey("cell_fault.fault_id"))
