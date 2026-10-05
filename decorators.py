
from flask import (
    session,
    redirect,
    url_for,
    flash,
    abort)

from functools import wraps 
from services import UserService

def is_logged_in():
    return "username" in session

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if not is_logged_in():
            return redirect(url_for("auth.login"))
        return func(*args,**kwargs)
    return wrapper

def admin_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        role=UserService.get_role(session["username"])
        if role!="admin":
            abort(403)
        return func(*args,**kwargs)
    return wrapper
