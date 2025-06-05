import distance

from evolvability.classic_model.neighborhood import Neighborhood



class MonotoneConjunctionNeighborhood(Neighborhood):
    def __init__(self):
        pass

    def get_neighborhood_of_rep(self, rep):
        return self.get_rep_plus_and_rep_minus(rep) | self.get_rep_plus_minus(rep)

    def get_rep_plus_minus(self, rep):
        rep_plus_minus = set()
        n = len(rep)
        original_rep_list = list(rep)

        for i in range(n):  # Index for potential 'plus' operation (0 -> 1)
            if original_rep_list[i] == 0:
                for j in range(n):  # Index for potential 'minus' operation (1 -> 0)
                    if i == j:  # Operations must be on different bits
                        continue
                    if original_rep_list[j] == 1:
                        candidate = list(original_rep_list)
                        candidate[i] = 1  # Plus operation
                        candidate[j] = 0  # Minus operation
                        rep_plus_minus.add(tuple(candidate))
        return rep_plus_minus

    def get_rep_plus_and_rep_minus(self, rep):
        rep_plus_and_rep_minus = set()
        rep_plus_and_rep_minus.add(tuple(rep))

        rep = list(rep)

        for i in range(len(rep)):
            rep_plus_and_rep_minus.add(tuple(rep[:i] + [1 - rep[i]] + rep[i+1:]))

        return rep_plus_and_rep_minus
