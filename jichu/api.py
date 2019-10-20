from flask import Flask, render_template, request, redirect, url_for
from contract import ContractDeployer

app = Flask(__name__)
# Load secret key using local config / env var in production
app.config["SECRET_KEY"] = "session-cookie-signing-key"
txhash = ''

@app.route("/")
def index():
    return render_template("index.html", txhash = txhash)

@app.route("/deploy", methods = ["POST"])
def deploy():
    # Server-side cookie to get around this golbal dropping Quart, no async!
    global txhash
    address = request.form['address']
    contract = request.form['contract']
    cd = ContractDeployer(address, 8000)
    txhash = cd.deploy(contract)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()