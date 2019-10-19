from flask import Flask, render_template, request, redirect, url_for
from contract import ContractDeployer

app = Flask(__name__)
# Load secret key using local config / env var in production
app.config["SECRET_KEY"] = "session-cookie-signing-key"
app.cd = ContractDeployer('127.0.0.1', 8000)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/deploy", methods = ["POST"])
def deploy():
    contract = request.form['contract']
    app.cd.deploy(contract)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()