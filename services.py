#import sqlite3
from models import db,User
class UserService:

    @staticmethod
    def get_user(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def update_username(old_username,new_username):
        user=UserService.get_user(old_username)
        if user:
            user.username=new_username
            db.session.commit()

    @staticmethod
    def update_password(username,new_hash):
        user=UserService.get_user(username)
        if user:
            user.password=new_hash
            db.session.commit()

    @staticmethod
    def delete_user(username):
        user=UserService.get_user(username)
        if user:
            db.session.delete(user)
            db.session.commit()

    @staticmethod
    def user_exists(username):
        user=UserService.get_user(username)
        return user is not None

    @staticmethod
    def create_user(username,password,register_date,role):
        user=User(username=username,
                  password=password,
                  register_date=register_date,
                  role=role)
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update_profile_image(username,image_name):
        user=UserService.get_user(username)
        if user:
            user.profile_image=image_name
            db.session.commit()

    @staticmethod
    def get_role(username):
        user=UserService.get_user(username)
        if user:
            return user.role
        return None 

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def promote_user(username):
        user=UserService.get_user(username)
        if user:
            user.role="admin"
            db.session.commit()

    @staticmethod
    def demote_user(username):
        user=UserService.get_user(username)
        if user:
            user.role="user"
            db.session.commit()

    @staticmethod
    def search_users(search):
        return User.query.filter(User.username.like(f"%{search}%")).all()

    @staticmethod
    def get_users_paginated(limit,offset):
        return User.query.limit(limit).offset(offset).all()
   
        
