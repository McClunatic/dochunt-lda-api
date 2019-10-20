import operator

import flask

from . import lda

snipe = flask.Blueprint('snipe', __name__)


@snipe.route('/snipe')
def fire():
    if flask.request.args:
        id_ = flask.request.args.get('target')
        db = lda.get_db()
        cursor = db.execute('select "index" from articles where id = ?', (id_,))
        index = cursor.fetchone()['index']
        corpus = lda.get_corpus()
        sim_index = lda.get_sim_index()
        sim_index.num_best = flask.request.args.get('num_best', 10)
        results = sim_index[corpus[index]]
        return flask.jsonify([
            {'similarity': sim.item(),
             **dict(db.execute('select "id", title, author, date '
                               'from articles where "index" = ?',
                               (idx.item(),)).fetchone())}
            for (idx, sim) in results])
    return 'Sniping...'
