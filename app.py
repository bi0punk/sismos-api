from flask import Flask, render_template, jsonify
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    table_MN = pd.read_html('https://www.sismologia.cl/sismicidad/catalogo/2022/11/20221107.html')
    print(f'Total tables: {len(table_MN)}')
    df = table_MN[1]

    data = df.to_json(orient='index')
    """ return (data) """

    return (data)
    
    """ return jsonify(df) """




