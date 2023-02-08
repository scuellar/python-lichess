"""Wrappers for the [Opening
Explorer](https://lichess.org/api#tag/Opening-Explorer/operation/openingExplorerLichess)
"""
import lichess.api as api

class OpeningExApiClient(api.DefaultApiClient):
    base_url = 'https://explorer.lichess.ovh'

opening_client = OpeningExApiClient()


def openings_master(fen, **kwargs):
    """Wrapper for the `GET /masters`_ endpoint.
    
    >>> openings_m = lichess.openings.openings_master('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    >>> print([move['uci'] for move in op['moves']])
    ['e2e4', 'd2d4', 'g1f3', 'c2c4', 'g2g3', 'b2b3', 'f2f4', 'b1c3', 'b2b4', 'e2e3', 'd2d3', 'a2a3']
    """
    kwargs['fen'] = fen
    kwargs['client'] = opening_client
    return api._api_get('/masters', kwargs)

def openings_lichess(fen, **kwargs):
    """Wrapper for the `GET /lichess`_ endpoint.

    >>> openings_m = lichess.openings.openings_liches('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
    >>> print([move['uci'] for move in op['moves']])
    ['e2e4', 'd2d4', 'g1f3', 'c2c4', 'e2e3', 'g2g3', 'b2b3', 'd2d3', 'f2f4', 'b1c3', 'b2b4', 'c2c3']
    """
    kwargs['fen'] = fen
    kwargs['client'] = opening_client
    return api._api_get('/lichess', kwargs)
