from evolvability.with_population.monotone_conjunction_algorithm.conjunction_algorithm import (
    MutationConjunctionAlgorithm,
)


class HGTConjunctionAlgorithm(MutationConjunctionAlgorithm):
    def __init__(self, mutator, length, epsilon, performance_oracle, population_factor=1):
        super(HGTConjunctionAlgorithm, self).__init__(
            mutator, length, epsilon, performance_oracle, population_factor
        )

        self.generation_size = self.parallel_time_steps
