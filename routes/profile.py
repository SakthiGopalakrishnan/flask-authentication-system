from flask import Blueprint,session,render_template,redirect,url_for,request,flash
from decorators import login_required
from services import UserService
from werkzeug.security import generate_password_hash,check_password_hash

profile_bp = Blueprint(
    "profile",
    __name__
)

@profile_bp.route("/profile")
@login_required
def profile():
    #with get_connection() as conn:
        #cur=conn.cursor()
        #cur.execute("""
        #SELECT * FROM users
        #WHERE username=?""",(session["username"],))
        #user=cur.fetchone()
    user=UserService.get_user(session["username"])
    return render_template("profile.html",user=user)

@profile_bp.route("/edit-profile")
@login_required
def edit_profile():
    # with get_connection() as conn:
    #     cur=conn.cursor()
    #     cur.execute("""
    #     SELECT * FROM users
    #     WHERE username=?""",(session["username"],))
    #     user=cur.fetchone()
    user=UserService.get_user(session["username"])
    return render_template("edit_profile.html",user=user)

@profile_bp.route("/update-profile",methods=['POST'])
@login_required
def update_profile():
    new_username=request.form["username"].strip()
    # with get_connection() as conn:
    #     cur=conn.cursor()
    if new_username != session["username"]:
        #     cur.execute("""
        # SELECT * FROM users
        # WHERE username=?""",(new_username,))
        #     existing_user=cur.fetchone()
        #     if existing_user:
        if UserService.user_exists(new_username):
            flash("User already exists")
            return redirect(url_for("profile.edit_profile"))
        # cur.execute("""
        # UPDATE users
        # SET username=?
        # WHERE username=?""",(new_username,session["username"]))
        # conn.commit()
    UserService.update_username(session["username"],new_username)
    session["username"]=new_username
    flash("Profile Updated Successfully")
    return redirect(url_for("profile.profile"))

@profile_bp.route("/change-password")
@login_required
def change_password():
    return render_template("change_password.html")

@profile_bp.route("/update-password",methods=['POST'])
@login_required
def update_password():
    old_password=request.form["old_password"]
    new_password=request.form["new_password"]
    # with get_connection() as conn:
    #     cur=conn.cursor()
    #     cur.execute("""
    #     SELECT * FROM users
    #     WHERE username=?""",(session["username"],))
    #     user=cur.fetchone()
    user=UserService.get_user(session["username"])
    if not check_password_hash(user.password,old_password):
        flash("Incorrect Old Password")
        return redirect(url_for("profile.change_password"))
    new_hash=generate_password_hash(new_password)
        # cur.execute("""
        # UPDATE users
        # SET password=?
        # WHERE username=?""",(new_hash,session["username"]))
        # conn.commit()
    UserService.update_password(session["username"],new_hash)
    flash("Password Updated Successfully")
    return(redirect(url_for("profile.profile")))

@profile_bp.route("/delete-account")
@login_required
def delete_account():
    return render_template("delete_account.html")

@profile_bp.route("/confirm-delete-account",methods=['POST'])
@login_required
def confirm_delete_account():
    password=request.form["password"]
    # with get_connection() as conn:
    #     cur=conn.cursor()
    #     cur.execute("""
    #     SELECT * FROM
    #     users WHERE username=?""",(session["username"],))
    #     user=cur.fetchone()
    user=UserService.get_user(session["username"])
    if not check_password_hash(user.password,password):
        flash("Incorrect Password")
        return redirect(url_for("profile.delete_account"))
        # cur.execute("""
        # DELETE FROM users
        # WHERE username=?""",(session["username"],))
        # conn.commit()
    UserService.delete_user(session["username"])
    session.clear()
    flash("Account Deleted Successfully")
    return redirect(url_for("home"))

@profile_bp.route("/upload-profile-image")
@login_required
def upload_profile_image():
    return render_template("upload_profile_image.html")

@profile_bp.route("/save-profile-image",methods=['POST'])
@login_required
def save_profile_image():
    file=request.files["profile_image"]
    filename=file.filename
    file.save(f"static/uploads/{filename}")
    UserService.update_profile_image(session["username"],filename)
    flash("Profile Uploaded Successfully")
    return redirect(url_for("profile.profile"))