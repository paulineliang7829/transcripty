from ..model import CreditAccumulationModel


class CommonProbabilityModel(CreditAccumulationModel):
    def __init__(
            self, p, Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad
        ):

        # Call the parent classes init method
        super().__init__(Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad)

        # All individuals share a probability of passing courses that
        # we will call p
        self.p = p

    def __call__(self, a):
        if len(np.shape(a)) == 0:
            return self.p
        else:
            return np.ones_like(a)*self.p

