import os

import flask
import flask_cors


def create_app(test_config: dict = None) -> flask.app.Flask:
    """Factory function for creating DocHunt LDA app.

    Args:
      test_config: Configuration to use when testing.

    Returns:
      DocHunt LDA Flask app.

    """

    # create and configure the app
    app = flask.Flask(__name__, instance_relative_config=True)
    flask_cors.CORS(app, origins="http://localhost:8081")
    ringer_path = os.path.abspath('../ringer-scraping')
    app.config.from_mapping(
        SECRET_KEY='dev',
        CORPUS=os.path.join(ringer_path, 'the-ringer-2019-11-07.mm'),
        SIM_INDEX=os.path.join(ringer_path, 'the-ringer-2019-11-07.index'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says welcome
    @app.route('/')
    def welcome():  # pylint: disable=unused-variable
        return 'Welcome from Flask!'

    from . import snipe
    app.register_blueprint(snipe.snipe)

    return app
