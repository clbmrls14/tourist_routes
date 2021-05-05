''' A Python implementation of the algorithm proposed here: https://arxiv.org/abs/2104.07663
by Cristina Maria Pacurar, Ruxandra-Gabriela Albu, Victor-Dan Pacurar [April 15, 2021]
Implementation by Caleb Morales
'''

from typing import Tuple, List
from operator import itemgetter

def get_routes(G: List[List[Tuple[int, int]]], start_node: int, end_node: int, stops=0) -> List[Tuple[int, List[int]]]:
    # If a user doesn't specify how many attractions they will visit, we will
    #   find a route through all of them
    if stops == 0:
        stops = len(G)
    routes: List[Tuple[int, List[int]]] = []
    visited: List[bool] = [False] * len(G)

    def get_route(current_attraction: int, v: List[bool], stack: List[int] = [], time: int = 0, total_cost: int = 0):
        # We add the valid attraction to our stack
        stack.append(current_attraction)
        v[current_attraction] = True
        total_cost += time
        # We check to see if a path has been completed
        if len(stack) == stops and stack[-1] == end_node:
            routes.append((total_cost, (list(stack))))
        else:
            # For every neighboring attraction we will determine if it's eligible.
            #   If it is, recurse; adding it to the stack
            for neighbor, weight in G[current_attraction]:
                if not v[neighbor]:
                    get_route(neighbor, v, stack, weight, total_cost)
        stack.pop()
        v[current_attraction] = False
        total_cost -= time

    get_route(start_node, visited)
    return routes


def get_shortest_route(G: List[List[Tuple[int, int]]], start_node: int, end_node: int, stops=0) -> Tuple[int, List[int]]:
    routes: Tuple[int, List[int]] = get_routes(G, start_node, end_node, stops)
    return min(routes, key=itemgetter(0), default=(0, []))