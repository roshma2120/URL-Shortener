from flask import Flask, request, redirect, render_template
import string
import random
import database

app = Flask(__name__)

database.create_table()

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    if request.method == "POST":
        long_url = request.form["long_url"]
        code = generate_short_code()
        database.save_url(code, long_url)
        short_url = request.host_url + code
    return render_template("index.html", short_url=short_url)

@app.route("/<code>")
def redirect_url(code):
    long_url = database.get_url(code)
    if long_url:
        return redirect(long_url)
    return "URL not found", 404

if __name__ == "__main__":
    app.run(debug=True)
