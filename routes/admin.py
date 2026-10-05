from flask import Blueprint,session,render_template,redirect,url_for,request,flash
from services import UserService
from decorators import login_required,admin_required

admin_bp = Blueprint(
    "admin",
    __name__
)

@admin_bp.route("/admin")
@login_required
@admin_required
def admin():
    #return "Welcome Admin"
    search=request.args.get("search")
    if search:
        users=UserService.search_users(search)
    else:
        #users=UserService.get_all_users()
        page=int(request.args.get("page",1))
        limit=2
        offset=(page-1)*limit
        users=UserService.get_users_paginated(limit,offset)
    return render_template("admin.html",users=users,page=page if not search else 1)

@admin_bp.route("/promote/<username>")
@login_required
@admin_required
def promote(username):
    UserService.promote_user(username)
    flash(f"{username} promoted to admin")
    return redirect(url_for("admin.admin"))

@admin_bp.route("/demote/<username>")
@login_required
@admin_required
def demote(username):
    UserService.demote_user(username)
    flash(f"{username} demoted to user")
    return redirect(url_for("admin.admin"))

@admin_bp.route("/delete-user/<username>")
@login_required
@admin_required
def delete_user_admin(username):
    if username==session["username"]:
        flash("You can't delete yourself")
        return redirect(url_for("admin.admin"))
    UserService.delete_user(username)
    flash(f"{username} deleted")
    return redirect(url_for("admin.admin"))