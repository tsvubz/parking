from flask import Blueprint, render_template, request, url_for, flash, redirect

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@users.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


