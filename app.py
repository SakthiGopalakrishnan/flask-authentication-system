from flask import Flask,render_template,session
from models import db,User
from routes.auth import auth_bp
from routes.profile import profile_bp
from decorators import login_required
from routes.admin import admin_bp
import os
from dotenv import load_dotenv
from flask_wtf import CSRFProtect


load_dotenv()
app=Flask(__name__)
app.secret_key=os.getenv("SECRET_KEY")
csrf = CSRFProtect(app)

basedir = os.path.abspath(
    os.path.dirname(__file__)
)

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"sqlite:///{os.path.join(basedir,'users.db')}"
db.init_app(app)
app.register_blueprint(
    auth_bp
)
app.register_blueprint(profile_bp)
app.register_blueprint(admin_bp)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html",username=session['username'])

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"),404

@app.errorhandler(403)
def forbidden(error):
    return render_template("403.html"),403

@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"),500

@app.route("/test-500")
def test_500():
    user = None
    return user.username

if __name__=="__main__":
    app.run(debug=True)