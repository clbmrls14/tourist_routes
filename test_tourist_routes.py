from tourist_routes import *


def test_get_all_routes():
    G = [
        [(1, 4), (2, 1)],
        [(0, 4), (2, 2), (3, 1)],
        [(0, 1), (1, 2), (3, 4)],
        [(1, 1), (2, 4)]
    ]
    assert get_routes(G, 0, 3) == [(10, [0, 1, 2, 3]), (4, [0, 2, 1, 3])]

def test_get_all_routes_limited_stops():
    G = [
        [(1, 4), (2, 1)],
        [(0, 4), (3, 3)],
        [(0, 1), (3, 1)],
        [(1, 3), (2, 1)]
    ]
    assert get_routes(G, 0, 3, 3) == [(7, [0, 1, 3]), (2, [0, 2, 3])]

def test_get_shortest_route():
    G = [
        [(1, 4), (2, 1)],
        [(0, 4), (2, 2), (3, 1)],
        [(0, 1), (1, 2), (3, 3), (4, 7)],
        [(1, 1), (2, 3), (4, 2)],
        [(2, 7), (3, 2)]
    ]
    assert get_shortest_route(G, 0, 4) == (6, [0, 2, 1, 3, 4])
    assert get_shortest_route(G, 0, 4, 4) == (6, [0, 2, 3, 4])