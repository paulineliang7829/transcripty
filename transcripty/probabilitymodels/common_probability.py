import numpy as np

from ..model import CreditAccumulationModel


class CommonProbabilityModel(CreditAccumulationModel):
    """
    This is a child class of CreditAccumulationModel. It implements a
    call method which evaluates the probability of passing courses
    given an individual's ability level and gpa. This method allows
    the parent class to take care of all simulation

    In this model, all individual's share a probability of passing
    a course.

    Attributes
    ----------
    p : float64
        The common probability of passing a course
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
            self, p, sigma, Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad
        ):

        # Call the parent classes init method
        super().__init__(
            Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad, sigma
        )

        # All individuals share a probability of passing courses that
        # we will call p
        self.p = p

    def __call__(self, a, gpa):
        if len(np.shape(a)) == 0:
            return self.p
        else:
            return np.ones_like(a)*self.p

