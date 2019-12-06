import numpy as np

from ..model import CreditAccumulationModel


class CommonProbabilityModel(CreditAccumulationModel):
    def __init__(
            self, p, sigma, Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad
        ):
        super().__init__(
            Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad, sigma
        )
        self.p = p

    def __call__(self, a, gpa):
        if len(np.shape(a)) == 0:
            return self.p
        else:
            return np.ones_like(a)*self.p

