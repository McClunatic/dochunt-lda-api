import flask

snipe = flask.Blueprint('snipe', __name__)


@snipe.route('/snipe')
def fire():
    if flask.request.args:
        return flask.jsonify(flask.request.args)
    return 'Sniping...'