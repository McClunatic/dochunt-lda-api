import operator

import flask

from . import lda

snipe = flask.Blueprint('snipe', __name__)


@snipe.route('/snipe')
def fire():
    if flask.request.args:
        index = flask.request.args.get('target', type=int)
        corpus = lda.get_corpus()
        sim_index = lda.get_sim_index()
        sim_index.num_best = flask.request.args.get('num_best', 10, type=int)
        results = sim_index[corpus[index]]
        return flask.jsonify([
            {'index': idx.item(), 'similarity': sim.item()}
            for (idx, sim) in results])
    return 'Sniping...'
