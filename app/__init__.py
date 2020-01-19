from flask import Flask
from flask import redirect
from flask import url_for
from flask_cors import CORS
from flask_electron.db.flaskalchemy.database import db

from app.user import user_blueprint
from app.ingredient import ingredient_blueprint
from app.recipe import recipe_blueprint
from app.category import category_blueprint
from app.tags import tag_blueprint

_appstate = Flask(__name__, instance_relative_config=True)


def verify_release_configuration():
    """
    A pre deployment sanity check to ensure that the minimal required configuration mappings
    are present within the release deploy/config.cfg file.
    Function will look for core config members such as secret key, salts etc...
    :return True / False: True or False if verified or unverified
    :rtype bool
    """
    return False


def error_handler(error):
    if error.code == 404:
        return redirect(url_for('site_controller.index'))
    elif error.code == 429:
        return error


def create_app(env='DEV'):
    appstate = Flask(__name__, instance_relative_config=True)
    CORS(appstate, resources=r'/api/*')

    config_path = 'app.config.DevelopmentConfig'
    if env == 'DEV':
        config_path = 'app.config.DevelopmentConfig'
    elif env == 'TEST':
        config_path = 'app.config.TestingConfig'
    elif env == 'RELEASE':
        config_path = 'app.config.ReleaseConfig'

    appstate.config.from_object(config_path)
    appstate.config.from_pyfile('config.cfg', silent=True)
    appstate.app_context().push()

    appstate.register_blueprint(user_blueprint, url_prefix='/user')
    appstate.register_blueprint(ingredient_blueprint, url_prefix='/ingredient')
    appstate.register_blueprint(recipe_blueprint, url_prefix='/recipe')
    appstate.register_blueprint(category_blueprint, url_prefix='/category')
    appstate.register_blueprint(tag_blueprint, url_prefix='/tag')

    db.init_app(appstate)
    db.create_all()

    return appstate
