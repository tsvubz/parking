from flask import Blueprint, render_template, request, url_for, flash, redirect

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')
