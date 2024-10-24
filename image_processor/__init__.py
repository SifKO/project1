"""
Initialiaze application
"""
import logging
from flask import Flask
from config import Config


logger = logging.getLogger()
# FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
FORMAT = '%(levelname)s : %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

app = Flask(__name__)
app.config.from_object(Config)

# from flaskapp import routes, models, errors
from image_processor import routes