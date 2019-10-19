import os

import flask


def create_app(test_config: dict = None) -> flask.app.Flask:
    """Factory function for creating DocHunt LDA app.

    Args:
      test_config: Configuration to use when testing.

    Returns:
      DocHunt LDA Flask app.

    """

    # create and configure the app
    app = flask.Flask('dochunt-lda-api', instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

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
    def welcome():
        return 'Welcome from Flask!'

    return app
