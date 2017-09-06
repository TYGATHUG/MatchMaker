import os, sys
basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir[:-5])
from app import db

db.create_all()