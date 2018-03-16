import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
app = Flask(__name__)

#################################################
# Database Setup
#################################################
dbfile = os.path.join('db', 'gun_violence.sqlite')
engine = create_engine(f"sqlite:///{dbfile}") 

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to tables
Gun_sales = Base.classes.gun_sales
Gun_law_grade= Base.classes.gun_law_grade
Mass_shootings = Base.classes.mass_shootings
Murder_2015 = Base.classes.Murder_2015
Murder_2016 = Base.classes.Murder_2016
State_laws_by_year = Base.classes.State_laws_by_year

# Create our session (link) from Python to the DB
session = Session(engine)





@app.route("/")
def index():
    """Return the homepage."""
    return render_template('index.html')

@app.route('/<state>')
def state_data(state):
    state_info= []



