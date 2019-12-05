import numpy as np
import scipy.stats as st


class CreditAccumulationModel(object):
    """
    This is a parent class which implements a general simulation method
    to allow for simulating different credit accumulation models
    """
    def __init__(self, Tc, ncoursesattempted, ncreditspercourse, ncreditsgrad):
        self.Tc = Tc
        self.ncoursesattempted = ncoursesattempted
        self.ncreditspercourse = ncreditspercourse
        self.ncreditsgrad = ncreditsgrad

    def __call__(self, a):
        raise NotImplementedError("Must used a child-class to evaluate probs")

    def simulate(self, N):
        """
        """
        # Unpack some variables
        ncoursesattempted = self.ncoursesattempted
        ncreditspercourse = self.ncreditspercourse
        ncreditsgrad = self.ncreditsgrad
        Tc = self.Tc

        # Allocate space to store the credits
        credits = np.zeros((N, Tc))

        # Simulate each individual
        for i in range(N):

            # Draw a random ability and create the binomial
            # distribution that governs an individual's credit
            # accumulation
            a_i = np.random.randn()
            credit_distribution = st.binom(ncoursesattempted, self(a_i))

            # Sample credits from each period they might have gone to
            # college but don't draw if they've already graduated
            for t in range(Tc):
                if np.sum(credits[i, :t]) > ncreditsgrad:
                    break

                credits[i, t] = credit_distribution.rvs() * ncreditspercourse

        return credits

