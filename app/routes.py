from flask import (
    Flask,
    render_template,
    request
)
import requests

app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:5000/data_types"

@app.get("/")
def get_index():
    response = requests.get(BACKEND_URL)
    scan_data = response.json().get("data_types")
    return render_template("main.html", data_types=scan_data)


@app.get("/floats")
def get_floats_page():
    url = "%s/%s" % (BACKEND_URL, "floats")
    response = requests.get(url)
    float_data = response.json().get("data_type")
    return render_template("data_type.html", data_type=float_data[0])

@app.get("/create/data_types")
def get_data_type_from():
    return render_template("new.html")

@app.post("/create/data/types")
def create_data_type():
    form_data = request.form
    new_dt = {
        "name": form_data.get("name"),
        "summary": form_data.get("summary"),
        "description": form_data.get("description")
    }
    response = requests.post(BACKEND_URL, json=new_dt)
    if response.status_code == 204:
        return render_template("new_success.html")
    else:
        return render_template("failed.html")