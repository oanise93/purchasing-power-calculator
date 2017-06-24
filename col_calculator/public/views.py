# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for

from col_calculator.public.forms import LoginForm
from col_calculator.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static')


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    # form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        # if form.validate_on_submit():
        #     flash('You are logged in.', 'success')
        #     redirect_url = request.args.get('next') or url_for('user.members')
        #     return redirect(redirect_url)
        # else:
        #     flash_errors(form)
        pass
    return render_template('public/home.html',
                           # form=form
                           )

