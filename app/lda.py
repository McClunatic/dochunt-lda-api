import flask
import gensim


def get_corpus():
    if 'corpus' not in flask.g:
        flask.g.corpus = gensim.corpora.MmCorpus(
            flask.current_app.config['CORPUS'])

    return flask.g.corpus


def get_sim_index():
    if 'sim_index' not in flask.g:
        flask.g.sim_index = gensim.similarities.Similarity.load(
            flask.current_app.config['SIM_INDEX'])

    return flask.g.sim_index
