from flask import *

app = Flask(__name__)


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template(
        "index.html",
        header="Миссия Колонизация Марса",
        title=title,
        icon=url_for("static", filename="img/mars.jpg"),
    )
