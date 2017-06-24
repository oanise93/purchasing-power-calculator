# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from collections import OrderedDict
import pandas as pd
import os
from col_calculator.extensions import cache
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

    drop_down_data = get_dropdown_data()
    return render_template('public/home.html',
                           drop_down_data=drop_down_data
                           # form=form
                           )


@cache.cached(timeout=60*60*24, key_prefix='rpp_data')
def get_dropdown_data():
    rpp_data_file_path = os.path.join(os.getcwd(), 'data/rpp_data.csv')
    rpp_df = pd.read_csv(rpp_data_file_path)
    rpp_df.sort_values(by="State", inplace=True)
    unique_states = list(rpp_df.State.unique())
    drop_down_dict = dict()
    for state in unique_states:
        temp_df = rpp_df[rpp_df.State == state][['Name', '2015_RPP']]
        temp_df.sort_values(by='Name', inplace=True)
        drop_down_dict[state] = list()
        for index, row in temp_df.iterrows():
            temp_tuple = (row['Name'], row['2015_RPP'])
            drop_down_dict[state].append(temp_tuple)

    return drop_down_dict

