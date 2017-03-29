# -*- coding:utf-8 -*-
from flask import Flask
import pymysql
from config import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False)
    city = db.Column(db.String(10), unique=False)
    passwd = db.Column(db.String(20), unique=False)
    type = db.Column(db.String(8), unique=False)
    style = db.Column(db.String(8), unique=False)
    qty = db.Column(db.Integer, unique=False)
    price = db.Column(db.Float, unique=False)
    remark = db.Column(db.Text(200), unique=False)

    # def __init__(self, name, city, passwd, type, style, qty, price, remark):
    #     self.name = name
    #     self.city = city
    #     self.passwd = passwd
    #     self.type = type
    #     self.style = style
    #     self.qty = qty
    #     self.price = price
    #     self.remark = remark
if __name__ == '__main__':
    db.create_all()
    # print Products.query.all()

