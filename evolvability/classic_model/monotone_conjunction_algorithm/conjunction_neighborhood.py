from evolvability.classic_model.neighborhood import Neighborhood


class MonotoneConjunctionNeighborhood(Neighborhood):
    def __init__(self):
        pass

    def get_neighborhood_of_rep(self, rep):
        """
        Returns the complete neighborhood of a representation.

        The neighborhood includes:
        - The representation itself.
        - All neighbors at Hamming distance 1 (single bit flips).
        - All neighbors formed by swapping a single 0 to a 1 and a single 1 to a 0.
        """
        neighborhood = {tuple(rep)}
        neighborhood.update(self._get_single_flip_neighbors(rep))
        neighborhood.update(self._get_swap_neighbors(rep))
        return neighborhood

    def _get_swap_neighbors(self, rep):
        """
        Generates neighbors by swapping a single 0 to a 1 and a single 1 to a 0.
        This is a specific type of Hamming distance 2 change.
        """
        swap_neighbors = set()
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
                        swap_neighbors.add(tuple(candidate))
        return swap_neighbors

    def _get_single_flip_neighbors(self, rep):
        """
        Generates all Hamming distance 1 neighbors of a representation.
        """
        neighbors = set()
        rep_list = list(rep)

        for i in range(len(rep_list)):
            candidate = list(rep_list)
            candidate[i] = 1 - rep_list[i]
            neighbors.add(tuple(candidate))

        return neighbors
