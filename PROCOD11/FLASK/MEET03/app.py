from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = True
app.config["PERMANENT_SESSION_LIFETIME"] = 300
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "uxDUhawQOqPuLibb3gtQsQ"
Session(app)

#notes = []

@app.route("/", methods={"GET", "POST"})
def index():
    if session.get["notes"] is None:
        session["notes"] = []

    if request.method == "POST" :
        note = request.form.get("note")
        #notes.append(note)
        session["notes"].append(note)

    return render_template("index.html", notes=session["notes"])

@app.route("/login", methods=["GET", "POST"])
def login():

    return render_template("login.html")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)