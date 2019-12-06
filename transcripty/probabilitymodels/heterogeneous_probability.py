import numpy as np

from ..model import CreditAccumulationModel


class HeterogeneousProbabilityModel(CreditAccumulationModel):
    """
    This is a child class of CreditAccumulationModel. It implements a
    call method which evaluates the probability of passing courses
    given an individual's ability level and gpa. This method allows
    the parent class to take care of all simulation

    In this model, the probability with which a student passes their
    courses is given by

    .. math::

        p(a) = \\frac{1 - \gamma_\\text{min}}{1 + \\gamma_1 \\exp^{-\\gamma_2 a_i}}


    Attributes
    ----------
    gamma_min : float64
        The minimum probability of passing a course
    gamma_1 : float64
        A parameter of the probability function
    gamma_2 : float64
        A parameter of the probability function
    sigma : float64
        The standard deviation of the GPA shock. The higher the sigma,
        the less correlated ability and GPA are.
    Tc : int
        The number of years an individual can stay enrolled in college
    ncoursesattempted : int
        The number of courses an individual attempts per year
    ncreditspercourse : int
        The number of credits each course is worth
    ncreditsgrad : int
        The number of credits required to graduate

    """
    def __init__(
            self, gamma_min, gamma_1, gamma_2, sigma,
            Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad
        ):

        # Call the parent classes init method
        super().__init__(
            Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad, sigma
        )

        # Parameters that govern passing probabilities
        self.gamma_min = gamma_min
        self.gamma_1 = gamma_1
        self.gamma_2 = gamma_2

    def __call__(self, a, gpa):
        num = 1 - self.gamma_min
        den = 1 + self.gamma_1 * np.exp(-self.gamma_2 * a)

        return np.clip(num / den, 0.0, 1.0)

