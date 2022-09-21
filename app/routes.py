from flask import (
    Flask,
    render_template
)
import requests

app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:5000/data_types"

@app.get("/")
def get_index():
    scan_data = requests.get(BACKEND_URL)
    return render_template("main.html", data_types=scan_data)



