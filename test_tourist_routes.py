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

def test_get_shortest_route_1():
    G = [
        [(1, 4), (2, 1)],
        [(0, 4), (2, 2), (3, 1)],
        [(0, 1), (1, 2), (3, 3), (4, 7)],
        [(1, 1), (2, 3), (4, 2)],
        [(2, 7), (3, 2)]
    ]
    assert get_shortest_route(G, 0, 4) == (6, [0, 2, 1, 3, 4])
    assert get_shortest_route(G, 0, 4, 4) == (6, [0, 2, 3, 4])

def test_get_shortest_route_2():
    G = [
        [(1, 2), (2, 1), (3, 3), (4, 2)],
        [(0, 2), (2, 2), (6, 4)],
        [(0, 1), (1, 2)],
        [(0, 3), (4, 2), (8, 3)],
        [(0, 2), (3, 2), (8, 3)],
        [(4, 1), (6, 5), (7, 1)],
        [(1, 4), (5, 5)],
        [(4, 2), (5, 1), (8, 7)],
        [(3, 3), (4, 3), (7, 7)]
    ]
    assert get_shortest_route(G, 0, 8) == (20, [0, 2, 1, 6, 5, 7, 4, 3, 8])

def test_brasov_old_city():
    brasov = [
        [(1, 1), (4, 8)],                                       # 0: First Romanian School
        [(0, 1), (2, 10)],                                      # 1: Saint Nicholas Church
        [(1, 10), (3, 9), (4, 5), (16, 5)],                     # 2: Weaver's Fortress
        [(2, 9), (17, 5), (19, 15), (20, 14)],                  # 3: Tampa Cable Way
        [(2, 5), (5, 1), (13, 4), (16, 2)],                     # 4: Schei's Gate
        [(4 ,1), (6, 7), (13, 4)],                              # 5: Catherine's Gate
        [(5, 7), (7, 4), (8, 4)],                               # 6: Black Tower
        [(6, 4), (8, 2)],                                       # 7: White Tower
        [(7, 5), (9, 5)],                                       # 8: Graft Fortress
        [(8, 5), (10, 2), (11, 2)],                             # 9: George Baritiu County Library
        [(9, 2), (11, 2), (14, 5), (18, 6)],                    # 10: Rectorate of Transilvania University of Brasov
        [(9, 2), (10, 2), (12, 3)],                             # 11: House of Army
        [(10, 2), (11, 3), (19, 4), (21, 9)],                   # 12: Annunciation Church
        [(4, 4), (5, 4), (14, 2), (15, 3), (16, 5), (17, 5)],   # 13: Black Church
        [(10, 5), (13, 2), (15, 1)],                            # 14: Council Square
        [(13, 3), (17, 6)],                                     # 15: History Museum
        [(2, 5), (4, 2), (13, 5), (17, 1)],                     # 16: Synagogue
        [(3, 10), (13, 5), (15, 6), (16, 1)],                   # 17: Rope Street
        [(10, 6), (19, 4)],                                     # 18: Art Museum
        [(3, 15), (12, 4), (18, 4), (20, 5)],                   # 19: Town Hall
        [(3, 14), (19, 5)],                                     # 20: Theater
        [(12, 9)],                                              # 21: The Citadel
    ]
    assert get_shortest_route(brasov, 20, 21) == (101, [20, 19, 18, 10, 14, 15, 13, 16, 17, 3, 2, 1, 0, 4, 5, 6, 7, 8, 9, 11, 12, 21])

def test_lagoon():
    lagoon = [
        [(1, 2), (9, 5), (10, 5), (11, 4), (12, 5)],        # 0: Memorial Fountain
        [(0, 2), (2, 2)],                                   # 1: Dracula's Castle
        [(1, 2), (3, 2), (4, 1)],                           # 2: Space Scrambler
        [(2, 2), (4, 2)],                                   # 3: Skycoaster
        [(2, 1), (3, 2), (5, 4), (8, 3)],                   # 4: Double Thunder Raceway
        [(4, 4), (6, 6), (7, 4)],                           # 5: Sky Scraper
        [(5, 6), (7, 1)],                                   # 6: Rocket
        [(5, 4), (6, 1), (8, 2)],                           # 7: Catapult
        [(4, 3), (7, 2), (9, 3)],                           # 8: Jet Star 2
        [(0, 5), (8, 3), (10, 5), (18, 10)],                # 9: Bat
        [(0, 5), (9, 5), (11, 2), (17, 2), (18, 3)],        # 10: Puff
        [(0, 4), (10, 2), (12, 2), (13, 5), (14, 5)],       # 11: Merry Go Round
        [(0, 5), (11, 2), (14, 3)],                         # 12: Roller Coaster
        [(11, 5), (14, 2), (15, 2), (16, 2), (17, 4)],      # 13: Wild Mouse
        [(11, 5), (12, 3), (13, 2), (15, 1)],               # 14: Spider
        [(13, 2), (14, 1), (16, 3)],                        # 15: Wicked
        [(13, 2), (15, 3)],                                 # 16: Colossus
        [(10, 2), (13, 4), (18, 4)],                        # 17: Tidal Wave
        [(9, 10), (10, 3), (17, 4), (19, 2)],               # 18: Rattlesnake Rapids
        [(18, 2)],                                          # 19: Pioneer Village
    ]
    assert get_shortest_route(lagoon, 0, 19, 6) == (14, [0, 11, 10, 17, 18, 19])