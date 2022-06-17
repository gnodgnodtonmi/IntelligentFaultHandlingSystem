from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# 数据库的配置变量
HOSTNAME = '47.112.216.3'
PORT = '3306'
DATABASE = 'ifhs_db'
USERNAME = 'root'
PASSWORD = 'mysql1010'
DB_URI = 'mysql+pymysql://root:mysql1010@47.112.216.3:3306/ifhs_db?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


class Car(db.Model):
    __tablename__ = "car"
    car_type_id = db.Column(db.String(10), primary_key=True)
    user_id = db.Column(db.String(20), nullable=False)


# class CommonFault:
#     __tablename__ = "common fault"
#     CarTypeId = db.Column(db.JSON, primary_key=True)

class WholeFault(db.Model):
    __tablename__ = "whole fault"
    fault_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fault_name = db.Column(db.String(20), nullable=False)

    car_type_id = db.Column(db.String(10), db.ForeignKey("car.car_type_id"))


db.create_all()
