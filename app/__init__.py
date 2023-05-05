"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa84jhp8u791gsmes0-a.oregon-postgres.render.com",
        database="todo_bcyg",
        user="todo_bcyg_user",
        password="sNdCOrnhcAd7mkzNiG0dXKE47aFeasA3")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
