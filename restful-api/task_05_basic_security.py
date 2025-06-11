#!/usr/bin/python3
"""
This module """
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"},
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"}
}


@auth.verify_password
def check_pass(username, password):
    if username in users:
        if check_password_hash(users[username]["password"], password):
            return username


@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def login():
    return "Basic Auth: Access Granted"
