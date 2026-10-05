from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    request,
    flash
)
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from services import UserService
from decorators import is_logged_in

auth_bp = Blueprint(
    "auth",
    __name__
)

@auth_bp.route("/login")
def login():
    #if "username" in session:
    if is_logged_in():
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('home'))

@auth_bp.route("/register")
def register_page():
    #if "username" in session:
    if is_logged_in():
        return redirect(url_for("dashboard"))
    return render_template("register.html")

@auth_bp.route("/submit-register",methods=["POST"])
def register():
    username=request.form["username"].strip()
    password=request.form["password"].strip()
    register_date=datetime.now().strftime("%d-%m-%Y")
    role="user"
    if username=="" or password=="":
        flash("Username and Password are required")
        return redirect(url_for("auth.register_page"))
    if len(username)<3:
        flash("Username must be atleast 3 characters")
        return redirect(url_for("auth.register_page"))
    hashed_password=generate_password_hash(password)
    #conn=sqlite3.connect("users.db")
    try:
        #conn=get_connection()
    #     with get_connection() as conn:
    #         cur=conn.cursor()
    #         cur.execute("""SELECT * FROM users
    # WHERE username=?""",(username,))
    #         user=cur.fetchone()
        user=UserService.get_user(username)
        if user:
                #conn.close()
                #return "Username already exists"
            flash("Username already exists")
            return redirect(url_for('auth.register_page'))
    #         cur.execute("""
    # INSERT INTO users(username,password,register_date)
    # VALUES(?,?,?)""",(username,hashed_password,register_date))
    #         conn.commit()
        UserService.create_user(username,hashed_password,register_date,role)
            #conn.close()
            #return "User Registered Successfully"
        flash("User Registered Successfully")
        return redirect(url_for("auth.login"))
            #return f"{username} {password}"
            #return render_template("register.html")
    except Exception as e:
        flash("Something went wrong")
        return redirect(url_for("auth.register_page"))
    """finally:
        conn.close()"""

@auth_bp.route("/submit-login", methods=["POST"])
def submit_login():
    username = request.form["username"]
    password = request.form["password"]
    #conn=sqlite3.connect("users.db")
    # conn=get_connection()
    # cur=conn.cursor()
    # cur.execute("""
    # SELECT * FROM users
    # WHERE username=?""",(username,))
    # user=cur.fetchone()
    user=UserService.get_user(username)
    if user is None:
        #return "User does not exist"
        flash("User does not exist")
        return redirect(url_for("auth.login"))
    #if user and password==user[2]:
    if user and check_password_hash(user.password,password):
        session['username']=username
        #return "Login Successful"
        flash("Login Successful")
        return redirect(url_for("dashboard"))
    #return "Invalid Password" 
    flash("Invalid Password")
    return redirect(url_for("auth.login"))
    #return f"{username} {password}"

@auth_bp.route("/forgot-password")
def forgot_password():
    return render_template("forgot_password.html")

@auth_bp.route("/check-user",methods=['POST'])
def check_user():
    username=request.form["username"]
    if not UserService.user_exists(username):
        flash("User does not exist")
        return redirect(url_for("auth.forgot_password"))
    return render_template("reset_password.html",username=username)

@auth_bp.route("/reset-password",methods=['POST'])
def reset_password():
    username=request.form["username"]
    new_password=request.form["new_password"]
    new_hash=generate_password_hash(new_password)
    if new_password.strip()=="":
        flash("Password is required")
        return redirect(url_for("auth.forgot_password"))
    UserService.update_password(username,new_hash)
    flash("Password Reset Successfully")
    return redirect(url_for("auth.login"))

