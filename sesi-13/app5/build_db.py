import os
from datetime import datetime
from config import db
from models import Director, Movie

if os.path.exists('final_proj.db'):
    os.remove('final_proj.db')

# Create the database
db.create_all()

db.session.commit()