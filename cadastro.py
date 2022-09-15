import flask
import pandas as pd
from flask import Flask, render_template
from flask.globals import request
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("cadastro.html")


@app.route('/cadastrar', methods=["POST", "GET"])
def cadastrar():
    ticker = request.form["ticker"]
    valor = request.form['valor']
    con = mysql.connector.connect(
        host="localhost", database="bolsa", user="root", password="#PASSWORD#")
    cursor = con.cursor()
    comando_SQL = "insert into acoes_alvo (ticker, valor) values ('" + \
        ticker + "',"+valor+");"
    cursor.execute(comando_SQL)
    con.commit()
    con.close()
    return render_template("cadastro.html")


if __name__ == "__main__":
    app.run(debug=True)
