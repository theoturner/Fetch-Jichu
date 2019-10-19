from flask import Flask

app = Flask(__name__)
# Load secret key using local config / env var in production
app.config["SECRET_KEY"] = "session-cookie-signing-key"
