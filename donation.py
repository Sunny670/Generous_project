from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Profile
from . import db

donation = Blueprint('donation', __name__)

@donation.route('/')
def home():
    # Home route logic

@donation.route('/donate', methods=['GET', 'POST'])
@login_required
def donate():
    # Donation route logic

@donation.route('/donation_history')
@login_required
def donation_history():
    # Donation history route logic
