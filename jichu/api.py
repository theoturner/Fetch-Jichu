from flask import Flask, render_template

app = Flask(__name__)
# Load secret key using local config / env var in production
app.config["SECRET_KEY"] = "session-cookie-signing-key"


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()