import numpy as np

from ..model import CreditAccumulationModel


class HeterogeneousProbabilityModel(CreditAccumulationModel):
    def __init__(
            self, gamma_min, gamma_1, gamma_2,
            Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad
        ):

        # Call the parent classes init method
        super().__init__(Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad)

        # Parameters that govern passing probabilities
        self.gamma_min = gamma_min
        self.gamma_1 = gamma_1
        self.gamma_2 = gamma_2
        self.p = p

    def __call__(self, a):
        num = 1 - self.gamma_min
        den = 1 + self.gamma_1 * np.exp(-self.gamma_2 * a)

        return np.clip(num / den, 0.0, 1.0)

