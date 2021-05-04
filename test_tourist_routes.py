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

def test_brasov_old_city():
    brasov = [
        [(1, 1), (4, 8)],                       # 0
        [(0, 1), (2, 10)],                      # 1 
        [(1, 10), (3, 9), (4, 5), (16, 5)],     # 2
        [(2, 9), (17, 5), (19, 15), (20, 14)],  # 3
        [(2, 5), (5, 1), (13, 4), (16, 2)],     # 4
        [(4 ,1), (6, 7), (13, 4)],              # 5
        [(5, 7), (7, 4), (8, 4)],               # 6
        [(6, 4), (8, 2)],                       # 7
        [(7, 5), (9, 5)],                       # 8
        [(8, 5), (10, 2), (11, 2)],             # 9
        [(9, 2), (11, 2), (14, 5), (18, 6)],    # 10
        [(9, 2), (10, 2), (12, 3)],             # 11
        [()],
        [],
        [],
        [],
        [],
        [],
        [],
    ]