import numpy as np

from ..model import CreditAccumulationModel


class HeterogeneousProbabilityModel(CreditAccumulationModel):
    def __init__(
            self, gamma_min, gamma_1, gamma_2, sigma,
            Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad
        ):

        super().__init__(
            Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad, sigma
        )
        self.gamma_min = gamma_min
        self.gamma_1 = gamma_1
        self.gamma_2 = gamma_2

    def __call__(self, a, gpa):
        num = 1 - self.gamma_min
        den = 1 + self.gamma_1 * np.exp(-self.gamma_2 * a)

        return np.clip(self.gamma_min + num / den, 0.0, 1.0)

