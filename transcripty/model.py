import numpy as np

from numba import jit


@jit(nopython=True)
def _inner_binom_simulate(
        p_i, credits, ncoursesattempted, ncreditspercourse, ncreditsgrad
    ):
    N, Tc = credits.shape

    for i in range(N):
        for t in range(Tc):
            if np.sum(credits[i, :t]) > ncreditsgrad:
                break

            credits[i, t] = np.random.binomial(ncoursesattempted, p_i[i]) \
                * ncreditspercourse

    return None


class CreditAccumulationModel(object):
    def __init__(
            self, Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad, sigma
        ):
        self.Tc = Tc
        self.ncoursesattempted = ncoursesattempted
        self.ncreditspercourse = ncreditspercourse
        self.ncreditsgrad = ncreditsgrad
        self.sigma = sigma

    def __call__(self, a, gpa):
        raise NotImplementedError("Must used a child-class to evaluate probs")

    def simulate(self, N):
        # Unpack some variables
        ncoursesattempted, ncreditspercourse, ncreditsgrad = self.ncoursesattempted, self.ncreditspercourse, self.ncreditsgrad
        sigma, Tc = self.sigma, self.Tc
        a_i = np.random.randn(N)
        gpa_i = a_i + sigma*np.random.randn(N)
        p_i = self(a_i, gpa_i)
        credits = np.zeros((N, Tc), int)
        _inner_binom_simulate(
            p_i, credits, ncoursesattempted, ncreditspercourse, ncreditsgrad
        )

        return a_i, gpa_i, credits

