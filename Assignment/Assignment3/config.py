import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'people.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://owxetcxykqigsm:50a02a4ae1cd4baf043798fc9b64182cae0be2ebf1d5ed240a7c79d9d7105185@ec2-3-209-124-113.compute-1.amazonaws.com:5432/deph9n6van4bop' + os.path.join(basedir, 'people.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# uri = os.getenv("DATABASE_URL")
# if uri and uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zpbbwjqhxnkdya:f97721f0434849c15296e52567d34a578647f1a4fbb1a7c193481cd944a70a09@ec2-54-80-122-11.compute-1.amazonaws.com:5432/ddpkjoo0opeb99'
# os.path.join(basedir, 'people.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)