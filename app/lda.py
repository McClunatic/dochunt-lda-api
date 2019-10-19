import sqlite3

import flask
import gensim


def get_corpus():
    if 'corpus' not in flask.g:
        flask.g.corpus = gensim.corpora.MmCorpus(
            flask.current_app.config['CORPUS'])

    return flask.g.corpus
    

def get_lda():
    if 'lda' not in flask.g:
        flask.g.lda = gensim.models.ldamodel.LdaModel.load(
            flask.current_app.config['LDA'])

    return flask.g.lda


def get_sim_index():
    if 'sim_index' not in flask.g:
        flask.g.sim_index = gensim.similarities.Similarity.load(
            flask.current_app.config['SIM_INDEX'])

    return flask.g.sim_index
    

def get_db():
    if 'db' not in flask.g:
        flask.g.db = sqlite3.connect(
            flask.current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        flask.g.db.row_factory = sqlite3.Row

    return flask.g.db


def close_db(e=None):
    db = flask.g.pop('db', None)

    if db is not None:
        db.close()
        

def init_app(app):
    app.teardown_appcontext(close_db)