import os
basedir = os.path.abspath(os.path.dirname(__file__))
from dotenv import load_dotenv

dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)

class Config:
    APP_NAME = "TimeClock"
    NAVBAR_DARK_LIGHT = 'dark'  #light or dark
    NAVBAR_BG = 'dark'  #primary, secondary, danger, warning, success, dark, info, light, body, muted, white
    BRAND_TEXT_COLOR = 'warning' # Bootstrap colors.  Same as above.
    SECRET_KEY = os.environ.get('SECRET_KEY')\
        or 'mysecretkey123456789'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')

