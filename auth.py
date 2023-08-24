from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import Profile
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    # Registration route logic

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # Login route logic

@auth.route('/logout')
@login_required
def logout():
    # Logout route logic
