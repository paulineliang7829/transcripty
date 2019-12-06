import numpy as np


def _inner_binom_simulate(
        p_i, credits, ncoursesattempted, ncreditspercourse, ncreditsgrad
    ):
    """
    Internal method used to simplify code in model credit simulation
    """
    N, Tc = credits.shape

    for i in range(N):
        for t in range(Tc):
            if np.sum(credits[i, :t]) > ncreditsgrad:
                break

            credits[i, t] = np.random.binomial(ncoursesattempted, p_i[i]) \
                * ncreditspercourse

    return None


class CreditAccumulationModel(object):
    """
    This is a parent class which implements a general credit accumulation
    method and implements a simulate method that could be used across
    various binomial credit accumulation models.

    Parameters
    ----------
    Tc : int
        The number of years an individual can stay enrolled in college
    ncoursesattempted : int
        The number of courses an individual attempts per year
    ncreditspercourse : int
        The number of credits each course is worth
    ncreditsgrad : int
        The number of credits required to graduate
    sigma : float64
        The standard deviation of the GPA shock. The higher the sigma,
        the less correlated ability and GPA are.

    Attributes
    -------
    See Parameters
    """
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
        """
        Simulates model outcomes, including ability level, GPA, and
        credit accumulation process, for `N` individuals.

        Parameters
        ----------
        N : Int
            The number of individuals that we provide a simulation for

        Returns
        -------
        a_i : np.array((N,), float64)
            The ith element is individual i's ability level
        gpa_i : np.array((N,), float64)
            The ith element is individual i's GPA
        credits : np.array((N, T_c), int)
            The [i, j] element is the number of credits accumulated by
            agent i in period j
        """
        # Unpack some variables
        ncoursesattempted = self.ncoursesattempted
        ncreditspercourse = self.ncreditspercourse
        ncreditsgrad = self.ncreditsgrad
        Tc = self.Tc
        sigma = self.sigma

        # Allocate space to store the credits
        a_i = np.random.randn(N)
        gpa_i = a_i + sigma*np.random.randn(N)
        p_i = self(a_i, gpa_i)
        credits = np.zeros((N, Tc), int)

        # Operates in-place to fill credits
        _inner_binom_simulate(
            p_i, credits, ncoursesattempted, ncreditspercourse, ncreditsgrad
        )

        return a_i, gpa_i, credits

